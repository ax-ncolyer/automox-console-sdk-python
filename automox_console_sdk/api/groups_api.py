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


class GroupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_server_group(self, o, **kwargs):  # noqa: E501
        """Creates a new server group.  # noqa: E501

        Creates a new server group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_server_group(o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID for the created group. (required)
        :param ServerGroupCreateOrUpdateRequest body:
        :return: ServerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_server_group_with_http_info(o, **kwargs)  # noqa: E501
        else:
            (data) = self.create_server_group_with_http_info(o, **kwargs)  # noqa: E501
            return data

    def create_server_group_with_http_info(self, o, **kwargs):  # noqa: E501
        """Creates a new server group.  # noqa: E501

        Creates a new server group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_server_group_with_http_info(o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID for the created group. (required)
        :param ServerGroupCreateOrUpdateRequest body:
        :return: ServerGroup
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
                    " to method create_server_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `create_server_group`")  # noqa: E501

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
            '/servergroups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServerGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_server_group(self, id, o, **kwargs):  # noqa: E501
        """Deletes a server group.  # noqa: E501

        **NOTE:** Any devices that belong to the deleted group will be moved to the organization's Default Group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_server_group(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Server Group ID for the specified group. (required)
        :param int o: Organization ID for the created group. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_server_group_with_http_info(id, o, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_server_group_with_http_info(id, o, **kwargs)  # noqa: E501
            return data

    def delete_server_group_with_http_info(self, id, o, **kwargs):  # noqa: E501
        """Deletes a server group.  # noqa: E501

        **NOTE:** Any devices that belong to the deleted group will be moved to the organization's Default Group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_server_group_with_http_info(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Server Group ID for the specified group. (required)
        :param int o: Organization ID for the created group. (required)
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
                    " to method delete_server_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_server_group`")  # noqa: E501
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `delete_server_group`")  # noqa: E501

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
            '/servergroups/{id}', 'DELETE',
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

    def get_server_group(self, id, o, **kwargs):  # noqa: E501
        """List Specific Group Object  # noqa: E501

        Returns a specific server group object for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_server_group(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Server Group ID for the specified group. (required)
        :param int o: Organization ID for the specified group. (required)
        :return: ServerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_server_group_with_http_info(id, o, **kwargs)  # noqa: E501
        else:
            (data) = self.get_server_group_with_http_info(id, o, **kwargs)  # noqa: E501
            return data

    def get_server_group_with_http_info(self, id, o, **kwargs):  # noqa: E501
        """List Specific Group Object  # noqa: E501

        Returns a specific server group object for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_server_group_with_http_info(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Server Group ID for the specified group. (required)
        :param int o: Organization ID for the specified group. (required)
        :return: ServerGroup
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
                    " to method get_server_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_server_group`")  # noqa: E501
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `get_server_group`")  # noqa: E501

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
            '/servergroups/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServerGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_server_groups(self, o, **kwargs):  # noqa: E501
        """List All Group Objects  # noqa: E501

        Retrieves all server group objects for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_server_groups(o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID for retrieving groups. (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :param int limit: A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :return: list[ServerGroup]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_server_groups_with_http_info(o, **kwargs)  # noqa: E501
        else:
            (data) = self.get_server_groups_with_http_info(o, **kwargs)  # noqa: E501
            return data

    def get_server_groups_with_http_info(self, o, **kwargs):  # noqa: E501
        """List All Group Objects  # noqa: E501

        Retrieves all server group objects for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_server_groups_with_http_info(o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID for retrieving groups. (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :param int limit: A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :return: list[ServerGroup]
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
                    " to method get_server_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `get_server_groups`")  # noqa: E501

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
            '/servergroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServerGroup]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_server_group(self, body, o, id, **kwargs):  # noqa: E501
        """Updates an existing server group.  # noqa: E501

        Updates server group settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_server_group(body, o, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ServerGroupCreateOrUpdateRequest body: (required)
        :param int o: Organization ID for the created group. (required)
        :param int id: Server Group ID for the specified group. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_server_group_with_http_info(body, o, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_server_group_with_http_info(body, o, id, **kwargs)  # noqa: E501
            return data

    def update_server_group_with_http_info(self, body, o, id, **kwargs):  # noqa: E501
        """Updates an existing server group.  # noqa: E501

        Updates server group settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_server_group_with_http_info(body, o, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ServerGroupCreateOrUpdateRequest body: (required)
        :param int o: Organization ID for the created group. (required)
        :param int id: Server Group ID for the specified group. (required)
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
                    " to method update_server_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_server_group`")  # noqa: E501
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `update_server_group`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_server_group`")  # noqa: E501

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
            '/servergroups/{id}', 'PUT',
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