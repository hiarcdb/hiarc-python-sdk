# coding: utf-8

"""
    Hiarc API

    Welcome to the Hiarc API documentation.  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import json
import pprint
import re  # noqa: F401

import six
from hiarc.models.create_or_update_entity_request import CreateOrUpdateEntityRequest  # noqa: F401,E501

class CreateFileRequest(CreateOrUpdateEntityRequest):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'storage_service': 'str'
    }
    if hasattr(CreateOrUpdateEntityRequest, "swagger_types"):
        swagger_types.update(CreateOrUpdateEntityRequest.swagger_types)

    attribute_map = {
        'storage_service': 'storageService'
    }
    if hasattr(CreateOrUpdateEntityRequest, "attribute_map"):
        attribute_map.update(CreateOrUpdateEntityRequest.attribute_map)

    def __init__(self, storage_service=None, *args, **kwargs):  # noqa: E501
        """CreateFileRequest - a model defined in Swagger"""  # noqa: E501
        self._storage_service = None
        self.discriminator = None
        if storage_service is not None:
            self.storage_service = storage_service
        CreateOrUpdateEntityRequest.__init__(self, *args, **kwargs)

    @property
    def storage_service(self):
        """Gets the storage_service of this CreateFileRequest.  # noqa: E501


        :return: The storage_service of this CreateFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_service

    @storage_service.setter
    def storage_service(self, storage_service):
        """Sets the storage_service of this CreateFileRequest.


        :param storage_service: The storage_service of this CreateFileRequest.  # noqa: E501
        :type: str
        """

        self._storage_service = storage_service

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CreateFileRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def to_json(self):
        return json.dumps({
            "key": self.key,
            "name": self.name,
            "description": self.description,
            "metadata": self.metadata,
            "storageService": self.storage_service
        }, indent=4, sort_keys=True, default=str)

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other