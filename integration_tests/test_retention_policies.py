from __future__ import absolute_import
from integration_tests.hiarc_util import hiarc_util

import unittest
import dateutil.parser
import os
import time

import hiarc
from hiarc.api.user_api import UserApi  # noqa: E501
from hiarc.rest import ApiException


class TestRetentionPolicyApi(unittest.TestCase):
    """RetentionPolicyApi unit test stubs"""

    def setUp(self):
        self.hiarc_util = hiarc_util()
        self.hiarc_config = self.hiarc_util.init_hiarc_config_admin()
        self.hiarc_files = hiarc.FileApi(hiarc.ApiClient(self.hiarc_config))
        self.hiarc_retention_policies = hiarc.RetentionPolicyApi(
            hiarc.ApiClient(self.hiarc_config))
        hiarc.AdminApi(hiarc.ApiClient(self.hiarc_config)).reset_db()

    def tearDown(self):
        pass

    def test_crud(self):
        """Test case for retention policies CRUD actions

        Retention Policy CRUD  # noqa: E501
        """
        rp = self.hiarc_retention_policies.create_retention_policy(
            self.hiarc_util.create_retention_policy(seconds=60))
        frp = self.hiarc_retention_policies.get_retention_policy(rp.key)
        assert rp == frp
        assert 60 == frp.seconds

        new_name = "New Name"
        new_description = "New description"
        urp = hiarc.UpdateRetentionPolicyRequest(
            name=new_name, description=new_description)
        updated = self.hiarc_retention_policies.update_retention_policy(
            urp, rp.key)
        assert new_name == updated.name
        assert new_description == updated.description
        assert updated.modified_at > updated.created_at

        urp = hiarc.UpdateRetentionPolicyRequest(key='new key')
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_retention_policies.update_retention_policy, urp, rp.key)

    def test_apply_multi_to_file(self):
        """Test case for apply_multi_to_file

        Apply Two Policies to File  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)

        rp1 = self.hiarc_retention_policies.create_retention_policy(
            self.hiarc_util.create_retention_policy(seconds=1))
        arpfr = hiarc.AddRetentionPolicyToFileRequest(rp1.key)
        self.hiarc_files.add_retention_policy_to_file(arpfr, f1.key)

        rp2 = self.hiarc_retention_policies.create_retention_policy(
            self.hiarc_util.create_retention_policy(seconds=3))
        arpfr = hiarc.AddRetentionPolicyToFileRequest(rp2.key)
        self.hiarc_files.add_retention_policy_to_file(arpfr, f1.key)
        time.sleep(2)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.delete_file, f1.key)

        policies = self.hiarc_files.get_retention_policies(f1.key)
        assert policies[0]['appliedAt'] < policies[1]['appliedAt']
        assert policies[0]['retentionPolicy']['key'] == rp1.key
        assert policies[0]['retentionPolicy']['seconds'] == 1
        assert policies[1]['retentionPolicy']['key'] == rp2.key
        assert policies[1]['retentionPolicy']['seconds'] == 3

        time.sleep(2)
        self.hiarc_files.delete_file(f1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f1.key)

    def test_delete_file_single_policy(self):
        """Test case for delete_file_single_policy

        Apply Single Policy to File  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)

        rp1 = self.hiarc_retention_policies.create_retention_policy(
            self.hiarc_util.create_retention_policy(seconds=2))
        arpfr = hiarc.AddRetentionPolicyToFileRequest(rp1.key)
        self.hiarc_files.add_retention_policy_to_file(arpfr, f1.key)

        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.delete_file, f1.key)

        time.sleep(3)
        self.hiarc_files.delete_file(f1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f1.key)

    def test_update_retention_period(self):
        """Test case for update_retention_period

        Update Retention Policy Period  # noqa: E501
        """
        rp = self.hiarc_retention_policies.create_retention_policy(
            self.hiarc_util.create_retention_policy(seconds=self.hiarc_util.RETENTION_PERIOD_MONTH))

        urp = hiarc.UpdateRetentionPolicyRequest(
            seconds=self.hiarc_util.RETENTION_PERIOD_DAY)
        self.assertRaises(hiarc.rest.ApiException, self.hiarc_retention_policies.update_retention_policy,
                          urp, rp.key)

        urp = hiarc.UpdateRetentionPolicyRequest(
            seconds=self.hiarc_util.RETENTION_PERIOD_MAX)
        updated = self.hiarc_retention_policies.update_retention_policy(
            urp, rp.key)
        assert updated.seconds == self.hiarc_util.RETENTION_PERIOD_MAX

    def test_delete_file_updated_policy(self):
        """Test case for delete_file_updated_policy

        Apply Updated Policy to File  # noqa: E501
        """
        filepath = os.path.join(
            os.getcwd(), self.hiarc_util.TEST_FILE_PATH, 'Test.txt')
        f1 = self.hiarc_files.create_file(
            self.hiarc_util.create_file(), filepath)

        rp1 = self.hiarc_retention_policies.create_retention_policy(
            self.hiarc_util.create_retention_policy(seconds=3))
        self.hiarc_files.add_retention_policy_to_file(
            hiarc.AddRetentionPolicyToFileRequest(rp1.key), f1.key)

        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.delete_file, f1.key)

        urp = hiarc.UpdateRetentionPolicyRequest(seconds=10)
        updated = self.hiarc_retention_policies.update_retention_policy(
            urp, rp1.key)
        time.sleep(5)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.delete_file, f1.key)

        time.sleep(7)
        self.hiarc_files.delete_file(f1.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_files.get_file, f1.key)

    def test_get_all_policies(self):
        """Test case for get_all_policies

        Get all Retention Policies  # noqa: E501
        """
        for i in range(self.hiarc_util.LARGE_ENTITY_COUNT):
            self.hiarc_retention_policies.create_retention_policy(
                self.hiarc_util.create_retention_policy(60))
        all_policies = self.hiarc_retention_policies.get_all_retention_policies()
        assert self.hiarc_util.LARGE_ENTITY_COUNT == len(all_policies)

    def test_create_policy_with_metadata(self):
        """Test case for create_policy_with_metadata

        Create a Retention Policy with Metadata  # noqa: E501
        """
        rp1 = self.hiarc_retention_policies.create_retention_policy(
            self.hiarc_util.create_retention_policy(60, metadata=self.hiarc_util.get_test_metadata()))
        grp = self.hiarc_retention_policies.get_retention_policy(rp1.key)

        assert self.hiarc_util.compare_entity_to_entity(rp1, grp)
        grp.metadata['startDate'] = dateutil.parser.parse(
            grp.metadata['startDate'])
        self.assertDictEqual(self.hiarc_util.get_test_metadata(), grp.metadata)

    def test_update_group_metadata(self):
        """Test case for update_group_metadata

        Update a Group's Metadata  # noqa: E501
        """
        rp1 = self.hiarc_retention_policies.create_retention_policy(
            self.hiarc_util.create_retention_policy(60, metadata=self.hiarc_util.get_test_metadata()))
        upmd = {
            "department": "support",
            "quotaCarrying": False,
            "targetRate": 7.271,
            "level": 2,
            "startDate": dateutil.parser.parse("2020-02-25T22:33:50.134Z")
        }
        urp = hiarc.UpdateRetentionPolicyRequest(metadata=upmd)
        updated = self.hiarc_retention_policies.update_retention_policy(
            urp, rp1.key)
        updated.metadata['startDate'] = dateutil.parser.parse(
            updated.metadata['startDate'])
        self.assertDictEqual(upmd, updated.metadata)

    def test_null_out_metadata(self):
        """Test case for null_out_metadata

        Null out metadata on a Group  # noqa: E501
        """
        rp1 = self.hiarc_retention_policies.create_retention_policy(
            self.hiarc_util.create_retention_policy(60, metadata=self.hiarc_util.get_test_metadata()))
        upmd = {
            "department": None,
            "quotaCarrying": None
        }
        urp = hiarc.UpdateRetentionPolicyRequest(metadata=upmd)
        updated = self.hiarc_retention_policies.update_retention_policy(
            urp, rp1.key)
        updated.metadata['startDate'] = dateutil.parser.parse(
            updated.metadata['startDate'])
        assert len(updated.metadata.keys()) == 3

        upmd = {
            "targetRate": None,
            "level": None,
            "startDate": None
        }
        urp = hiarc.UpdateRetentionPolicyRequest(metadata=upmd)
        updated = self.hiarc_retention_policies.update_retention_policy(
            urp, rp1.key)
        self.assertIsNone(updated.metadata)

    def test_find_policy(self):
        """Test case for find_policy

        Find a Retention Policy  # noqa: E501
        """
        md = self.hiarc_util.get_test_metadata()
        rp1 = self.hiarc_retention_policies.create_retention_policy(
            self.hiarc_util.create_retention_policy(60, metadata=md))

        md["quotaCarrying"] = False
        self.hiarc_retention_policies.create_retention_policy(
            self.hiarc_util.create_retention_policy(60, metadata=md))
        self.hiarc_retention_policies.create_retention_policy(
            self.hiarc_util.create_retention_policy(60))

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

        qr = hiarc.FindRetentionPoliciesRequest(query=q)
        frp = self.hiarc_retention_policies.find_retention_policies(qr)
        assert len(frp) == 1
        assert self.hiarc_util.compare_dict_to_entity(frp[0], rp1)


if __name__ == '__main__':
    unittest.main()
