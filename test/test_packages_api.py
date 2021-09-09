# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-08-10
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import automox_console_sdk
from automox_console_sdk.api.packages_api import PackagesApi  # noqa: E501
from automox_console_sdk.rest import ApiException


class TestPackagesApi(unittest.TestCase):
    """PackagesApi unit test stubs"""

    def setUp(self):
        self.api = PackagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_device_packages(self):
        """Test case for get_device_packages

        List Software Packages for Specific Device  # noqa: E501
        """
        pass

    def test_get_organization_packages(self):
        """Test case for get_organization_packages

        List All Software Packages for All Devices  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()