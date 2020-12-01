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

class UserCredentials(object):
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
        'bearer_token': 'str',
        'created_at': 'datetime',
        'expires_at': 'datetime'
    }

    attribute_map = {
        'user_key': 'userKey',
        'bearer_token': 'bearerToken',
        'created_at': 'createdAt',
        'expires_at': 'expiresAt'
    }

    def __init__(self, user_key=None, bearer_token=None, created_at=None, expires_at=None):  # noqa: E501
        """UserCredentials - a model defined in Swagger"""  # noqa: E501
        self._user_key = None
        self._bearer_token = None
        self._created_at = None
        self._expires_at = None
        self.discriminator = None
        if user_key is not None:
            self.user_key = user_key
        if bearer_token is not None:
            self.bearer_token = bearer_token
        if created_at is not None:
            self.created_at = created_at
        if expires_at is not None:
            self.expires_at = expires_at

    @property
    def user_key(self):
        """Gets the user_key of this UserCredentials.  # noqa: E501


        :return: The user_key of this UserCredentials.  # noqa: E501
        :rtype: str
        """
        return self._user_key

    @user_key.setter
    def user_key(self, user_key):
        """Sets the user_key of this UserCredentials.


        :param user_key: The user_key of this UserCredentials.  # noqa: E501
        :type: str
        """

        self._user_key = user_key

    @property
    def bearer_token(self):
        """Gets the bearer_token of this UserCredentials.  # noqa: E501


        :return: The bearer_token of this UserCredentials.  # noqa: E501
        :rtype: str
        """
        return self._bearer_token

    @bearer_token.setter
    def bearer_token(self, bearer_token):
        """Sets the bearer_token of this UserCredentials.


        :param bearer_token: The bearer_token of this UserCredentials.  # noqa: E501
        :type: str
        """

        self._bearer_token = bearer_token

    @property
    def created_at(self):
        """Gets the created_at of this UserCredentials.  # noqa: E501


        :return: The created_at of this UserCredentials.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserCredentials.


        :param created_at: The created_at of this UserCredentials.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def expires_at(self):
        """Gets the expires_at of this UserCredentials.  # noqa: E501


        :return: The expires_at of this UserCredentials.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this UserCredentials.


        :param expires_at: The expires_at of this UserCredentials.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

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
        if issubclass(UserCredentials, dict):
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
        if not isinstance(other, UserCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other