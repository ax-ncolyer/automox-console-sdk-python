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
from automox_console_sdk.api.events_api import EventsApi  # noqa: E501
from automox_console_sdk.rest import ApiException


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self):
        self.api = EventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_events(self):
        """Test case for get_events

        Retrieve All Event Objects for the Authenticated User  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()