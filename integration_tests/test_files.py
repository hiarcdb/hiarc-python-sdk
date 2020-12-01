from __future__ import absolute_import
from integration_tests.hiarc_util import hiarc_util

import unittest
import hashlib
import os
from datetime import datetime, timedelta
import dateutil.parser
import pytz

import hiarc
from hiarc.rest import ApiException


class TestFileApi(unittest.TestCase):
    """FileApi unit test stubs"""

    def setUp(self):
        self.hiarc_util = hiarc_util()
        self.hiarc_config = self.hiarc_util.init_hiarc_config_admin()
        self.hiarc_users = hiarc.UserApi(hiarc.ApiClient(self.hiarc_config))
        self.hiarc_groups = hiarc.GroupApi(hiarc.ApiClient(self.hiarc_config))
        self.hiarc_collections = hiarc.CollectionApi(hiarc.ApiClient(self.hiarc_config))
        self.hiarc_files = hiarc.FileApi(hiarc.ApiClient(self.hiarc_config))
        hiarc.AdminApi(hiarc.ApiClient(self.hiarc_config)).reset_db()

    def tearDown(self):
        pass

    def test_crud(self):
        """Test case for file CRUD actions

        File CRUD  # noqa: E501
        """
        cfr = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        upf = self.hiarc_files.create_file(cfr, filepath)
        gf = self.hiarc_files.get_file(cfr.key)
        assert upf == gf

        new_name = "New Name.txt"
        new_description = "New description"
        ufr = hiarc.UpdateFileRequest(
            name=new_name, description=new_description)
        uf = self.hiarc_files.update_file(ufr, cfr.key)
        assert new_name == uf.name
        assert new_description == uf.description
        assert uf.modified_at > uf.created_at

        ufr = hiarc.UpdateClassificationRequest(key='new key')
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.update_file, ufr, cfr.key)

        self.hiarc_files.delete_file(cfr.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, cfr.key)

    def test_file_versions(self):
        """Test case for file versions actions

        File Versions  # noqa: E501
        """
        cfr = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        upf = self.hiarc_files.create_file(cfr, filepath)
        assert upf.version_count == 1

        new_version_filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'NewVersionOfTest.txt')
        nvr = hiarc.AddVersionToFileRequest(key=cfr.key)
        new_version = self.hiarc_files.add_version(
            nvr, new_version_filepath, cfr.key)
        assert new_version.modified_at > upf.modified_at
        assert new_version.version_count == 2

        nvr = hiarc.AddVersionToFileRequest(key=cfr.key)
        another_new_version = self.hiarc_files.add_version(
            nvr, new_version_filepath, cfr.key)
        assert another_new_version.modified_at > upf.modified_at
        assert another_new_version.version_count == 3

        versions = self.hiarc_files.get_versions(cfr.key)
        assert len(versions) == 3
        assert versions[0]['createdAt'] < versions[2]['createdAt']

        self.hiarc_files.delete_file(cfr.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, cfr.key)

    def test_file_versions_created_by(self):
        """Test case for file versions created by

        File Versions Created By  # noqa: E501
        """
        cfr = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        upf = self.hiarc_files.create_file(cfr, filepath)
        assert upf.version_count == 1

        u = self.hiarc_users.create_user(self.hiarc_util.create_user())
        autf = hiarc.AddUserToFileRequest(u.key, hiarc.AccessLevel.READ_WRITE)
        self.hiarc_files.add_user_to_file(autf, cfr.key)

        new_version_filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'NewVersionOfTest.txt')
        nvr = hiarc.AddVersionToFileRequest(key=cfr.key)
        new_version = self.hiarc_files.add_version(
            nvr, new_version_filepath, cfr.key, x_hiarc_user_key=u.key)
        assert new_version.modified_at > upf.modified_at
        assert new_version.version_count == 2

        versions = self.hiarc_files.get_versions(cfr.key)
        assert len(versions) == 2
        assert versions[0]['createdAt'] < versions[-1]['createdAt']
        assert versions[0]['createdBy'] == self.hiarc_util.ADMIN_NAME
        assert versions[-1]['createdBy'] == u.key

        self.hiarc_files.delete_file(cfr.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, cfr.key)

    def test_file_versions_access_level(self):
        """Test case for file versions access levels

        File Versions Access Levels  # noqa: E501
        """
        cfr = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        upf = self.hiarc_files.create_file(cfr, filepath)
        assert upf.version_count == 1

        u = self.hiarc_users.create_user(self.hiarc_util.create_user())
        autf = hiarc.AddUserToFileRequest(u.key, hiarc.AccessLevel.READ_ONLY)
        self.hiarc_files.add_user_to_file(autf, cfr.key)

        new_version_filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'NewVersionOfTest.txt')
        nvr = hiarc.AddVersionToFileRequest(key=cfr.key)
        self.assertRaises(hiarc.rest.ApiException, self.hiarc_files.add_version,
                          nvr, new_version_filepath, cfr.key, x_hiarc_user_key=u.key)

        u2 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        autf = hiarc.AddUserToFileRequest(
            u2.key, hiarc.AccessLevel.UPLOAD_ONLY)
        self.hiarc_files.add_user_to_file(autf, cfr.key)

        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, cfr.key, x_hiarc_user_key=u2.key)

        new_version_filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'NewVersionOfTest.txt')
        nvr = hiarc.AddVersionToFileRequest(key=cfr.key)
        self.hiarc_files.add_version(
            nvr, new_version_filepath, cfr.key, x_hiarc_user_key=u2.key)

        u3 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        autf = hiarc.AddUserToFileRequest(u3.key, hiarc.AccessLevel.READ_WRITE)
        self.hiarc_files.add_user_to_file(autf, cfr.key)

        new_version_filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'NewVersionOfTest.txt')
        nvr = hiarc.AddVersionToFileRequest(key=cfr.key)
        self.hiarc_files.add_version(
            nvr, new_version_filepath, cfr.key, x_hiarc_user_key=u3.key)

        u4 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        autf = hiarc.AddUserToFileRequest(u4.key, hiarc.AccessLevel.READ_WRITE)
        self.hiarc_files.add_user_to_file(autf, cfr.key)

        new_version_filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'NewVersionOfTest.txt')
        nvr = hiarc.AddVersionToFileRequest(key=cfr.key)
        self.hiarc_files.add_version(
            nvr, new_version_filepath, cfr.key, x_hiarc_user_key=u4.key)

        versions = self.hiarc_files.get_versions(cfr.key)
        assert len(versions) == 4
        assert versions[0]['createdAt'] < versions[-1]['createdAt']
        assert versions[0]['createdBy'] == self.hiarc_util.ADMIN_NAME
        assert versions[-1]['createdBy'] == u4.key

        self.hiarc_files.delete_file(cfr.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, cfr.key)

    def test_file_versions_storage(self):
        """Test case for file versions in storage services

        File Versions Storage  # noqa: E501
        """
        cfr = self.hiarc_util.create_file(
            storage=self.hiarc_util.AWS_EAST_STORAGE)
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        upf = self.hiarc_files.create_file(cfr, filepath)

        new_version_filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'NewVersionOfTest.txt')
        nvr = hiarc.AddVersionToFileRequest(key=cfr.key)
        self.hiarc_files.add_version(nvr, new_version_filepath, cfr.key)

        nvr = hiarc.AddVersionToFileRequest(
            key=cfr.key, storage_service=self.hiarc_util.AZURE_STORAGE_1)
        self.hiarc_files.add_version(nvr, new_version_filepath, cfr.key)

        nvr = hiarc.AddVersionToFileRequest(key=cfr.key)
        self.hiarc_files.add_version(nvr, new_version_filepath, cfr.key)

        versions = self.hiarc_files.get_versions(cfr.key)
        assert len(versions) == 4
        assert versions[0]['storageService'] == self.hiarc_util.AWS_EAST_STORAGE
        assert versions[1]['storageService'] == self.hiarc_util.AWS_EAST_STORAGE
        assert versions[2]['storageService'] == self.hiarc_util.AZURE_STORAGE_1
        assert versions[3]['storageService'] == self.hiarc_util.AZURE_STORAGE_1

        self.hiarc_files.delete_file(cfr.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, cfr.key)

    def test_get_allowed_files(self):
        """Test case for getting allowed files for user

        Files allowed to access  # noqa: E501
        """
        cfr1 = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(cfr1, filepath)

        cfr2 = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f2 = self.hiarc_files.create_file(cfr2, filepath)

        cfr3 = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f3 = self.hiarc_files.create_file(cfr3, filepath)

        cfr4 = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f4 = self.hiarc_files.create_file(cfr4, filepath)

        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        autf = hiarc.AddUserToFileRequest(u1.key, hiarc.AccessLevel.READ_ONLY)
        self.hiarc_files.add_user_to_file(autf, f1.key)

        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        aftc = hiarc.AddFileToCollectionRequest(f2.key)
        self.hiarc_collections.add_file_to_collection(aftc, c1.key)

        autc = hiarc.AddUserToCollectionRequest(
            u1.key, hiarc.AccessLevel.READ_ONLY)
        self.hiarc_collections.add_user_to_collection(autc, c1.key)

        c2 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c3 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.hiarc_collections.add_child_to_collection(c2.key, c3.key)

        aftc = hiarc.AddFileToCollectionRequest(f3.key)
        self.hiarc_collections.add_file_to_collection(aftc, c3.key)

        self.hiarc_collections.add_user_to_collection(autc, c2.key)

        files = [f1.key, f2.key, f3.key, f4.key]
        filter = hiarc.AllowedFilesRequest(files)
        filtered_files = self.hiarc_files.filter_allowed_files(
            filter, x_hiarc_user_key=u1.key)
        self.assertIn(f1.key, filtered_files)
        self.assertIn(f2.key, filtered_files)
        self.assertIn(f3.key, filtered_files)
        self.assertNotIn(f4.key, filtered_files)

        for f in files:
            self.hiarc_files.delete_file(f)
            self.assertRaises(hiarc.rest.ApiException,
                              self.hiarc_files.get_file, f)

    def test_download(self):
        """Test case for downloading files

        File Download  # noqa: E501
        """
        for s in self.hiarc_util.All_STORAGE_SERVICES:
            filepath = os.path.join(
                os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
            download_filepath = os.path.join(
                os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'downloaded-Test.txt')

            cfr = self.hiarc_util.create_file(storage=s)
            f = self.hiarc_files.create_file(cfr, filepath)
            self.hiarc_files.download_file(
                key=f.key, filepath=download_filepath)

            md5 = hashlib.md5(open(filepath, 'rb').read()).hexdigest()
            md52 = hashlib.md5(
                open(download_filepath, 'rb').read()).hexdigest()
            assert md5 == md52

            os.remove(download_filepath)
            self.hiarc_files.delete_file(f.key)
            self.assertRaises(hiarc.rest.ApiException,
                              self.hiarc_files.get_file, f.key)

    def test_direct_download(self):
        """Test case for file direct download

        File Direct Download  # noqa: E501
        """
        cfr = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f = self.hiarc_files.create_file(cfr, filepath)

        dd = self.hiarc_files.get_direct_download_url(f.key)
        now = datetime.now(tz=pytz.utc)
        assert dd.key == f.key
        assert dd.expires_at > now
        now_plus_ten = now + \
            timedelta(seconds=self.hiarc_util.DEFAULT_EXPIRES_IN_SECONDS)
        assert dd.expires_at < now_plus_ten

        expires_in = 60
        dd2 = self.hiarc_files.get_direct_download_url(
            f.key, expires_in_seconds=expires_in)
        now = datetime.now(tz=pytz.utc)
        assert dd2.expires_at > now + timedelta(seconds=expires_in-5)
        assert dd2.expires_at < now + timedelta(seconds=expires_in)

        self.hiarc_files.delete_file(cfr.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, cfr.key)

    def test_direct_upload(self):
        """Test case for file direct upload

        File Direct Upload  # noqa: E501
        """
        # cdur = hiarc.CreateDirectUploadUrlRequest()
        url = self.hiarc_files.create_direct_upload_url()
        assert url.direct_upload_url.startswith('https')

    def test_download_new_version(self):
        """Test case for downloading new version of a file

        File Download New Version  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        new_version_filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'NewVersionOfTest.txt')
        download_filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'downloaded-Test.txt')

        cfr = self.hiarc_util.create_file()
        f = self.hiarc_files.create_file(cfr, filepath)

        nvr = hiarc.AddVersionToFileRequest(key=f.key)
        self.hiarc_files.add_version(nvr, new_version_filepath, f.key)

        self.hiarc_files.download_file(key=f.key, filepath=download_filepath)
        md5 = hashlib.md5(open(new_version_filepath, 'rb').read()).hexdigest()
        md52 = hashlib.md5(open(download_filepath, 'rb').read()).hexdigest()
        assert md5 == md52

        os.remove(download_filepath)
        self.hiarc_files.delete_file(f.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f.key)

    def test_copy_file_aws(self):
        """Test case for copying a file to other storage services from AWS

        AWS File Copy  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        cfr = self.hiarc_util.create_file(
            storage=self.hiarc_util.AWS_EAST_STORAGE)
        source = self.hiarc_files.create_file(cfr, filepath)

        cfcr = self.hiarc_util.create_file_copy(
            storage=self.hiarc_util.AWS_EAST_STORAGE)
        copy = self.hiarc_files.copy_file(cfcr, source.key)
        self.assertNotEqual(source.key, copy.key)

        cfcr = self.hiarc_util.create_file_copy(
            storage=self.hiarc_util.AWS_WEST_STORAGE)
        aws_west_copy = self.hiarc_files.copy_file(cfcr, source.key)
        self.assertNotEqual(source.key, aws_west_copy.key)

        cfcr = self.hiarc_util.create_file_copy(
            storage=self.hiarc_util.AZURE_STORAGE_1)
        azure_copy = self.hiarc_files.copy_file(cfcr, source.key)
        self.assertNotEqual(source.key, azure_copy.key)

        cfcr = self.hiarc_util.create_file_copy(
            storage=self.hiarc_util.GOOGLE_EAST_STORAGE)
        google_copy = self.hiarc_files.copy_file(cfcr, source.key)
        self.assertNotEqual(source.key, google_copy.key)

        for f in [source.key, copy.key, aws_west_copy.key, azure_copy.key, google_copy.key]:
            self.hiarc_files.delete_file(f)
            self.assertRaises(hiarc.rest.ApiException,
                              self.hiarc_files.get_file, f)

    def test_copy_file_azure(self):
        """Test case for copying a file to other storage services from Azure

        Azure File Copy  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        cfr = self.hiarc_util.create_file(
            storage=self.hiarc_util.AZURE_STORAGE_1)
        source = self.hiarc_files.create_file(cfr, filepath)

        cfcr = self.hiarc_util.create_file_copy(
            storage=self.hiarc_util.AZURE_STORAGE_1)
        copy = self.hiarc_files.copy_file(cfcr, source.key)
        self.assertNotEqual(source.key, copy.key)

        cfcr = self.hiarc_util.create_file_copy(
            storage=self.hiarc_util.AZURE_STORAGE_2)
        azure_copy = self.hiarc_files.copy_file(cfcr, source.key)
        self.assertNotEqual(source.key, azure_copy.key)

        cfcr = self.hiarc_util.create_file_copy(
            storage=self.hiarc_util.AWS_EAST_STORAGE)
        aws_copy = self.hiarc_files.copy_file(cfcr, source.key)
        self.assertNotEqual(source.key, aws_copy.key)

        cfcr = self.hiarc_util.create_file_copy(
            storage=self.hiarc_util.GOOGLE_EAST_STORAGE)
        google_copy = self.hiarc_files.copy_file(cfcr, source.key)
        self.assertNotEqual(source.key, google_copy.key)

        for f in [source.key, copy.key, aws_copy.key, azure_copy.key, google_copy.key]:
            self.hiarc_files.delete_file(f)
            self.assertRaises(hiarc.rest.ApiException,
                              self.hiarc_files.get_file, f)

    def test_copy_file_google(self):
        """Test case for copying a file to other storage services from Google

        Google File Copy  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        cfr = self.hiarc_util.create_file(
            storage=self.hiarc_util.GOOGLE_EAST_STORAGE)
        source = self.hiarc_files.create_file(cfr, filepath)

        cfcr = self.hiarc_util.create_file_copy(
            storage=self.hiarc_util.GOOGLE_EAST_STORAGE)
        copy = self.hiarc_files.copy_file(cfcr, source.key)
        self.assertNotEqual(source.key, copy.key)

        cfcr = self.hiarc_util.create_file_copy(
            storage=self.hiarc_util.GOOGLE_WEST_STORAGE)
        google_copy = self.hiarc_files.copy_file(cfcr, source.key)
        self.assertNotEqual(source.key, google_copy.key)

        cfcr = self.hiarc_util.create_file_copy(
            storage=self.hiarc_util.AZURE_STORAGE_1)
        azure_copy = self.hiarc_files.copy_file(cfcr, source.key)
        self.assertNotEqual(source.key, azure_copy.key)

        cfcr = self.hiarc_util.create_file_copy(
            storage=self.hiarc_util.AWS_EAST_STORAGE)
        aws_copy = self.hiarc_files.copy_file(cfcr, source.key)
        self.assertNotEqual(source.key, aws_copy.key)

        for f in [source.key, copy.key, aws_copy.key, azure_copy.key, google_copy.key]:
            self.hiarc_files.delete_file(f)
            self.assertRaises(hiarc.rest.ApiException,
                              self.hiarc_files.get_file, f)

    def test_complex_delete(self):
        """Test case for deleting file in complex situations

        File Complex Delete  # noqa: E501
        """
        cfr = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f = self.hiarc_files.create_file(cfr, filepath)

        new_version_filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'NewVersionOfTest.txt')
        nvr = hiarc.AddVersionToFileRequest(key=f.key)
        self.hiarc_files.add_version(nvr, new_version_filepath, f.key)

        nvr = hiarc.AddVersionToFileRequest(key=f.key)
        self.hiarc_files.add_version(nvr, new_version_filepath, f.key)

        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        aftc = hiarc.AddFileToCollectionRequest(f.key)
        self.hiarc_collections.add_file_to_collection(aftc, c1.key)

        self.hiarc_files.delete_file(f.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f.key)

    def test_get_collections_for_file(self):
        """Test case for getting collections for a file

        Collections for File  # noqa: E501
        """
        cfr1 = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(cfr1, filepath)

        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        aftc = hiarc.AddFileToCollectionRequest(f1.key)
        self.hiarc_collections.add_file_to_collection(aftc, c1.key)

        c2 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        aftc = hiarc.AddFileToCollectionRequest(f1.key)
        self.hiarc_collections.add_file_to_collection(aftc, c1.key)

        c3 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        aftc = hiarc.AddFileToCollectionRequest(f1.key)
        self.hiarc_collections.add_file_to_collection(aftc, c1.key)

        collections = self.hiarc_files.get_collections_for_file(f1.key)
        assert len(collections) == 3

        self.hiarc_files.delete_file(f1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f1.key)

    def test_child_collection_access_by_user(self):
        """Test case for accessing a file in child collection inheritance by user

        User File Access in Child Collection  # noqa: E501
        """
        cfr1 = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(cfr1, filepath)

        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())

        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c2 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c3 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.hiarc_collections.add_child_to_collection(c1.key, c2.key)
        self.hiarc_collections.add_child_to_collection(c2.key, c3.key)
        # c1 -> c2 -> c3

        autc = hiarc.AddUserToCollectionRequest(
            u1.key, hiarc.AccessLevel.READ_ONLY)
        self.hiarc_collections.add_user_to_collection(
            autc, c1.key)  # add user to parent collection

        aftc = hiarc.AddFileToCollectionRequest(f1.key)
        # add file to nested child collection with parent of c1
        self.hiarc_collections.add_file_to_collection(aftc, c3.key)

        fetched = self.hiarc_files.get_file(f1.key, x_hiarc_user_key=u1.key)
        assert fetched == f1

        self.hiarc_files.delete_file(f1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f1.key)

    def test_parent_collection_access_by_user(self):
        """Test case for accessing a file in parent collection inheritance by user

        User File Access in Parent Collection  # noqa: E501
        """
        cfr1 = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(cfr1, filepath)

        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())

        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c2 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c3 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.hiarc_collections.add_child_to_collection(c1.key, c2.key)
        self.hiarc_collections.add_child_to_collection(c2.key, c3.key)
        # c1 -> c2 -> c3

        autc = hiarc.AddUserToCollectionRequest(
            u1.key, hiarc.AccessLevel.READ_ONLY)
        self.hiarc_collections.add_user_to_collection(
            autc, c1.key)  # add user to parent collection

        aftc = hiarc.AddFileToCollectionRequest(f1.key)
        self.hiarc_collections.add_file_to_collection(
            aftc, c1.key)  # add file to parent collection

        fetched = self.hiarc_files.get_file(f1.key, x_hiarc_user_key=u1.key)
        assert fetched == f1

        self.hiarc_files.delete_file(f1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f1.key)

    def test_child_collection_access_by_group(self):
        """Test case for accessing a file in child collection inheritance by group

        Group File Access in Child Collection  # noqa: E501
        """
        cfr1 = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(cfr1, filepath)

        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        g1 = self.hiarc_groups.create_group(self.hiarc_util.create_group())
        self.hiarc_groups.add_user_to_group(g1.key, u1.key)

        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c2 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c3 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.hiarc_collections.add_child_to_collection(c1.key, c2.key)
        self.hiarc_collections.add_child_to_collection(c2.key, c3.key)
        # c1 -> c2 -> c3

        agtc = hiarc.AddGroupToCollectionRequest(
            g1.key, hiarc.AccessLevel.READ_ONLY)
        self.hiarc_collections.add_group_to_collection(
            agtc, c1.key)  # add group to parent collection

        aftc = hiarc.AddFileToCollectionRequest(f1.key)
        # nested child collection with parent of c1
        self.hiarc_collections.add_file_to_collection(aftc, c3.key)

        fetched = self.hiarc_files.get_file(f1.key, x_hiarc_user_key=u1.key)
        assert fetched == f1

        self.hiarc_files.delete_file(f1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f1.key)

    def test_parent_collection_access_by_group(self):
        """Test case for accessing a file in parent collection inheritance by group

        Group File Access in Parent Collection  # noqa: E501
        """
        cfr1 = self.hiarc_util.create_file()
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(cfr1, filepath)

        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        g1 = self.hiarc_groups.create_group(self.hiarc_util.create_group())
        self.hiarc_groups.add_user_to_group(g1.key, u1.key)

        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c2 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c3 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.hiarc_collections.add_child_to_collection(c1.key, c2.key)
        self.hiarc_collections.add_child_to_collection(c2.key, c3.key)
        # c1 -> c2 -> c3

        agtc = hiarc.AddGroupToCollectionRequest(
            g1.key, hiarc.AccessLevel.READ_ONLY)
        self.hiarc_collections.add_group_to_collection(
            agtc, c1.key)  # add group to parent collection

        aftc = hiarc.AddFileToCollectionRequest(f1.key)
        self.hiarc_collections.add_file_to_collection(
            aftc, c1.key)  # add file to parent collection

        fetched = self.hiarc_files.get_file(f1.key, x_hiarc_user_key=u1.key)
        assert fetched == f1

        self.hiarc_files.delete_file(f1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f1.key)

    def test_create_file_with_metadata(self):
        """Test case for create_file_with_metadata

        Get a User  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(
                metadata=self.hiarc_util.get_test_metadata()),
            filepath=filepath)
        gf1 = self.hiarc_files.get_file(f1.key)

        assert self.hiarc_util.compare_entity_to_entity(f1, gf1)
        gf1.metadata['startDate'] = dateutil.parser.parse(
            gf1.metadata['startDate'])
        self.assertDictEqual(self.hiarc_util.get_test_metadata(), gf1.metadata)

        self.hiarc_files.delete_file(f1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f1.key)

    def test_update_file_with_metadata(self):
        """Test case for update_file_with_metadata

        Update File's Metadata  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(
                metadata=self.hiarc_util.get_test_metadata()),
            filepath=filepath)

        upmd = {
            "department": "support",
            "quotaCarrying": False,
            "targetRate": 7.271,
            "level": 2,
            "startDate": dateutil.parser.parse("2020-02-25T22:33:50.134Z")
        }

        uf = hiarc.UpdateFileRequest(metadata=upmd)
        updated = self.hiarc_files.update_file(uf, f1.key)
        updated.metadata['startDate'] = dateutil.parser.parse(
            updated.metadata['startDate'])
        self.assertDictEqual(upmd, updated.metadata)

        self.hiarc_files.delete_file(f1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f1.key)

    def test_nullout_file_with_metadata(self):
        """Test case for nullout_file_with_metadata

        Null File's Metadata  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(
                metadata=self.hiarc_util.get_test_metadata()),
            filepath=filepath)

        upmd = {
            "department": None,
            "quotaCarrying": None
        }

        uf = hiarc.UpdateFileRequest(metadata=upmd)
        updated = self.hiarc_files.update_file(uf, f1.key)
        assert len(updated.metadata.keys()) == 3

        next_upmd = {
            "targetRate": None,
            "level": None,
            "startDate": None
        }
        uf = hiarc.UpdateFileRequest(metadata=next_upmd)
        updated = self.hiarc_files.update_file(uf, f1.key)
        self.assertIsNone(updated.metadata)

        self.hiarc_files.delete_file(f1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f1.key)


if __name__ == '__main__':
    unittest.main()
