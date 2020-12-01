from __future__ import absolute_import
from integration_tests.hiarc_util import hiarc_util

import unittest
import dateutil.parser

import hiarc
from hiarc.api.user_api import UserApi  # noqa: E501
from hiarc.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.hiarc_util = hiarc_util()
        self.hiarc_config = self.hiarc_util.init_hiarc_config_admin()
        self.hiarc_client = hiarc.ApiClient(self.hiarc_config)
        self.hiarc_users = hiarc.UserApi(self.hiarc_client)
        self.hiarc_groups = hiarc.GroupApi(self.hiarc_client)
        self.hiarc_token = hiarc.TokenApi(self.hiarc_client)
        hiarc.AdminApi(self.hiarc_client).reset_db()

    def tearDown(self):
        pass

    def test_crud(self):
        """Test case for user CRUD actions

        User CRUD  # noqa: E501
        """
        u1r = self.hiarc_util.create_user()
        u = self.hiarc_users.create_user(u1r)
        fu = self.hiarc_users.get_user(u1r.key)
        assert u == fu

        new_name = "New Name"
        new_description = "New description"
        uu = hiarc.UpdateUserRequest(
            name=new_name, description=new_description)
        updated_user = self.hiarc_users.update_user(uu, u.key)
        assert new_name == updated_user.name
        assert new_description == updated_user.description
        assert updated_user.modified_at > updated_user.created_at

        uu = hiarc.UpdateUserRequest(key='new key')
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_users.update_user, uu, u.key)

        self.hiarc_users.delete_user(u.key)
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_users.get_user, u.key)

    def test_get_all_users(self):
        """Test case for get_all_users

        Get all Users  # noqa: E501
        """
        for i in range(self.hiarc_util.LARGE_ENTITY_COUNT):
            self.hiarc_users.create_user(self.hiarc_util.create_user())
        all_users = self.hiarc_users.get_all_users()
        assert self.hiarc_util.LARGE_ENTITY_COUNT == len(all_users)

    def test_get_current_user(self):
        """Test case for get_current_user

        Get the current User  # noqa: E501
        """
        u = self.hiarc_users.create_user(self.hiarc_util.create_user())
        fetchu = self.hiarc_users.get_current_user(x_hiarc_user_key=u.key)
        assert u.key == fetchu.key

        ut = self.hiarc_token.create_user_token(
            hiarc.CreateUserTokenRequest(key=u.key))
        lc = hiarc.UserApi(hiarc.ApiClient(self.hiarc_util.init_hiarc_client_jwt_token(ut.bearer_token)))
        fetchu = lc.get_current_user()
        assert u.key == fetchu.key

        # reset ApiClient to Admin User
        # hiarc.ApiClient(
        #     configuration=self.hiarc_util.init_hiarc_config_admin())

    def test_get_groups_for_user(self):
        """Test case for get_groups_for_user

        Get Groups for a User  # noqa: E501
        """
        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        g1 = self.hiarc_groups.create_group(self.hiarc_util.create_group())
        g2 = self.hiarc_groups.create_group(self.hiarc_util.create_group())

        self.hiarc_groups.add_user_to_group(g1.key, u1.key)
        self.hiarc_groups.add_user_to_group(g2.key, u1.key)

        groups = self.hiarc_users.get_groups_for_user(u1.key)
        assert len(groups) == 2

        assert next((g for g in groups if self.hiarc_util.compare_dict_to_entity(
            g, g1)), None) is not None
        assert next((g for g in groups if self.hiarc_util.compare_dict_to_entity(
            g, g2)), None) is not None

    def test_get_groups_for_current_user(self):
        """Test case for get_groups_for_current_user

        Get the Groups for the current User  # noqa: E501
        """
        u1 = self.hiarc_users.create_user(self.hiarc_util.create_user())
        g1 = self.hiarc_groups.create_group(self.hiarc_util.create_group())
        g2 = self.hiarc_groups.create_group(self.hiarc_util.create_group())

        self.hiarc_groups.add_user_to_group(g1.key, u1.key)
        self.hiarc_groups.add_user_to_group(g2.key, u1.key)

        ut = self.hiarc_token.create_user_token(
            hiarc.CreateUserTokenRequest(key=u1.key))
        lc = hiarc.GroupApi(hiarc.ApiClient(
            configuration=self.hiarc_util.init_hiarc_client_jwt_token(ut.bearer_token)))
        groups = lc.get_groups_for_current_user()
        assert len(groups) == 2

        # reset ApiClient to Admin User
        # hiarc.ApiClient(
        #     configuration=self.hiarc_util.init_hiarc_config_admin())

        assert next((g for g in groups if self.hiarc_util.compare_dict_to_entity(
            g, g1)), None) is not None
        assert next((g for g in groups if self.hiarc_util.compare_dict_to_entity(
            g, g2)), None) is not None

    def test_create_user_with_metadata(self):
        """Test case for create_user_with_metadata

        Create a User with Metadata  # noqa: E501
        """
        u1 = self.hiarc_users.create_user(
            self.hiarc_util.create_user(self.hiarc_util.get_test_metadata()))
        gu = self.hiarc_users.get_user(u1.key)

        assert self.hiarc_util.compare_entity_to_entity(u1, gu)
        gu.metadata['startDate'] = dateutil.parser.parse(
            gu.metadata['startDate'])
        self.assertDictEqual(self.hiarc_util.get_test_metadata(), gu.metadata)

    def test_update_user_metadata(self):
        """Test case for update_user_metadata

        Update a User's Metadata  # noqa: E501
        """
        u1 = self.hiarc_users.create_user(
            self.hiarc_util.create_user(self.hiarc_util.get_test_metadata()))
        upmd = {
            "department": "support",
            "quotaCarrying": False,
            "targetRate": 7.271,
            "level": 2,
            "startDate": dateutil.parser.parse("2020-02-25T22:33:50.134Z")
        }
        uu = hiarc.UpdateUserRequest(metadata=upmd)
        updated = self.hiarc_users.update_user(uu, u1.key)
        updated.metadata['startDate'] = dateutil.parser.parse(
            updated.metadata['startDate'])
        self.assertDictEqual(upmd, updated.metadata)

    def test_null_out_metadata(self):
        """Test case for null_out_metadata

        Null out metadata on a User  # noqa: E501
        """
        u1 = self.hiarc_users.create_user(
            self.hiarc_util.create_user(self.hiarc_util.get_test_metadata()))
        upmd = {
            "department": None,
            "quotaCarrying": None
        }
        uu = hiarc.UpdateUserRequest(metadata=upmd)
        updated = self.hiarc_users.update_user(uu, u1.key)
        updated.metadata['startDate'] = dateutil.parser.parse(
            updated.metadata['startDate'])
        assert len(updated.metadata.keys()) == 3

        upmd = {
            "targetRate": None,
            "level": None,
            "startDate": None
        }
        uu = hiarc.UpdateUserRequest(metadata=upmd)
        updated = self.hiarc_users.update_user(uu, u1.key)
        self.assertIsNone(updated.metadata)

    def test_find_users(self):
        """Test case for find_users

        Find a User  # noqa: E501
        """
        md = self.hiarc_util.get_test_metadata()
        u1 = self.hiarc_users.create_user(
            self.hiarc_util.create_user(md))

        md["quotaCarrying"] = False
        self.hiarc_users.create_user(
            self.hiarc_util.create_user(md))
        self.hiarc_users.create_user(
            self.hiarc_util.create_user())

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

        qr = hiarc.FindUsersRequest(query=q)
        fu = self.hiarc_users.find_user(qr)
        assert len(fu) == 1
        assert self.hiarc_util.compare_dict_to_entity(fu[0], u1)


if __name__ == '__main__':
    unittest.main()
