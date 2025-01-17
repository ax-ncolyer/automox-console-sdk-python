# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-09-01
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from automox_console_sdk.api_client import ApiClient


class PoliciesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_policy(self, o, **kwargs):  # noqa: E501
        """Create a New Policy  # noqa: E501

        Creates a new policy for a specified organization. For more info on filter types and scheduling, see [Policy and Device Filters, and Scheduling](/developer-portal/policy_filters_schedule).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_policy(o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID for the specified policy. (required)
        :param PoliciesBody body:
        :return: list[Policy]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_policy_with_http_info(o, **kwargs)  # noqa: E501
        else:
            (data) = self.create_policy_with_http_info(o, **kwargs)  # noqa: E501
            return data

    def create_policy_with_http_info(self, o, **kwargs):  # noqa: E501
        """Create a New Policy  # noqa: E501

        Creates a new policy for a specified organization. For more info on filter types and scheduling, see [Policy and Device Filters, and Scheduling](/developer-portal/policy_filters_schedule).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_policy_with_http_info(o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID for the specified policy. (required)
        :param PoliciesBody body:
        :return: list[Policy]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['o', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `create_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/policies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Policy]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_policy(self, id, o, **kwargs):  # noqa: E501
        """Delete Specific Policy Object  # noqa: E501

        Deletes a specific policy object for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_policy(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Policy ID for the specified policy (required)
        :param int o: Organization ID for the specified policy (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_policy_with_http_info(id, o, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_policy_with_http_info(id, o, **kwargs)  # noqa: E501
            return data

    def delete_policy_with_http_info(self, id, o, **kwargs):  # noqa: E501
        """Delete Specific Policy Object  # noqa: E501

        Deletes a specific policy object for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_policy_with_http_info(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Policy ID for the specified policy (required)
        :param int o: Organization ID for the specified policy (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'o']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_policy`")  # noqa: E501
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `delete_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def execute_policy(self, id, o, action, **kwargs):  # noqa: E501
        """Schedule a Policy for Immediate Remediation  # noqa: E501

        Schedule a policy for immediate remediation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execute_policy(id, o, action, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Policy ID for the specified policy (required)
        :param int o: Organization ID for the specified policy (required)
        :param str action: Specify the action to be taken. Possible values: `remediateAll`, `remediateServer` Format: `action=remediateServer` (required)
        :param int server_id: Specify the specific Server to run the policy for. Only applicable when action is set to \"remediateServer\" Format: serverId=123456
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.execute_policy_with_http_info(id, o, action, **kwargs)  # noqa: E501
        else:
            (data) = self.execute_policy_with_http_info(id, o, action, **kwargs)  # noqa: E501
            return data

    def execute_policy_with_http_info(self, id, o, action, **kwargs):  # noqa: E501
        """Schedule a Policy for Immediate Remediation  # noqa: E501

        Schedule a policy for immediate remediation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execute_policy_with_http_info(id, o, action, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Policy ID for the specified policy (required)
        :param int o: Organization ID for the specified policy (required)
        :param str action: Specify the action to be taken. Possible values: `remediateAll`, `remediateServer` Format: `action=remediateServer` (required)
        :param int server_id: Specify the specific Server to run the policy for. Only applicable when action is set to \"remediateServer\" Format: serverId=123456
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'o', 'action', 'server_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method execute_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `execute_policy`")  # noqa: E501
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `execute_policy`")  # noqa: E501
        # verify the required parameter 'action' is set
        if ('action' not in params or
                params['action'] is None):
            raise ValueError("Missing the required parameter `action` when calling `execute_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501
        if 'action' in params:
            query_params.append(('action', params['action']))  # noqa: E501
        if 'server_id' in params:
            query_params.append(('serverId', params['server_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def generate_policy_device_filter_preview(self, body, o, **kwargs):  # noqa: E501
        """Policy Device Filters Preview  # noqa: E501

        Generate a preview of the list of devices that matches the provided device filter set. For more information, see [Policy and Device Filters, and Scheduling](/developer-portal/policy_filters_schedule).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_policy_device_filter_preview(body, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PolicyDeviceFiltersPreview body: (required)
        :param int o: Organization ID. If omitted, results will include all organizations for the authenticated user. (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :param int limit: A limit on the number of results to be returned, between 1 and 200 with a default of 25. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :return: list[PolicyDeviceFiltersOutput]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_policy_device_filter_preview_with_http_info(body, o, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_policy_device_filter_preview_with_http_info(body, o, **kwargs)  # noqa: E501
            return data

    def generate_policy_device_filter_preview_with_http_info(self, body, o, **kwargs):  # noqa: E501
        """Policy Device Filters Preview  # noqa: E501

        Generate a preview of the list of devices that matches the provided device filter set. For more information, see [Policy and Device Filters, and Scheduling](/developer-portal/policy_filters_schedule).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_policy_device_filter_preview_with_http_info(body, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PolicyDeviceFiltersPreview body: (required)
        :param int o: Organization ID. If omitted, results will include all organizations for the authenticated user. (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :param int limit: A limit on the number of results to be returned, between 1 and 200 with a default of 25. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :return: list[PolicyDeviceFiltersOutput]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'o', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_policy_device_filter_preview" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `generate_policy_device_filter_preview`")  # noqa: E501
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `generate_policy_device_filter_preview`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/policies/device-filters-preview', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PolicyDeviceFiltersOutput]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_policies(self, o, **kwargs):  # noqa: E501
        """List All Policy Objects  # noqa: E501

        Retrieves a list of all policy objects for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policies(o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID for retrieving policies (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :param int limit: A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :return: list[Policy]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_policies_with_http_info(o, **kwargs)  # noqa: E501
        else:
            (data) = self.get_policies_with_http_info(o, **kwargs)  # noqa: E501
            return data

    def get_policies_with_http_info(self, o, **kwargs):  # noqa: E501
        """List All Policy Objects  # noqa: E501

        Retrieves a list of all policy objects for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policies_with_http_info(o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID for retrieving policies (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :param int limit: A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :return: list[Policy]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['o', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `get_policies`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Policy]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_policy(self, id, o, **kwargs):  # noqa: E501
        """List Specific Policy Object  # noqa: E501

        Returns a specific policy object for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Policy ID for the specified policy (required)
        :param int o: Organization ID for the specified policy (required)
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_policy_with_http_info(id, o, **kwargs)  # noqa: E501
        else:
            (data) = self.get_policy_with_http_info(id, o, **kwargs)  # noqa: E501
            return data

    def get_policy_with_http_info(self, id, o, **kwargs):  # noqa: E501
        """List Specific Policy Object  # noqa: E501

        Returns a specific policy object for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy_with_http_info(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Policy ID for the specified policy (required)
        :param int o: Organization ID for the specified policy (required)
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'o']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_policy`")  # noqa: E501
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `get_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Policy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_policy_stats(self, o, **kwargs):  # noqa: E501
        """List Policy Compliance Stats  # noqa: E501

        Retrieve policy compliance statistics for all policies.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy_stats(o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID for retrieving policy stats. Omit this to retrieve stats for policies in all organizations that the authenticated user can access (required)
        :return: list[PolicyStats]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_policy_stats_with_http_info(o, **kwargs)  # noqa: E501
        else:
            (data) = self.get_policy_stats_with_http_info(o, **kwargs)  # noqa: E501
            return data

    def get_policy_stats_with_http_info(self, o, **kwargs):  # noqa: E501
        """List Policy Compliance Stats  # noqa: E501

        Retrieve policy compliance statistics for all policies.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy_stats_with_http_info(o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID for retrieving policy stats. Omit this to retrieve stats for policies in all organizations that the authenticated user can access (required)
        :return: list[PolicyStats]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['o']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `get_policy_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/policystats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PolicyStats]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_policy(self, body, o, id, **kwargs):  # noqa: E501
        """Updates a specific policy object for the authenticated user.  # noqa: E501

        Updates a specific policy object for the authenticated user. For more info on filter types and scheduling, see [Policy and Device Filters, and Scheduling](/developer-portal/policy_filters_schedule).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_policy(body, o, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Policy body: (required)
        :param int o: Organization ID for the specified policy (required)
        :param int id: Policy ID for the specified policy (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_policy_with_http_info(body, o, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_policy_with_http_info(body, o, id, **kwargs)  # noqa: E501
            return data

    def update_policy_with_http_info(self, body, o, id, **kwargs):  # noqa: E501
        """Updates a specific policy object for the authenticated user.  # noqa: E501

        Updates a specific policy object for the authenticated user. For more info on filter types and scheduling, see [Policy and Device Filters, and Scheduling](/developer-portal/policy_filters_schedule).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_policy_with_http_info(body, o, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Policy body: (required)
        :param int o: Organization ID for the specified policy (required)
        :param int id: Policy ID for the specified policy (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'o', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_policy`")  # noqa: E501
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `update_policy`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
