# V1alpha1ResourceNode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.  +protobuf.options.marshal&#x3D;false +protobuf.as&#x3D;Timestamp +protobuf.options.(gogoproto.goproto_stringer)&#x3D;false | [optional] 
**health** | [**V1alpha1HealthStatus**](V1alpha1HealthStatus.md) |  | [optional] 
**images** | **[str]** |  | [optional] 
**info** | [**[V1alpha1InfoItem]**](V1alpha1InfoItem.md) |  | [optional] 
**networking_info** | [**V1alpha1ResourceNetworkingInfo**](V1alpha1ResourceNetworkingInfo.md) |  | [optional] 
**parent_refs** | [**[V1alpha1ResourceRef]**](V1alpha1ResourceRef.md) |  | [optional] 
**resource_ref** | [**V1alpha1ResourceRef**](V1alpha1ResourceRef.md) |  | [optional] 
**resource_version** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


