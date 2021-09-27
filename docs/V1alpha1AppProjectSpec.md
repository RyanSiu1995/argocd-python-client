# V1alpha1AppProjectSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_resource_blacklist** | [**[V1GroupKind]**](V1GroupKind.md) |  | [optional] 
**cluster_resource_whitelist** | [**[V1GroupKind]**](V1GroupKind.md) |  | [optional] 
**description** | **str** |  | [optional] 
**destinations** | [**[V1alpha1ApplicationDestination]**](V1alpha1ApplicationDestination.md) |  | [optional] 
**namespace_resource_blacklist** | [**[V1GroupKind]**](V1GroupKind.md) |  | [optional] 
**namespace_resource_whitelist** | [**[V1GroupKind]**](V1GroupKind.md) |  | [optional] 
**orphaned_resources** | [**V1alpha1OrphanedResourcesMonitorSettings**](V1alpha1OrphanedResourcesMonitorSettings.md) |  | [optional] 
**roles** | [**[V1alpha1ProjectRole]**](V1alpha1ProjectRole.md) |  | [optional] 
**signature_keys** | [**[V1alpha1SignatureKey]**](V1alpha1SignatureKey.md) |  | [optional] 
**source_repos** | **[str]** |  | [optional] 
**sync_windows** | [**[V1alpha1SyncWindow]**](V1alpha1SyncWindow.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


