from __future__ import absolute_import
from integration_tests.hiarc_util import hiarc_util

import unittest
import dateutil.parser

import hiarc
from hiarc.api.user_api import UserApi  # noqa: E501
from hiarc.rest import ApiException


class TestClassificationApi(unittest.TestCase):
    """ClassificationApi unit test stubs"""

    def setUp(self):
        self.hiarc_util = hiarc_util()
        self.hiarc_config = self.hiarc_util.init_hiarc_config_admin()
        self.hiarc_client = hiarc.ApiClient(self.hiarc_config)
        self.hiarc_classifications = hiarc.ClassificationApi(self.hiarc_client)
        hiarc.AdminApi(self.hiarc_client).reset_db()

    def tearDown(self):
        pass

    def test_crud(self):
        """Test case for classification CRUD actions

        Classification CRUD  # noqa: E501
        """
        c=self.hiarc_classifications.create_classification(
            self.hiarc_util.create_classification())
        fc=self.hiarc_classifications.get_classification(c.key)
        assert c == fc

        new_name="New Name"
        new_description="New description"
        uc=hiarc.UpdateClassificationRequest(
            name = new_name, description = new_description)
        updated=self.hiarc_classifications.update_classification(uc, c.key)
        assert new_name == updated.name
        assert new_description == updated.description
        assert updated.modified_at > updated.created_at

        uc=hiarc.UpdateClassificationRequest(key = 'new key')
        self.assertRaises(hiarc.rest.ApiException,
                          self.hiarc_classifications.update_classification, uc, c.key)

        # self.hiarc_classifications.delete_classification(c.key)
        # self.assertRaises(hiarc.rest.ApiException,
        #                   self.hiarc_groups.get_group, g.key)

    def test_get_all_classifications(self):
        """Test case for get_all_classifications

        Get all Classifications  # noqa: E501
        """
        for i in range(self.hiarc_util.LARGE_ENTITY_COUNT):
            self.hiarc_classifications.create_classification(
                self.hiarc_util.create_classification())
        all_classifications= self.hiarc_classifications.get_all_classifications()
        assert self.hiarc_util.LARGE_ENTITY_COUNT == len(all_classifications)

    def test_create_classification_with_metadata(self):
        """Test case for create_classification_with_metadata

        Create a Classification with Metadata  # noqa: E501
        """
        c1= self.hiarc_classifications.create_classification(
            self.hiarc_util.create_classification(self.hiarc_util.get_test_metadata()))
        gc= self.hiarc_classifications.get_classification(c1.key)

        assert self.hiarc_util.compare_entity_to_entity(c1, gc)
        gc.metadata['startDate']= dateutil.parser.parse(
            gc.metadata['startDate'])
        self.assertDictEqual(self.hiarc_util.get_test_metadata(), gc.metadata)

    def test_update_classification_metadata(self):
        """Test case for update_classification_metadata

        Update a Classification's Metadata  # noqa: E501
        """
        c1= self.hiarc_classifications.create_classification(
            self.hiarc_util.create_classification(self.hiarc_util.get_test_metadata()))
        upmd= {
            "department": "support",
            "quotaCarrying": False,
            "targetRate": 7.271,
            "level": 2,
            "startDate": dateutil.parser.parse("2020-02-25T22:33:50.134Z")
        }
        uc = hiarc.UpdateClassificationRequest(metadata=upmd)
        updated = self.hiarc_classifications.update_classification(uc, c1.key)
        updated.metadata['startDate'] = dateutil.parser.parse(
            updated.metadata['startDate'])
        self.assertDictEqual(upmd, updated.metadata)

    def test_null_out_metadata(self):
        """Test case for null_out_metadata

        Null out metadata on a Classification  # noqa: E501
        """
        c1= self.hiarc_classifications.create_classification(
            self.hiarc_util.create_classification(self.hiarc_util.get_test_metadata()))
        upmd= {
            "department": None,
            "quotaCarrying": None
        }
        uc = hiarc.UpdateClassificationRequest(metadata=upmd)
        updated = self.hiarc_classifications.update_classification(uc, c1.key)
        updated.metadata['startDate'] = dateutil.parser.parse(
            updated.metadata['startDate'])
        assert len(updated.metadata.keys()) == 3

        upmd= {
            "targetRate": None,
            "level": None,
            "startDate": None
        }
        uc = hiarc.UpdateClassificationRequest(metadata=upmd)
        updated = self.hiarc_classifications.update_classification(uc, c1.key)
        self.assertIsNone(updated.metadata)

    def test_find_classifications(self):
        """Test case for find_classifications

        Find a Classification  # noqa: E501
        """
        md = self.hiarc_util.get_test_metadata()
        c1 = self.hiarc_classifications.create_classification(
            self.hiarc_util.create_classification(md))

        md["quotaCarrying"]= False
        self.hiarc_classifications.create_classification(
            self.hiarc_util.create_classification(md))
        self.hiarc_classifications.create_classification(
            self.hiarc_util.create_classification())

        q= [{
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

        qr= hiarc.FindClassificationsRequest(query=q)
        fc= self.hiarc_classifications.find_classification(qr)
        assert len(fc) == 1
        assert self.hiarc_util.compare_dict_to_entity(fc[0], c1)

if __name__ == '__main__':
    unittest.main()
