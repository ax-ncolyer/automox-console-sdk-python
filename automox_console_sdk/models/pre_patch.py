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

class PrePatch(object):
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
        'prepatch': 'PrePatchPrepatch'
    }

    attribute_map = {
        'prepatch': 'prepatch'
    }

    def __init__(self, prepatch=None):  # noqa: E501
        """PrePatch - a model defined in Swagger"""  # noqa: E501
        self._prepatch = None
        self.discriminator = None
        if prepatch is not None:
            self.prepatch = prepatch

    @property
    def prepatch(self):
        """Gets the prepatch of this PrePatch.  # noqa: E501


        :return: The prepatch of this PrePatch.  # noqa: E501
        :rtype: PrePatchPrepatch
        """
        return self._prepatch

    @prepatch.setter
    def prepatch(self, prepatch):
        """Sets the prepatch of this PrePatch.


        :param prepatch: The prepatch of this PrePatch.  # noqa: E501
        :type: PrePatchPrepatch
        """

        self._prepatch = prepatch

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
        if issubclass(PrePatch, dict):
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
        if not isinstance(other, PrePatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
