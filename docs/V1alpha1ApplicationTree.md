# V1alpha1ApplicationTree


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**[V1alpha1HostInfo]**](V1alpha1HostInfo.md) |  | [optional] 
**nodes** | [**[V1alpha1ResourceNode]**](V1alpha1ResourceNode.md) | Nodes contains list of nodes which either directly managed by the application and children of directly managed nodes. | [optional] 
**orphaned_nodes** | [**[V1alpha1ResourceNode]**](V1alpha1ResourceNode.md) | OrphanedNodes contains if or orphaned nodes: nodes which are not managed by the app but in the same namespace. List is populated only if orphaned resources enabled in app project. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


