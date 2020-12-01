from __future__ import absolute_import
from integration_tests.hiarc_util import hiarc_util

import unittest
import dateutil.parser

import hiarc
from hiarc.api.user_api import UserApi  # noqa: E501
from hiarc.rest import ApiException


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self):
        self.hiarc_util = hiarc_util()
        self.hiarc_config = self.hiarc_util.init_hiarc_config_admin()
        self.hiarc_client = hiarc.ApiClient(self.hiarc_config)
        self.hiarc_groups = hiarc.GroupApi(self.hiarc_client)
        hiarc.AdminApi(self.hiarc_client).reset_db()

    def tearDown(self):
        pass

    def test_crud(self):
        """Test case for group CRUD actions

        Group CRUD  # noqa: E501
        """
        g = self.hiarc_groups.create_group(self.hiarc_util.create_group())
        fg = self.hiarc_groups.get_group(g.key)
        assert g == fg

        new_name = "New Name"
        new_description = "New description"
        ug = hiarc.UpdateGroupRequest(
            name=new_name, description=new_description)
        updated = self.hiarc_groups.update_group(ug, g.key)
        assert new_name == updated.name
        assert new_description == updated.description
        assert updated.modified_at > updated.created_at

        ug = hiarc.UpdateGroupRequest(key='new key')
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_groups.update_group, ug, g.key)

        self.hiarc_groups.delete_group(g.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_groups.get_group, g.key)

    def test_get_all_groups(self):
        """Test case for get_all_groups

        Get all Groups  # noqa: E501
        """
        for i in range(self.hiarc_util.LARGE_ENTITY_COUNT):
            self.hiarc_groups.create_group(self.hiarc_util.create_group())
        all_groups = self.hiarc_groups.get_all_groups()
        assert self.hiarc_util.LARGE_ENTITY_COUNT == len(all_groups)

    def test_create_group_with_metadata(self):
        """Test case for create_group_with_metadata

        Create a Group with Metadata  # noqa: E501
        """
        g1 = self.hiarc_groups.create_group(
            self.hiarc_util.create_group(self.hiarc_util.get_test_metadata()))
        gg = self.hiarc_groups.get_group(g1.key)

        assert self.hiarc_util.compare_entity_to_entity(g1, gg)
        gg.metadata['startDate'] = dateutil.parser.parse(
            gg.metadata['startDate'])
        self.assertDictEqual(self.hiarc_util.get_test_metadata(), gg.metadata)

    def test_update_group_metadata(self):
        """Test case for update_group_metadata

        Update a Group's Metadata  # noqa: E501
        """
        g1 = self.hiarc_groups.create_group(
            self.hiarc_util.create_group(self.hiarc_util.get_test_metadata()))
        upmd = {
            "department": "support",
            "quotaCarrying": False,
            "targetRate": 7.271,
            "level": 2,
            "startDate": dateutil.parser.parse("2020-02-25T22:33:50.134Z")
        }
        ug = hiarc.UpdateGroupRequest(metadata=upmd)
        updated = self.hiarc_groups.update_group(ug, g1.key)
        updated.metadata['startDate'] = dateutil.parser.parse(
            updated.metadata['startDate'])
        self.assertDictEqual(upmd, updated.metadata)

    def test_null_out_metadata(self):
        """Test case for null_out_metadata

        Null out metadata on a Group  # noqa: E501
        """
        g1 = self.hiarc_groups.create_group(
            self.hiarc_util.create_group(self.hiarc_util.get_test_metadata()))
        upmd = {
            "department": None,
            "quotaCarrying": None
        }
        ug = hiarc.UpdateGroupRequest(metadata=upmd)
        updated = self.hiarc_groups.update_group(ug, g1.key)
        updated.metadata['startDate'] = dateutil.parser.parse(
            updated.metadata['startDate'])
        assert len(updated.metadata.keys()) == 3

        upmd = {
            "targetRate": None,
            "level": None,
            "startDate": None
        }
        ug = hiarc.UpdateGroupRequest(metadata=upmd)
        updated = self.hiarc_groups.update_group(ug, g1.key)
        self.assertIsNone(updated.metadata)

    def test_find_groups(self):
        """Test case for find_groups

        Find a Group  # noqa: E501
        """
        md = self.hiarc_util.get_test_metadata()
        g1 = self.hiarc_groups.create_group(
            self.hiarc_util.create_group(md))

        md["quotaCarrying"] = False
        self.hiarc_groups.create_group(
            self.hiarc_util.create_group(md))
        self.hiarc_groups.create_group(
            self.hiarc_util.create_group())

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

        qr = hiarc.FindGroupsRequest(query=q)
        fg = self.hiarc_groups.find_group(qr)
        assert len(fg) == 1
        assert self.hiarc_util.compare_dict_to_entity(fg[0], g1)

if __name__ == '__main__':
    unittest.main()
