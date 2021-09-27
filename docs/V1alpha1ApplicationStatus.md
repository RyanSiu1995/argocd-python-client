# V1alpha1ApplicationStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**[V1alpha1ApplicationCondition]**](V1alpha1ApplicationCondition.md) |  | [optional] 
**health** | [**V1alpha1HealthStatus**](V1alpha1HealthStatus.md) |  | [optional] 
**history** | [**[V1alpha1RevisionHistory]**](V1alpha1RevisionHistory.md) |  | [optional] 
**observed_at** | [**V1Time**](V1Time.md) |  | [optional] 
**operation_state** | [**V1alpha1OperationState**](V1alpha1OperationState.md) |  | [optional] 
**reconciled_at** | [**V1Time**](V1Time.md) |  | [optional] 
**resources** | [**[V1alpha1ResourceStatus]**](V1alpha1ResourceStatus.md) |  | [optional] 
**source_type** | **str** |  | [optional] 
**summary** | [**V1alpha1ApplicationSummary**](V1alpha1ApplicationSummary.md) |  | [optional] 
**sync** | [**V1alpha1SyncStatus**](V1alpha1SyncStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


