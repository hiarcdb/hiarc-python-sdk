from __future__ import absolute_import
from integration_tests.hiarc_util import hiarc_util

import unittest
import dateutil.parser
import os

import hiarc
from hiarc.api.user_api import UserApi  # noqa: E501
from hiarc.rest import ApiException


class TestCollectionApi(unittest.TestCase):
    """CollectionApi unit test stubs"""

    def setUp(self):
        self.hiarc_util = hiarc_util()
        self.hiarc_config = self.hiarc_util.init_hiarc_config_admin()
        self.hiarc_users = hiarc.UserApi(hiarc.ApiClient(self.hiarc_config))
        self.hiarc_groups = hiarc.GroupApi(hiarc.ApiClient(self.hiarc_config))
        self.hiarc_collections = hiarc.CollectionApi(hiarc.ApiClient(self.hiarc_config))
        self.hiarc_token = hiarc.TokenApi(hiarc.ApiClient(self.hiarc_config))
        self.hiarc_files = hiarc.FileApi(hiarc.ApiClient(self.hiarc_config))
        hiarc.AdminApi(hiarc.ApiClient(self.hiarc_config)).reset_db()

    def tearDown(self):
        pass

    def test_crud(self):
        """Test case for collection CRUD actions

        Collection CRUD  # noqa: E501
        """
        c1 = self.hiarc_util.create_collection()
        c = self.hiarc_collections.create_collection(c1)
        gc = self.hiarc_collections.get_collection(c1.key)
        assert c == gc

        new_name = "New Name"
        new_description = "New description"
        ucr = hiarc.UpdateCollectionRequest(
            name=new_name, description=new_description)
        uc = self.hiarc_collections.update_collection(ucr, c.key)
        assert new_name == uc.name
        assert new_description == uc.description
        assert uc.modified_at > uc.created_at

        uc = hiarc.UpdateCollectionRequest(key='new key')
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.update_collection, uc, c.key)

        self.hiarc_collections.delete_collection(c.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.get_collection, c.key)

    def test_create_access_and_update_collection_asuser(self):
        """Test case for creating access to and updating a collection as user

        Collection access and update as user  # noqa: E501
        """
        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        c1 = self.hiarc_util.create_collection()
        c = self.hiarc_collections.create_collection(
            c1, x_hiarc_user_key=u1.key)
        gc = self.hiarc_collections.get_collection(
            c1.key, x_hiarc_user_key=u1.key)
        assert c == gc

        u2 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        autc = hiarc.AddUserToCollectionRequest(
            u2.key, hiarc.AccessLevel.READ_ONLY)
        self.hiarc_collections.add_user_to_collection(autc, c1.key)
        fc = self.hiarc_collections.get_collection(
            c1.key, x_hiarc_user_key=u2.key)
        assert c == fc

        u3 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.get_collection, c1.key, x_hiarc_user_key=u3.key)

        ac = self.hiarc_collections.get_collection(c1.key)
        assert c == ac

        new_name = "New Name"
        new_description = "New description"
        ucr = hiarc.UpdateCollectionRequest(
            name=new_name, description=new_description)
        uc = self.hiarc_collections.update_collection(
            ucr, c.key, x_hiarc_user_key=u1.key)
        assert new_name == uc.name
        assert new_description == uc.description
        assert uc.modified_at > uc.created_at

        new_name = "New Name 2"
        new_description = "New description 2"
        ucr = hiarc.UpdateCollectionRequest(
            name=new_name, description=new_description)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.update_collection, ucr, c1.key, x_hiarc_user_key=u2.key)

        autc = hiarc.AddUserToCollectionRequest(
            u3.key, hiarc.AccessLevel.READ_WRITE)
        self.hiarc_collections.add_user_to_collection(autc, c1.key)
        new_name = "New Name 3"
        new_description = "New description 3"
        ucr = hiarc.UpdateCollectionRequest(
            name=new_name, description=new_description)
        uc = self.hiarc_collections.update_collection(
            ucr, c.key, x_hiarc_user_key=u3.key)
        assert new_name == uc.name
        assert new_description == uc.description
        assert uc.modified_at > uc.created_at

        u4 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.update_collection, ucr, c1.key, x_hiarc_user_key=u4.key)

        new_name = "New Name 4"
        new_description = "New description 4"
        ucr = hiarc.UpdateCollectionRequest(
            name=new_name, description=new_description)
        uc = self.hiarc_collections.update_collection(ucr, c.key)
        assert new_name == uc.name
        assert new_description == uc.description
        assert uc.modified_at > uc.created_at

    def test_hierarchies(self):
        """Test case for collection hierarchies

        Collection hierarchies  # noqa: E501
        """
        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c2 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c3 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c4 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c5 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c6 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.hiarc_collections.add_child_to_collection(c1.key, c2.key)
        self.hiarc_collections.add_child_to_collection(c2.key, c3.key)
        self.hiarc_collections.add_child_to_collection(c3.key, c4.key)
        self.hiarc_collections.add_child_to_collection(c4.key, c5.key)
        self.hiarc_collections.add_child_to_collection(c6.key, c4.key)

        autc = hiarc.AddUserToCollectionRequest(
            u1.key, hiarc.AccessLevel.READ_ONLY)
        self.hiarc_collections.add_user_to_collection(autc, c2.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.get_collection, c1.key, x_hiarc_user_key=u1.key)

        fc = self.hiarc_collections.get_collection(
            c2.key, x_hiarc_user_key=u1.key)
        assert c2 == fc

        fc = self.hiarc_collections.get_collection(
            c3.key, x_hiarc_user_key=u1.key)
        assert c3 == fc

        fc = self.hiarc_collections.get_collection(
            c4.key, x_hiarc_user_key=u1.key)
        assert c4 == fc

        fc = self.hiarc_collections.get_collection(
            c5.key, x_hiarc_user_key=u1.key)
        assert c5 == fc

        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.get_collection, c6.key, x_hiarc_user_key=u1.key)

    def test_prevent_cycle(self):
        """Test case for preventing cyclical collection hierarchies

        Prevent Cyclical Collection  # noqa: E501
        """
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c2 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c3 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c4 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c5 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c6 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c7 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.hiarc_collections.add_child_to_collection(c1.key, c2.key)
        self.hiarc_collections.add_child_to_collection(c2.key, c3.key)
        self.hiarc_collections.add_child_to_collection(c3.key, c4.key)
        self.hiarc_collections.add_child_to_collection(c4.key, c5.key)
        self.hiarc_collections.add_child_to_collection(c6.key, c4.key)
        self.hiarc_collections.add_child_to_collection(c6.key, c7.key)

        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.add_child_to_collection, c5.key, c1.key)

    def test_get_children(self):
        """Test case for getting children of collections

        Children of Collection  # noqa: E501
        """
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c2 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c3 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c4 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c5 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c6 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.hiarc_collections.add_child_to_collection(c1.key, c2.key)
        self.hiarc_collections.add_child_to_collection(c1.key, c3.key)
        self.hiarc_collections.add_child_to_collection(c1.key, c4.key)
        self.hiarc_collections.add_child_to_collection(c2.key, c5.key)
        self.hiarc_collections.add_child_to_collection(c4.key, c6.key)

        children = self.hiarc_collections.get_collection_children(c1.key)
        assert len(children) == 3
        assert next((c for c in children if self.hiarc_util.compare_dict_to_entity(
            c, c2)), None) is not None
        assert next((c for c in children if self.hiarc_util.compare_dict_to_entity(
            c, c3)), None) is not None
        assert next((c for c in children if self.hiarc_util.compare_dict_to_entity(
            c, c4)), None) is not None
        assert next((c for c in children if self.hiarc_util.compare_dict_to_entity(
            c, c5)), None) is None
        assert next((c for c in children if self.hiarc_util.compare_dict_to_entity(
            c, c6)), None) is None

    def test_get_items(self):
        """Test case for getting items of collections

        Items of Collection  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c2 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c3 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c4 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c5 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c6 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.hiarc_collections.add_child_to_collection(c1.key, c2.key)
        self.hiarc_collections.add_child_to_collection(c1.key, c3.key)
        self.hiarc_collections.add_child_to_collection(c1.key, c4.key)
        self.hiarc_collections.add_child_to_collection(c2.key, c5.key)
        self.hiarc_collections.add_child_to_collection(c4.key, c6.key)

        f1 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)
        f2 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)
        f3 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)
        f4 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)
        f5 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)

        self.hiarc_collections.add_file_to_collection(
            hiarc.AddFileToCollectionRequest(f1.key), c1.key)
        self.hiarc_collections.add_file_to_collection(
            hiarc.AddFileToCollectionRequest(f2.key), c1.key)
        self.hiarc_collections.add_file_to_collection(
            hiarc.AddFileToCollectionRequest(f3.key), c1.key)
        self.hiarc_collections.add_file_to_collection(
            hiarc.AddFileToCollectionRequest(f4.key), c2.key)
        self.hiarc_collections.add_file_to_collection(
            hiarc.AddFileToCollectionRequest(f5.key), c3.key)

        items = self.hiarc_collections.get_collection_items(c1.key)
        children = items.child_collections
        assert len(children) == 3
        assert next((c for c in children if self.hiarc_util.compare_entity_to_entity(
            c, c2)), None) is not None
        assert next((c for c in children if self.hiarc_util.compare_entity_to_entity(
            c, c3)), None) is not None
        assert next((c for c in children if self.hiarc_util.compare_entity_to_entity(
            c, c4)), None) is not None
        assert next((c for c in children if self.hiarc_util.compare_entity_to_entity(
            c, c5)), None) is None
        assert next((c for c in children if self.hiarc_util.compare_entity_to_entity(
            c, c6)), None) is None

        files = items.files
        assert len(files) == 3
        assert next((f for f in files if self.hiarc_util.compare_entity_to_entity(
            f, f1)), None) is not None
        assert next((f for f in files if self.hiarc_util.compare_entity_to_entity(
            f, f2)), None) is not None
        assert next((f for f in files if self.hiarc_util.compare_entity_to_entity(
            f, f3)), None) is not None
        assert next((f for f in files if self.hiarc_util.compare_entity_to_entity(
            f, f4)), None) is None
        assert next((f for f in files if self.hiarc_util.compare_entity_to_entity(
            f, f5)), None) is None

        for f in [f1.key, f2.key, f3.key, f4.key, f5.key]:
            self.hiarc_files.delete_file(f)
            self.assertRaises(hiarc.rest.ApiException,
                              self.hiarc_files.get_file, f)

    def test_add_child_collection_as_user(self):
        """Test case for adding children to collections as a user

        Add Children of Collection as User  # noqa: E501
        """
        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())
        c2 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.add_child_to_collection, c1.key, c2.key, x_hiarc_user_key=u1.key)

        autc = hiarc.AddUserToCollectionRequest(
            u1.key, hiarc.AccessLevel.READ_ONLY)
        self.hiarc_collections.add_user_to_collection(autc, c1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.add_child_to_collection, c1.key, c2.key, x_hiarc_user_key=u1.key)

        u2 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        autc = hiarc.AddUserToCollectionRequest(
            u2.key, hiarc.AccessLevel.READ_WRITE)
        self.hiarc_collections.add_user_to_collection(autc, c1.key)

        self.hiarc_collections.add_child_to_collection(
            c1.key, c2.key, x_hiarc_user_key=u2.key)

    def test_delete_with_file(self):
        """Test case for deleting collections with files

        Delete Collection with File  # noqa: E501
        """
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)

        self.hiarc_collections.add_file_to_collection(
            hiarc.AddFileToCollectionRequest(f1.key), c1.key)

        self.hiarc_collections.delete_collection(c1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.get_collection, c1.key)

        r = self.hiarc_files.get_file(f1.key)
        assert f1 == r

        self.hiarc_files.delete_file(f1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f1.key)

    def test_delete_as_user(self):
        """Test case for deleting collections as user

        Delete Collection as User  # noqa: E501
        """
        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.delete_collection, c1.key, x_hiarc_user_key=u1.key)

        self.hiarc_collections.add_user_to_collection(
            hiarc.AddUserToCollectionRequest(u1.key, hiarc.AccessLevel.READ_ONLY), c1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.delete_collection, c1.key, x_hiarc_user_key=u1.key)

        u2 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        self.hiarc_collections.add_user_to_collection(
            hiarc.AddUserToCollectionRequest(u2.key, hiarc.AccessLevel.READ_WRITE), c1.key)
        self.hiarc_collections.delete_collection(
            c1.key, x_hiarc_user_key=u2.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.get_collection, c1.key)

    def test_add_remove_files(self):
        """Test case for adding and removing files from collections

        Add/Remove File from Collection # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)
        f2 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)
        f3 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)

        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.hiarc_collections.add_file_to_collection(
            hiarc.AddFileToCollectionRequest(f1.key), c1.key)
        self.hiarc_collections.add_file_to_collection(
            hiarc.AddFileToCollectionRequest(f2.key), c1.key)
        self.hiarc_collections.add_file_to_collection(
            hiarc.AddFileToCollectionRequest(f3.key), c1.key)

        files = self.hiarc_collections.get_collection_files(c1.key)
        assert len(files) == 3

        self.hiarc_collections.remove_file_from_collection(c1.key, f3.key)
        files = self.hiarc_collections.get_collection_files(c1.key)
        assert len(files) == 2

        for f in [f1.key, f2.key, f3.key]:
            self.hiarc_files.delete_file(f)
            self.assertRaises(hiarc.rest.ApiException,
                              self.hiarc_files.get_file, f)

    def test_add_remove_files_as_user(self):
        """Test case for adding and removing files from collections as user

        Add/Remove File from Collection as User # noqa: E501
        """
        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())

        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)

        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        aftcr = hiarc.AddFileToCollectionRequest(f1.key)
        self.assertRaises(hiarc.rest.ApiException, self.hiarc_collections.add_file_to_collection,
                          aftcr, c1.key, x_hiarc_user_key=u1.key)

        self.hiarc_collections.add_user_to_collection(
            hiarc.AddUserToCollectionRequest(u1.key, hiarc.AccessLevel.READ_ONLY), c1.key)
        self.assertRaises(hiarc.rest.ApiException, self.hiarc_collections.add_file_to_collection,
                          aftcr, c1.key, x_hiarc_user_key=u1.key)

        u2 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        self.hiarc_collections.add_user_to_collection(
            hiarc.AddUserToCollectionRequest(u2.key, hiarc.AccessLevel.READ_WRITE), c1.key)
        self.hiarc_collections.add_file_to_collection(
            aftcr, c1.key, x_hiarc_user_key=u2.key)

        files = self.hiarc_collections.get_collection_files(c1.key)
        assert len(files) == 1

        u3 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        self.assertRaises(hiarc.rest.ApiException, self.hiarc_collections.remove_file_from_collection,
                          c1.key, f1.key, x_hiarc_user_key=u3.key)
        self.assertRaises(hiarc.rest.ApiException, self.hiarc_collections.remove_file_from_collection,
                          c1.key, f1.key, x_hiarc_user_key=u1.key)
        self.hiarc_collections.remove_file_from_collection(
            c1.key, f1.key, x_hiarc_user_key=u2.key)

        files = self.hiarc_collections.get_collection_files(c1.key)
        assert len(files) == 0

        self.hiarc_files.delete_file(f1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f1.key)

    def test_get_files_for_user(self):
        """Test case for getting files of collections for a user

        Files of Collection for User  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')

        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        f1 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)
        f2 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)
        f3 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)

        self.hiarc_collections.add_file_to_collection(
            hiarc.AddFileToCollectionRequest(f1.key), c1.key)
        self.hiarc_collections.add_file_to_collection(
            hiarc.AddFileToCollectionRequest(f2.key), c1.key)
        self.hiarc_collections.add_file_to_collection(
            hiarc.AddFileToCollectionRequest(f3.key), c1.key)

        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.get_collection_files, c1.key, x_hiarc_user_key=u1.key)

        self.hiarc_collections.add_user_to_collection(
            hiarc.AddUserToCollectionRequest(u1.key, hiarc.AccessLevel.READ_ONLY), c1.key)

        files = self.hiarc_collections.get_collection_files(
            c1.key, x_hiarc_user_key=u1.key)
        assert len(files) == 3

        ut = self.hiarc_token.create_user_token(
            hiarc.CreateUserTokenRequest(key=u1.key))
        lc = hiarc.CollectionApi(hiarc.ApiClient(
            configuration=self.hiarc_util.init_hiarc_client_jwt_token(ut.bearer_token)))
        files = lc.get_collection_files(c1.key)
        assert len(files) == 3

        # reset ApiClient to Admin User
        hiarc.ApiClient(
            configuration=self.hiarc_util.init_hiarc_config_admin())

        for f in [f1.key, f2.key, f3.key]:
            self.hiarc_files.delete_file(f)
            self.assertRaises(hiarc.rest.ApiException,
                              self.hiarc_files.get_file, f)

    def test_add_user_as_user(self):
        """Test case for adding users to collections as user

        Add Users to Collection as User  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')

        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        u2 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.add_user_to_collection,
                          hiarc.AddUserToCollectionRequest(u2.key, hiarc.AccessLevel.READ_ONLY), c1.key, x_hiarc_user_key=u1.key)

        self.hiarc_collections.add_user_to_collection(
            hiarc.AddUserToCollectionRequest(u1.key, hiarc.AccessLevel.READ_ONLY), c1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.add_user_to_collection,
                          hiarc.AddUserToCollectionRequest(u2.key, hiarc.AccessLevel.READ_ONLY), c1.key, x_hiarc_user_key=u1.key)

        u3 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        self.hiarc_collections.add_user_to_collection(
            hiarc.AddUserToCollectionRequest(u3.key, hiarc.AccessLevel.READ_WRITE), c1.key)
        self.hiarc_collections.add_user_to_collection(
            hiarc.AddUserToCollectionRequest(u2.key, hiarc.AccessLevel.READ_ONLY), c1.key, x_hiarc_user_key=u3.key)

    def test_add_group_as_user(self):
        """Test case for adding groups to collections as user

        Add Group to Collection as User  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')

        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        g1 = self.hiarc_groups.create_group(self.hiarc_util.create_group())
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.add_group_to_collection,
                          hiarc.AddGroupToCollectionRequest(g1.key, hiarc.AccessLevel.READ_ONLY), c1.key, x_hiarc_user_key=u1.key)

        self.hiarc_collections.add_user_to_collection(
            hiarc.AddUserToCollectionRequest(u1.key, hiarc.AccessLevel.READ_ONLY), c1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.add_group_to_collection,
                          hiarc.AddGroupToCollectionRequest(g1.key, hiarc.AccessLevel.READ_ONLY), c1.key, x_hiarc_user_key=u1.key)

        u3 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        self.hiarc_collections.add_user_to_collection(
            hiarc.AddUserToCollectionRequest(u3.key, hiarc.AccessLevel.READ_WRITE), c1.key)
        self.hiarc_collections.add_group_to_collection(
            hiarc.AddGroupToCollectionRequest(g1.key, hiarc.AccessLevel.READ_ONLY), c1.key, x_hiarc_user_key=u3.key)

    def test_get_all_collections(self):
        """Test case for get_all_collections

        Get all Collections  # noqa: E501
        """
        for i in range(self.hiarc_util.LARGE_ENTITY_COUNT):
            self.hiarc_collections.create_collection(
                self.hiarc_util.create_collection())
        all_collections = self.hiarc_collections.get_all_collections()
        assert self.hiarc_util.LARGE_ENTITY_COUNT == len(all_collections)

        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_collections.get_all_collections, x_hiarc_user_key=u1.key)

        ut = self.hiarc_token.create_user_token(
            hiarc.CreateUserTokenRequest(key=u1.key))
        lc = hiarc.CollectionApi(hiarc.ApiClient(
            configuration=self.hiarc_util.init_hiarc_client_jwt_token(ut.bearer_token)))
        self.assertRaises(hiarc.rest.ApiException,
                          lc.get_all_collections)
        # reset ApiClient to Admin User
        # hiarc.ApiClient(
        #     configuration=self.hiarc_util.init_hiarc_config_admin())

    def test_create_collection_with_metadata(self):
        """Test case for create_collection_with_metadata

        Create a collection with metadata  # noqa: E501
        """
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection(self.hiarc_util.get_test_metadata()))
        gc = self.hiarc_collections.get_collection(c1.key)

        assert self.hiarc_util.compare_entity_to_entity(c1, gc)
        gc.metadata['startDate'] = dateutil.parser.parse(
            gc.metadata['startDate'])
        self.assertDictEqual(self.hiarc_util.get_test_metadata(), gc.metadata)

    def test_update_collection_metadata(self):
        """Test case for update_collection_metadata

        Update a Collection's metadata  # noqa: E501
        """
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection(self.hiarc_util.get_test_metadata()))
        upmd = {
            "department": "support",
            "quotaCarrying": False,
            "targetRate": 7.271,
            "level": 2,
            "startDate": dateutil.parser.parse("2020-02-25T22:33:50.134Z")
        }
        uc = hiarc.UpdateCollectionRequest(metadata=upmd)
        updated = self.hiarc_collections.update_collection(uc, c1.key)
        updated.metadata['startDate'] = dateutil.parser.parse(
            updated.metadata['startDate'])
        self.assertDictEqual(upmd, updated.metadata)

    def test_null_out_metadata(self):
        """Test case for null_out_metadata

        Null out metadata on a Collection  # noqa: E501
        """
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection(self.hiarc_util.get_test_metadata()))
        upmd = {
            "department": None,
            "quotaCarrying": None
        }
        uc = hiarc.UpdateCollectionRequest(metadata=upmd)
        updated = self.hiarc_collections.update_collection(uc, c1.key)
        updated.metadata['startDate'] = dateutil.parser.parse(
            updated.metadata['startDate'])
        assert len(updated.metadata.keys()) == 3

        upmd = {
            "targetRate": None,
            "level": None,
            "startDate": None
        }
        uc = hiarc.UpdateCollectionRequest(metadata=upmd)
        updated = self.hiarc_collections.update_collection(uc, c1.key)
        self.assertIsNone(updated.metadata)

    def test_find_collection(self):
        """Test case for find_collection

        Find a Collection  # noqa: E501
        """
        md = self.hiarc_util.get_test_metadata()
        c1 = self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection(metadata=md))
        md["quotaCarrying"] = False
        self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection(metadata=md))
        self.hiarc_collections.create_collection(
            self.hiarc_util.create_collection())

        q = [{
            "prop": "department",
            "op": "starts with",
            "value": "sal"
        },
            {
                "bool": "and"
        },
            {
                "parens": "("
        },
            {
                "prop": "targetRate",
                "op": ">=",
                "value": 4.22
        },
            {
                "bool": "and"
        },
            {
                "prop": "quotaCarrying",
                "op": "=",
                "value": True
        },
            {
                "parens": ")"
        }]

        qr = hiarc.FindCollectionsRequest(query=q)
        fc = self.hiarc_collections.find_collection(qr)
        assert len(fc) == 1
        assert self.hiarc_util.compare_dict_to_entity(fc[0], c1)


if __name__ == '__main__':
    unittest.main()
