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

class NonCompliantNonCompliantDevices(object):
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
        'name': 'str',
        'custom_name': 'str',
        'server_create_time': 'datetime',
        'last_refresh_time': 'datetime',
        'connected': 'bool',
        'needs_reboot': 'bool',
        'group_id': 'int',
        'os_family': 'str',
        'policies': 'list[NonCompliantNonCompliantPolicies]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'custom_name': 'customName',
        'server_create_time': 'serverCreateTime',
        'last_refresh_time': 'lastRefreshTime',
        'connected': 'connected',
        'needs_reboot': 'needsReboot',
        'group_id': 'groupId',
        'os_family': 'os_family',
        'policies': 'policies'
    }

    def __init__(self, id=None, name=None, custom_name=None, server_create_time=None, last_refresh_time=None, connected=None, needs_reboot=None, group_id=None, os_family=None, policies=None):  # noqa: E501
        """NonCompliantNonCompliantDevices - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._custom_name = None
        self._server_create_time = None
        self._last_refresh_time = None
        self._connected = None
        self._needs_reboot = None
        self._group_id = None
        self._os_family = None
        self._policies = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if custom_name is not None:
            self.custom_name = custom_name
        if server_create_time is not None:
            self.server_create_time = server_create_time
        if last_refresh_time is not None:
            self.last_refresh_time = last_refresh_time
        if connected is not None:
            self.connected = connected
        if needs_reboot is not None:
            self.needs_reboot = needs_reboot
        if group_id is not None:
            self.group_id = group_id
        if os_family is not None:
            self.os_family = os_family
        if policies is not None:
            self.policies = policies

    @property
    def id(self):
        """Gets the id of this NonCompliantNonCompliantDevices.  # noqa: E501


        :return: The id of this NonCompliantNonCompliantDevices.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NonCompliantNonCompliantDevices.


        :param id: The id of this NonCompliantNonCompliantDevices.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NonCompliantNonCompliantDevices.  # noqa: E501


        :return: The name of this NonCompliantNonCompliantDevices.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NonCompliantNonCompliantDevices.


        :param name: The name of this NonCompliantNonCompliantDevices.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def custom_name(self):
        """Gets the custom_name of this NonCompliantNonCompliantDevices.  # noqa: E501


        :return: The custom_name of this NonCompliantNonCompliantDevices.  # noqa: E501
        :rtype: str
        """
        return self._custom_name

    @custom_name.setter
    def custom_name(self, custom_name):
        """Sets the custom_name of this NonCompliantNonCompliantDevices.


        :param custom_name: The custom_name of this NonCompliantNonCompliantDevices.  # noqa: E501
        :type: str
        """

        self._custom_name = custom_name

    @property
    def server_create_time(self):
        """Gets the server_create_time of this NonCompliantNonCompliantDevices.  # noqa: E501


        :return: The server_create_time of this NonCompliantNonCompliantDevices.  # noqa: E501
        :rtype: datetime
        """
        return self._server_create_time

    @server_create_time.setter
    def server_create_time(self, server_create_time):
        """Sets the server_create_time of this NonCompliantNonCompliantDevices.


        :param server_create_time: The server_create_time of this NonCompliantNonCompliantDevices.  # noqa: E501
        :type: datetime
        """

        self._server_create_time = server_create_time

    @property
    def last_refresh_time(self):
        """Gets the last_refresh_time of this NonCompliantNonCompliantDevices.  # noqa: E501


        :return: The last_refresh_time of this NonCompliantNonCompliantDevices.  # noqa: E501
        :rtype: datetime
        """
        return self._last_refresh_time

    @last_refresh_time.setter
    def last_refresh_time(self, last_refresh_time):
        """Sets the last_refresh_time of this NonCompliantNonCompliantDevices.


        :param last_refresh_time: The last_refresh_time of this NonCompliantNonCompliantDevices.  # noqa: E501
        :type: datetime
        """

        self._last_refresh_time = last_refresh_time

    @property
    def connected(self):
        """Gets the connected of this NonCompliantNonCompliantDevices.  # noqa: E501


        :return: The connected of this NonCompliantNonCompliantDevices.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this NonCompliantNonCompliantDevices.


        :param connected: The connected of this NonCompliantNonCompliantDevices.  # noqa: E501
        :type: bool
        """

        self._connected = connected

    @property
    def needs_reboot(self):
        """Gets the needs_reboot of this NonCompliantNonCompliantDevices.  # noqa: E501


        :return: The needs_reboot of this NonCompliantNonCompliantDevices.  # noqa: E501
        :rtype: bool
        """
        return self._needs_reboot

    @needs_reboot.setter
    def needs_reboot(self, needs_reboot):
        """Sets the needs_reboot of this NonCompliantNonCompliantDevices.


        :param needs_reboot: The needs_reboot of this NonCompliantNonCompliantDevices.  # noqa: E501
        :type: bool
        """

        self._needs_reboot = needs_reboot

    @property
    def group_id(self):
        """Gets the group_id of this NonCompliantNonCompliantDevices.  # noqa: E501


        :return: The group_id of this NonCompliantNonCompliantDevices.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this NonCompliantNonCompliantDevices.


        :param group_id: The group_id of this NonCompliantNonCompliantDevices.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def os_family(self):
        """Gets the os_family of this NonCompliantNonCompliantDevices.  # noqa: E501


        :return: The os_family of this NonCompliantNonCompliantDevices.  # noqa: E501
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """Sets the os_family of this NonCompliantNonCompliantDevices.


        :param os_family: The os_family of this NonCompliantNonCompliantDevices.  # noqa: E501
        :type: str
        """

        self._os_family = os_family

    @property
    def policies(self):
        """Gets the policies of this NonCompliantNonCompliantDevices.  # noqa: E501


        :return: The policies of this NonCompliantNonCompliantDevices.  # noqa: E501
        :rtype: list[NonCompliantNonCompliantPolicies]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this NonCompliantNonCompliantDevices.


        :param policies: The policies of this NonCompliantNonCompliantDevices.  # noqa: E501
        :type: list[NonCompliantNonCompliantPolicies]
        """

        self._policies = policies

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
        if issubclass(NonCompliantNonCompliantDevices, dict):
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
        if not isinstance(other, NonCompliantNonCompliantDevices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other