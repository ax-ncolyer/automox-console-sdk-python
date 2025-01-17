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

class NonCompliant(object):
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
        'non_compliant': 'NonCompliantNonCompliant'
    }

    attribute_map = {
        'non_compliant': 'nonCompliant'
    }

    def __init__(self, non_compliant=None):  # noqa: E501
        """NonCompliant - a model defined in Swagger"""  # noqa: E501
        self._non_compliant = None
        self.discriminator = None
        if non_compliant is not None:
            self.non_compliant = non_compliant

    @property
    def non_compliant(self):
        """Gets the non_compliant of this NonCompliant.  # noqa: E501


        :return: The non_compliant of this NonCompliant.  # noqa: E501
        :rtype: NonCompliantNonCompliant
        """
        return self._non_compliant

    @non_compliant.setter
    def non_compliant(self, non_compliant):
        """Sets the non_compliant of this NonCompliant.


        :param non_compliant: The non_compliant of this NonCompliant.  # noqa: E501
        :type: NonCompliantNonCompliant
        """

        self._non_compliant = non_compliant

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
        if issubclass(NonCompliant, dict):
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
        if not isinstance(other, NonCompliant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
