# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-09-01
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ServersBatchBody(object):
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
        'devices': 'list[int]',
        'actions': 'list[ServersbatchActions]'
    }

    attribute_map = {
        'devices': 'devices',
        'actions': 'actions'
    }

    def __init__(self, devices=None, actions=None):  # noqa: E501
        """ServersBatchBody - a model defined in Swagger"""  # noqa: E501
        self._devices = None
        self._actions = None
        self.discriminator = None
        self.devices = devices
        self.actions = actions

    @property
    def devices(self):
        """Gets the devices of this ServersBatchBody.  # noqa: E501

        List of device (server) ids  # noqa: E501

        :return: The devices of this ServersBatchBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this ServersBatchBody.

        List of device (server) ids  # noqa: E501

        :param devices: The devices of this ServersBatchBody.  # noqa: E501
        :type: list[int]
        """
        if devices is None:
            raise ValueError("Invalid value for `devices`, must not be `None`")  # noqa: E501

        self._devices = devices

    @property
    def actions(self):
        """Gets the actions of this ServersBatchBody.  # noqa: E501

        Array of different actions to take on each device  # noqa: E501

        :return: The actions of this ServersBatchBody.  # noqa: E501
        :rtype: list[ServersbatchActions]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ServersBatchBody.

        Array of different actions to take on each device  # noqa: E501

        :param actions: The actions of this ServersBatchBody.  # noqa: E501
        :type: list[ServersbatchActions]
        """
        if actions is None:
            raise ValueError("Invalid value for `actions`, must not be `None`")  # noqa: E501

        self._actions = actions

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
        if issubclass(ServersBatchBody, dict):
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
        if not isinstance(other, ServersBatchBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other