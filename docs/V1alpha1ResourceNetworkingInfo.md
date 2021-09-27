# V1alpha1ResourceNetworkingInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_urls** | **[str]** | ExternalURLs holds list of URLs which should be available externally. List is populated for ingress resources using rules hostnames. | [optional] 
**ingress** | [**[V1LoadBalancerIngress]**](V1LoadBalancerIngress.md) |  | [optional] 
**labels** | **{str: (str,)}** |  | [optional] 
**target_labels** | **{str: (str,)}** |  | [optional] 
**target_refs** | [**[V1alpha1ResourceRef]**](V1alpha1ResourceRef.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


