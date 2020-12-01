from __future__ import absolute_import
from integration_tests.hiarc_util import hiarc_util

import unittest

import hiarc
from hiarc.api.user_api import UserApi  # noqa: E501
from hiarc.rest import ApiException


class TestLegalHoldApi(unittest.TestCase):
    """LegalHoldApi unit test stubs"""

    def setUp(self):
        self.hiarc_util = hiarc_util()
        self.hiarc_config = self.hiarc_util.init_hiarc_config_admin()
        self.hiarc_client = hiarc.ApiClient(self.hiarc_config)
        self.hiarc_legal_holds = hiarc.LegalHoldApi(self.hiarc_client)
        hiarc.AdminApi(self.hiarc_client).reset_db()

    def tearDown(self):
        pass

    def test_crud(self):
        """Test case for legal hold CRUD actions

        Legal Hold CRUD  # noqa: E501
        """
        lh = self.hiarc_legal_holds.create_legal_hold(self.hiarc_util.create_legal_hold())
        flh = self.hiarc_legal_holds.get_legal_hold(lh.key)
        assert lh == flh

if __name__ == '__main__':
    unittest.main()
