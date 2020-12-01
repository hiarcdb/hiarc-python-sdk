# coding: utf-8

"""
    Hiarc API

    Welcome to the Hiarc API documentation.  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AddUserToFileRequest(object):
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
        'user_key': 'str',
        'access_level': 'AccessLevel'
    }

    attribute_map = {
        'user_key': 'userKey',
        'access_level': 'accessLevel'
    }

    def __init__(self, user_key=None, access_level=None):  # noqa: E501
        """AddUserToFileRequest - a model defined in Swagger"""  # noqa: E501
        self._user_key = None
        self._access_level = None
        self.discriminator = None
        if user_key is not None:
            self.user_key = user_key
        if access_level is not None:
            self.access_level = access_level

    @property
    def user_key(self):
        """Gets the user_key of this AddUserToFileRequest.  # noqa: E501


        :return: The user_key of this AddUserToFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_key

    @user_key.setter
    def user_key(self, user_key):
        """Sets the user_key of this AddUserToFileRequest.


        :param user_key: The user_key of this AddUserToFileRequest.  # noqa: E501
        :type: str
        """

        self._user_key = user_key

    @property
    def access_level(self):
        """Gets the access_level of this AddUserToFileRequest.  # noqa: E501


        :return: The access_level of this AddUserToFileRequest.  # noqa: E501
        :rtype: AccessLevel
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this AddUserToFileRequest.


        :param access_level: The access_level of this AddUserToFileRequest.  # noqa: E501
        :type: AccessLevel
        """

        self._access_level = access_level

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
        if issubclass(AddUserToFileRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddUserToFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other