# V1alpha1SyncOperation

SyncOperation contains details about a sync operation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  | [optional] 
**manifests** | **[str]** |  | [optional] 
**prune** | **bool** |  | [optional] 
**resources** | [**[V1alpha1SyncOperationResource]**](V1alpha1SyncOperationResource.md) |  | [optional] 
**revision** | **str** | Revision is the revision (Git) or chart version (Helm) which to sync the application to If omitted, will use the revision specified in app spec. | [optional] 
**source** | [**V1alpha1ApplicationSource**](V1alpha1ApplicationSource.md) |  | [optional] 
**sync_options** | **[str]** |  | [optional] 
**sync_strategy** | [**V1alpha1SyncStrategy**](V1alpha1SyncStrategy.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


