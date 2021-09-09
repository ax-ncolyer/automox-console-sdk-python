# ServerWithPolicies

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**os_version_id** | **int** |  | [optional] 
**server_group_id** | **int** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**instance_id** | **str** |  | [optional] 
**refresh_interval** | **int** |  | [optional] 
**last_update_time** | **str** |  | [optional] 
**last_refresh_time** | **str** |  | [optional] 
**uptime** | **int** |  | [optional] 
**needs_reboot** | **bool** |  | [optional] 
**timezone** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**create_time** | **datetime** |  | [optional] 
**os_version** | **str** |  | [optional] 
**os_name** | **str** |  | [optional] 
**os_family** | **str** |  | [optional] 
**ip_addrs** | **list[str]** |  | [optional] 
**ip_addrs_private** | **list[str]** |  | [optional] 
**hostname** | **str** |  | [optional] 
**patches** | **int** |  | [optional] 
**details** | [**ServerDetail**](ServerDetail.md) |  | [optional] 
**agent_version** | **str** |  | [optional] 
**custom_name** | **str** |  | [optional] 
**exception** | **bool** |  | [optional] 
**total_count** | **int** |  | [optional] 
**server_policies** | [**list[Policy]**](Policy.md) |  | [optional] 
**policy_status** | [**list[ServerPolicyStatus]**](ServerPolicyStatus.md) |  | [optional] 
**last_scan_failed** | **bool** |  | [optional] 
**pending** | **bool** |  | [optional] 
**compliant** | **bool** |  | [optional] 
**display_name** | **str** |  | [optional] 
**commands** | [**list[Command]**](Command.md) |  | [optional] 
**pending_patches** | **int** |  | [optional] 
**connected** | **bool** |  | [optional] 
**last_process_time** | **str** |  | [optional] 
**next_patch_time** | **str** |  | [optional] 
**notification_count** | **int** |  | [optional] 
**reboot_notification_count** | **int** |  | [optional] 
**patch_deferral_count** | **int** |  | [optional] 
**is_delayed_by_notification** | **bool** |  | [optional] 
**reboot_is_delayed_by_notification** | **bool** |  | [optional] 
**is_delayed_by_user** | **bool** |  | [optional] 
**reboot_is_delayed_by_user** | **bool** |  | [optional] 
**last_disconnect_time** | **datetime** |  | [optional] 
**needs_attention** | **bool** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**status** | [**DeviceStatus**](DeviceStatus.md) |  | [optional] 
**last_logged_in_user** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
