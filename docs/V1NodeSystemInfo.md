# V1NodeSystemInfo

NodeSystemInfo is a set of ids/uuids to uniquely identify the node.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** |  | [optional] 
**boot_id** | **str** | Boot ID reported by the node. | [optional] 
**container_runtime_version** | **str** | ContainerRuntime Version reported by the node through runtime remote API (e.g. docker://1.5.0). | [optional] 
**kernel_version** | **str** | Kernel Version reported by the node from &#39;uname -r&#39; (e.g. 3.16.0-0.bpo.4-amd64). | [optional] 
**kube_proxy_version** | **str** | KubeProxy Version reported by the node. | [optional] 
**kubelet_version** | **str** | Kubelet Version reported by the node. | [optional] 
**machine_id** | **str** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**os_image** | **str** | OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)). | [optional] 
**system_uuid** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


