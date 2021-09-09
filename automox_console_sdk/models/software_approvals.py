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

class SoftwareApprovals(object):
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
        'id': 'int',
        'software_version_id': 'int',
        'policy_id': 'int',
        'manual_approval': 'bool',
        'manual_approval_time': 'datetime',
        'auto_approval': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'software_version_id': 'software_version_id',
        'policy_id': 'policy_id',
        'manual_approval': 'manual_approval',
        'manual_approval_time': 'manual_approval_time',
        'auto_approval': 'auto_approval'
    }

    def __init__(self, id=None, software_version_id=None, policy_id=None, manual_approval=None, manual_approval_time=None, auto_approval=None):  # noqa: E501
        """SoftwareApprovals - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._software_version_id = None
        self._policy_id = None
        self._manual_approval = None
        self._manual_approval_time = None
        self._auto_approval = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if software_version_id is not None:
            self.software_version_id = software_version_id
        if policy_id is not None:
            self.policy_id = policy_id
        self.manual_approval = manual_approval
        if manual_approval_time is not None:
            self.manual_approval_time = manual_approval_time
        if auto_approval is not None:
            self.auto_approval = auto_approval

    @property
    def id(self):
        """Gets the id of this SoftwareApprovals.  # noqa: E501


        :return: The id of this SoftwareApprovals.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SoftwareApprovals.


        :param id: The id of this SoftwareApprovals.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def software_version_id(self):
        """Gets the software_version_id of this SoftwareApprovals.  # noqa: E501


        :return: The software_version_id of this SoftwareApprovals.  # noqa: E501
        :rtype: int
        """
        return self._software_version_id

    @software_version_id.setter
    def software_version_id(self, software_version_id):
        """Sets the software_version_id of this SoftwareApprovals.


        :param software_version_id: The software_version_id of this SoftwareApprovals.  # noqa: E501
        :type: int
        """

        self._software_version_id = software_version_id

    @property
    def policy_id(self):
        """Gets the policy_id of this SoftwareApprovals.  # noqa: E501


        :return: The policy_id of this SoftwareApprovals.  # noqa: E501
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this SoftwareApprovals.


        :param policy_id: The policy_id of this SoftwareApprovals.  # noqa: E501
        :type: int
        """

        self._policy_id = policy_id

    @property
    def manual_approval(self):
        """Gets the manual_approval of this SoftwareApprovals.  # noqa: E501

        true = Approved, false = Rejected  # noqa: E501

        :return: The manual_approval of this SoftwareApprovals.  # noqa: E501
        :rtype: bool
        """
        return self._manual_approval

    @manual_approval.setter
    def manual_approval(self, manual_approval):
        """Sets the manual_approval of this SoftwareApprovals.

        true = Approved, false = Rejected  # noqa: E501

        :param manual_approval: The manual_approval of this SoftwareApprovals.  # noqa: E501
        :type: bool
        """
        if manual_approval is None:
            raise ValueError("Invalid value for `manual_approval`, must not be `None`")  # noqa: E501

        self._manual_approval = manual_approval

    @property
    def manual_approval_time(self):
        """Gets the manual_approval_time of this SoftwareApprovals.  # noqa: E501


        :return: The manual_approval_time of this SoftwareApprovals.  # noqa: E501
        :rtype: datetime
        """
        return self._manual_approval_time

    @manual_approval_time.setter
    def manual_approval_time(self, manual_approval_time):
        """Sets the manual_approval_time of this SoftwareApprovals.


        :param manual_approval_time: The manual_approval_time of this SoftwareApprovals.  # noqa: E501
        :type: datetime
        """

        self._manual_approval_time = manual_approval_time

    @property
    def auto_approval(self):
        """Gets the auto_approval of this SoftwareApprovals.  # noqa: E501


        :return: The auto_approval of this SoftwareApprovals.  # noqa: E501
        :rtype: bool
        """
        return self._auto_approval

    @auto_approval.setter
    def auto_approval(self, auto_approval):
        """Sets the auto_approval of this SoftwareApprovals.


        :param auto_approval: The auto_approval of this SoftwareApprovals.  # noqa: E501
        :type: bool
        """

        self._auto_approval = auto_approval

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
        if issubclass(SoftwareApprovals, dict):
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
        if not isinstance(other, SoftwareApprovals):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other