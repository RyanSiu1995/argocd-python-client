# V1alpha1Repository


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_state** | [**V1alpha1ConnectionState**](V1alpha1ConnectionState.md) |  | [optional] 
**enable_lfs** | **bool** | EnableLFS specifies whether git-lfs support should be enabled for this repo. Only valid for Git repositories. | [optional] 
**enable_oci** | **bool** |  | [optional] 
**github_app_enterprise_base_url** | **str** |  | [optional] 
**github_app_id** | **str** |  | [optional] 
**github_app_installation_id** | **str** |  | [optional] 
**github_app_private_key** | **str** |  | [optional] 
**inherited_creds** | **bool** |  | [optional] 
**insecure** | **bool** |  | [optional] 
**insecure_ignore_host_key** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**repo** | **str** |  | [optional] 
**ssh_private_key** | **str** | SSHPrivateKey contains the PEM data for authenticating at the repo server. Only used with Git repos. | [optional] 
**tls_client_cert_data** | **str** |  | [optional] 
**tls_client_cert_key** | **str** |  | [optional] 
**type** | **str** | Type specifies the type of the repo. Can be either \&quot;git\&quot; or \&quot;helm. \&quot;git\&quot; is assumed if empty or absent. | [optional] 
**username** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


