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

class Patches(object):
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
        'package_version_id': 'int',
        'name': 'str',
        'severity': 'str',
        'cve': 'str',
        'create_time': 'datetime',
        'patch_time': 'datetime',
        'needs_approval': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'package_version_id': 'packageVersionId',
        'name': 'name',
        'severity': 'severity',
        'cve': 'cve',
        'create_time': 'createTime',
        'patch_time': 'patchTime',
        'needs_approval': 'needsApproval'
    }

    def __init__(self, id=None, package_version_id=None, name=None, severity=None, cve=None, create_time=None, patch_time=None, needs_approval=None):  # noqa: E501
        """Patches - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._package_version_id = None
        self._name = None
        self._severity = None
        self._cve = None
        self._create_time = None
        self._patch_time = None
        self._needs_approval = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if package_version_id is not None:
            self.package_version_id = package_version_id
        if name is not None:
            self.name = name
        if severity is not None:
            self.severity = severity
        if cve is not None:
            self.cve = cve
        if create_time is not None:
            self.create_time = create_time
        if patch_time is not None:
            self.patch_time = patch_time
        if needs_approval is not None:
            self.needs_approval = needs_approval

    @property
    def id(self):
        """Gets the id of this Patches.  # noqa: E501


        :return: The id of this Patches.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Patches.


        :param id: The id of this Patches.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def package_version_id(self):
        """Gets the package_version_id of this Patches.  # noqa: E501


        :return: The package_version_id of this Patches.  # noqa: E501
        :rtype: int
        """
        return self._package_version_id

    @package_version_id.setter
    def package_version_id(self, package_version_id):
        """Sets the package_version_id of this Patches.


        :param package_version_id: The package_version_id of this Patches.  # noqa: E501
        :type: int
        """

        self._package_version_id = package_version_id

    @property
    def name(self):
        """Gets the name of this Patches.  # noqa: E501


        :return: The name of this Patches.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Patches.


        :param name: The name of this Patches.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def severity(self):
        """Gets the severity of this Patches.  # noqa: E501


        :return: The severity of this Patches.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Patches.


        :param severity: The severity of this Patches.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def cve(self):
        """Gets the cve of this Patches.  # noqa: E501


        :return: The cve of this Patches.  # noqa: E501
        :rtype: str
        """
        return self._cve

    @cve.setter
    def cve(self, cve):
        """Sets the cve of this Patches.


        :param cve: The cve of this Patches.  # noqa: E501
        :type: str
        """

        self._cve = cve

    @property
    def create_time(self):
        """Gets the create_time of this Patches.  # noqa: E501


        :return: The create_time of this Patches.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Patches.


        :param create_time: The create_time of this Patches.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def patch_time(self):
        """Gets the patch_time of this Patches.  # noqa: E501


        :return: The patch_time of this Patches.  # noqa: E501
        :rtype: datetime
        """
        return self._patch_time

    @patch_time.setter
    def patch_time(self, patch_time):
        """Sets the patch_time of this Patches.


        :param patch_time: The patch_time of this Patches.  # noqa: E501
        :type: datetime
        """

        self._patch_time = patch_time

    @property
    def needs_approval(self):
        """Gets the needs_approval of this Patches.  # noqa: E501


        :return: The needs_approval of this Patches.  # noqa: E501
        :rtype: bool
        """
        return self._needs_approval

    @needs_approval.setter
    def needs_approval(self, needs_approval):
        """Sets the needs_approval of this Patches.


        :param needs_approval: The needs_approval of this Patches.  # noqa: E501
        :type: bool
        """

        self._needs_approval = needs_approval

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
        if issubclass(Patches, dict):
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
        if not isinstance(other, Patches):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other