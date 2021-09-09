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

class PoliciesBody(object):
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
        'name': 'str',
        'policy_type_name': 'str',
        'organization_id': 'int',
        'schedule_days': 'int',
        'schedule_weeks_of_month': 'int',
        'schedule_months': 'int',
        'schedule_time': 'str',
        'configuration': 'PolicyConfiguration',
        'notify_user': 'bool',
        'notes': 'str',
        'server_groups': 'list[int]',
        'auto_patch': 'bool',
        'auto_reboot': 'bool',
        'notify_reboot_user': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'policy_type_name': 'policy_type_name',
        'organization_id': 'organization_id',
        'schedule_days': 'schedule_days',
        'schedule_weeks_of_month': 'schedule_weeks_of_month',
        'schedule_months': 'schedule_months',
        'schedule_time': 'schedule_time',
        'configuration': 'configuration',
        'notify_user': 'notify_user',
        'notes': 'notes',
        'server_groups': 'server_groups',
        'auto_patch': 'auto_patch',
        'auto_reboot': 'auto_reboot',
        'notify_reboot_user': 'notify_reboot_user'
    }

    def __init__(self, name=None, policy_type_name=None, organization_id=None, schedule_days=None, schedule_weeks_of_month=None, schedule_months=None, schedule_time=None, configuration=None, notify_user=None, notes=None, server_groups=None, auto_patch=None, auto_reboot=None, notify_reboot_user=None):  # noqa: E501
        """PoliciesBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._policy_type_name = None
        self._organization_id = None
        self._schedule_days = None
        self._schedule_weeks_of_month = None
        self._schedule_months = None
        self._schedule_time = None
        self._configuration = None
        self._notify_user = None
        self._notes = None
        self._server_groups = None
        self._auto_patch = None
        self._auto_reboot = None
        self._notify_reboot_user = None
        self.discriminator = None
        self.name = name
        self.policy_type_name = policy_type_name
        self.organization_id = organization_id
        self.schedule_days = schedule_days
        self.schedule_weeks_of_month = schedule_weeks_of_month
        self.schedule_months = schedule_months
        self.schedule_time = schedule_time
        self.configuration = configuration
        self.notify_user = notify_user
        if notes is not None:
            self.notes = notes
        if server_groups is not None:
            self.server_groups = server_groups
        if auto_patch is not None:
            self.auto_patch = auto_patch
        if auto_reboot is not None:
            self.auto_reboot = auto_reboot
        if notify_reboot_user is not None:
            self.notify_reboot_user = notify_reboot_user

    @property
    def name(self):
        """Gets the name of this PoliciesBody.  # noqa: E501

        The name of the policy.  # noqa: E501

        :return: The name of this PoliciesBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PoliciesBody.

        The name of the policy.  # noqa: E501

        :param name: The name of this PoliciesBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def policy_type_name(self):
        """Gets the policy_type_name of this PoliciesBody.  # noqa: E501


        :return: The policy_type_name of this PoliciesBody.  # noqa: E501
        :rtype: str
        """
        return self._policy_type_name

    @policy_type_name.setter
    def policy_type_name(self, policy_type_name):
        """Sets the policy_type_name of this PoliciesBody.


        :param policy_type_name: The policy_type_name of this PoliciesBody.  # noqa: E501
        :type: str
        """
        if policy_type_name is None:
            raise ValueError("Invalid value for `policy_type_name`, must not be `None`")  # noqa: E501
        allowed_values = ["patch", "custom", "required_software"]  # noqa: E501
        if policy_type_name not in allowed_values:
            raise ValueError(
                "Invalid value for `policy_type_name` ({0}), must be one of {1}"  # noqa: E501
                .format(policy_type_name, allowed_values)
            )

        self._policy_type_name = policy_type_name

    @property
    def organization_id(self):
        """Gets the organization_id of this PoliciesBody.  # noqa: E501

        Organization ID for the specified policy  # noqa: E501

        :return: The organization_id of this PoliciesBody.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this PoliciesBody.

        Organization ID for the specified policy  # noqa: E501

        :param organization_id: The organization_id of this PoliciesBody.  # noqa: E501
        :type: int
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def schedule_days(self):
        """Gets the schedule_days of this PoliciesBody.  # noqa: E501

        Decimal value of binary day schedule. See [Policy and Device Filters, and Scheduling - Example Days per Week](/developer-portal/policy_filters_schedule/#example-days-per-week).  # noqa: E501

        :return: The schedule_days of this PoliciesBody.  # noqa: E501
        :rtype: int
        """
        return self._schedule_days

    @schedule_days.setter
    def schedule_days(self, schedule_days):
        """Sets the schedule_days of this PoliciesBody.

        Decimal value of binary day schedule. See [Policy and Device Filters, and Scheduling - Example Days per Week](/developer-portal/policy_filters_schedule/#example-days-per-week).  # noqa: E501

        :param schedule_days: The schedule_days of this PoliciesBody.  # noqa: E501
        :type: int
        """
        if schedule_days is None:
            raise ValueError("Invalid value for `schedule_days`, must not be `None`")  # noqa: E501

        self._schedule_days = schedule_days

    @property
    def schedule_weeks_of_month(self):
        """Gets the schedule_weeks_of_month of this PoliciesBody.  # noqa: E501

        Decimal value of binary week schedule. See [Policy and Device Filters, and Scheduling - Example Weeks per Month](/developer-portal/policy_filters_schedule/#example-weeks-per-month).  # noqa: E501

        :return: The schedule_weeks_of_month of this PoliciesBody.  # noqa: E501
        :rtype: int
        """
        return self._schedule_weeks_of_month

    @schedule_weeks_of_month.setter
    def schedule_weeks_of_month(self, schedule_weeks_of_month):
        """Sets the schedule_weeks_of_month of this PoliciesBody.

        Decimal value of binary week schedule. See [Policy and Device Filters, and Scheduling - Example Weeks per Month](/developer-portal/policy_filters_schedule/#example-weeks-per-month).  # noqa: E501

        :param schedule_weeks_of_month: The schedule_weeks_of_month of this PoliciesBody.  # noqa: E501
        :type: int
        """
        if schedule_weeks_of_month is None:
            raise ValueError("Invalid value for `schedule_weeks_of_month`, must not be `None`")  # noqa: E501

        self._schedule_weeks_of_month = schedule_weeks_of_month

    @property
    def schedule_months(self):
        """Gets the schedule_months of this PoliciesBody.  # noqa: E501

        Decimal value of binary month schedule. See [Policy and Device Filters, and Scheduling - Example Months per Year](/developer-portal/policy_filters_schedule/#example-months-per-year).  # noqa: E501

        :return: The schedule_months of this PoliciesBody.  # noqa: E501
        :rtype: int
        """
        return self._schedule_months

    @schedule_months.setter
    def schedule_months(self, schedule_months):
        """Sets the schedule_months of this PoliciesBody.

        Decimal value of binary month schedule. See [Policy and Device Filters, and Scheduling - Example Months per Year](/developer-portal/policy_filters_schedule/#example-months-per-year).  # noqa: E501

        :param schedule_months: The schedule_months of this PoliciesBody.  # noqa: E501
        :type: int
        """
        if schedule_months is None:
            raise ValueError("Invalid value for `schedule_months`, must not be `None`")  # noqa: E501

        self._schedule_months = schedule_months

    @property
    def schedule_time(self):
        """Gets the schedule_time of this PoliciesBody.  # noqa: E501

        Scheduled time for automatic policy execution. Format: `\"hh:mm\"`  # noqa: E501

        :return: The schedule_time of this PoliciesBody.  # noqa: E501
        :rtype: str
        """
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, schedule_time):
        """Sets the schedule_time of this PoliciesBody.

        Scheduled time for automatic policy execution. Format: `\"hh:mm\"`  # noqa: E501

        :param schedule_time: The schedule_time of this PoliciesBody.  # noqa: E501
        :type: str
        """
        if schedule_time is None:
            raise ValueError("Invalid value for `schedule_time`, must not be `None`")  # noqa: E501

        self._schedule_time = schedule_time

    @property
    def configuration(self):
        """Gets the configuration of this PoliciesBody.  # noqa: E501


        :return: The configuration of this PoliciesBody.  # noqa: E501
        :rtype: PolicyConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this PoliciesBody.


        :param configuration: The configuration of this PoliciesBody.  # noqa: E501
        :type: PolicyConfiguration
        """
        if configuration is None:
            raise ValueError("Invalid value for `configuration`, must not be `None`")  # noqa: E501

        self._configuration = configuration

    @property
    def notify_user(self):
        """Gets the notify_user of this PoliciesBody.  # noqa: E501

        Display notification 15 minutes before patching.  # noqa: E501

        :return: The notify_user of this PoliciesBody.  # noqa: E501
        :rtype: bool
        """
        return self._notify_user

    @notify_user.setter
    def notify_user(self, notify_user):
        """Sets the notify_user of this PoliciesBody.

        Display notification 15 minutes before patching.  # noqa: E501

        :param notify_user: The notify_user of this PoliciesBody.  # noqa: E501
        :type: bool
        """
        if notify_user is None:
            raise ValueError("Invalid value for `notify_user`, must not be `None`")  # noqa: E501

        self._notify_user = notify_user

    @property
    def notes(self):
        """Gets the notes of this PoliciesBody.  # noqa: E501

        Policy notes  # noqa: E501

        :return: The notes of this PoliciesBody.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PoliciesBody.

        Policy notes  # noqa: E501

        :param notes: The notes of this PoliciesBody.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def server_groups(self):
        """Gets the server_groups of this PoliciesBody.  # noqa: E501

        Integer array. Server groups to link with the policy  # noqa: E501

        :return: The server_groups of this PoliciesBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._server_groups

    @server_groups.setter
    def server_groups(self, server_groups):
        """Sets the server_groups of this PoliciesBody.

        Integer array. Server groups to link with the policy  # noqa: E501

        :param server_groups: The server_groups of this PoliciesBody.  # noqa: E501
        :type: list[int]
        """

        self._server_groups = server_groups

    @property
    def auto_patch(self):
        """Gets the auto_patch of this PoliciesBody.  # noqa: E501

        Enable or Disable automatic execution of the policy.  # noqa: E501

        :return: The auto_patch of this PoliciesBody.  # noqa: E501
        :rtype: bool
        """
        return self._auto_patch

    @auto_patch.setter
    def auto_patch(self, auto_patch):
        """Sets the auto_patch of this PoliciesBody.

        Enable or Disable automatic execution of the policy.  # noqa: E501

        :param auto_patch: The auto_patch of this PoliciesBody.  # noqa: E501
        :type: bool
        """

        self._auto_patch = auto_patch

    @property
    def auto_reboot(self):
        """Gets the auto_reboot of this PoliciesBody.  # noqa: E501

        Enable or Disable automatic reboots following policy execution.  # noqa: E501

        :return: The auto_reboot of this PoliciesBody.  # noqa: E501
        :rtype: bool
        """
        return self._auto_reboot

    @auto_reboot.setter
    def auto_reboot(self, auto_reboot):
        """Sets the auto_reboot of this PoliciesBody.

        Enable or Disable automatic reboots following policy execution.  # noqa: E501

        :param auto_reboot: The auto_reboot of this PoliciesBody.  # noqa: E501
        :type: bool
        """

        self._auto_reboot = auto_reboot

    @property
    def notify_reboot_user(self):
        """Gets the notify_reboot_user of this PoliciesBody.  # noqa: E501

        Display modified notification 15 minutes before patching. This message should inform the user that a reboot will follow patching actions.  # noqa: E501

        :return: The notify_reboot_user of this PoliciesBody.  # noqa: E501
        :rtype: bool
        """
        return self._notify_reboot_user

    @notify_reboot_user.setter
    def notify_reboot_user(self, notify_reboot_user):
        """Sets the notify_reboot_user of this PoliciesBody.

        Display modified notification 15 minutes before patching. This message should inform the user that a reboot will follow patching actions.  # noqa: E501

        :param notify_reboot_user: The notify_reboot_user of this PoliciesBody.  # noqa: E501
        :type: bool
        """

        self._notify_reboot_user = notify_reboot_user

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
        if issubclass(PoliciesBody, dict):
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
        if not isinstance(other, PoliciesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other