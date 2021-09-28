# argocd_python_client.ProjectServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_service_create**](ProjectServiceApi.md#project_service_create) | **POST** /api/v1/projects | Create a new project
[**project_service_create_token**](ProjectServiceApi.md#project_service_create_token) | **POST** /api/v1/projects/{project}/roles/{role}/token | Create a new project token
[**project_service_delete**](ProjectServiceApi.md#project_service_delete) | **DELETE** /api/v1/projects/{name} | Delete deletes a project
[**project_service_delete_token**](ProjectServiceApi.md#project_service_delete_token) | **DELETE** /api/v1/projects/{project}/roles/{role}/token/{iat} | Delete a new project token
[**project_service_get**](ProjectServiceApi.md#project_service_get) | **GET** /api/v1/projects/{name} | Get returns a project by name
[**project_service_get_global_projects**](ProjectServiceApi.md#project_service_get_global_projects) | **GET** /api/v1/projects/{name}/globalprojects | Get returns a virtual project by name
[**project_service_get_sync_windows_state**](ProjectServiceApi.md#project_service_get_sync_windows_state) | **GET** /api/v1/projects/{name}/syncwindows | GetSchedulesState returns true if there are any active sync syncWindows
[**project_service_list**](ProjectServiceApi.md#project_service_list) | **GET** /api/v1/projects | List returns list of projects
[**project_service_list_events**](ProjectServiceApi.md#project_service_list_events) | **GET** /api/v1/projects/{name}/events | ListEvents returns a list of project events
[**project_service_update**](ProjectServiceApi.md#project_service_update) | **PUT** /api/v1/projects/{project.metadata.name} | Update updates a project


# **project_service_create**
> V1alpha1AppProject project_service_create(body)

Create a new project

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import project_service_api
from argocd_python_client.model.project_project_create_request import ProjectProjectCreateRequest
from argocd_python_client.model.v1alpha1_app_project import V1alpha1AppProject
from argocd_python_client.model.runtime_error import RuntimeError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_service_api.ProjectServiceApi(api_client)
    body = ProjectProjectCreateRequest(
        project=V1alpha1AppProject(
            metadata=V1ObjectMeta(
                annotations={
                    "key": "key_example",
                },
                cluster_name="cluster_name_example",
                creation_timestamp="creation_timestamp_example",
                deletion_grace_period_seconds="deletion_grace_period_seconds_example",
                deletion_timestamp="deletion_timestamp_example",
                finalizers=[
                    "finalizers_example",
                ],
                generate_name="generate_name_example",
                labels={
                    "key": "key_example",
                },
                managed_fields=[
                    V1ManagedFieldsEntry(
                        api_version="api_version_example",
                        fields_type="fields_type_example",
                        fields_v1=V1FieldsV1(
                            raw='YQ==',
                        ),
                        manager="manager_example",
                        operation="operation_example",
                        time="time_example",
                    ),
                ],
                name="name_example",
                namespace="namespace_example",
                owner_references=[
                    V1OwnerReference(
                        api_version="api_version_example",
                        block_owner_deletion=True,
                        controller=True,
                        kind="kind_example",
                        name="name_example",
                        uid="uid_example",
                    ),
                ],
                resource_version="resource_version_example",
                self_link="self_link_example",
                uid="uid_example",
            ),
            spec=V1alpha1AppProjectSpec(
                cluster_resource_blacklist=[
                    V1GroupKind(
                        group="group_example",
                        kind="kind_example",
                    ),
                ],
                cluster_resource_whitelist=[
                    V1GroupKind(
                        group="group_example",
                        kind="kind_example",
                    ),
                ],
                description="description_example",
                destinations=[
                    V1alpha1ApplicationDestination(
                        name="name_example",
                        namespace="namespace_example",
                        server="server_example",
                    ),
                ],
                namespace_resource_blacklist=[
                    V1GroupKind(
                        group="group_example",
                        kind="kind_example",
                    ),
                ],
                namespace_resource_whitelist=[
                    V1GroupKind(
                        group="group_example",
                        kind="kind_example",
                    ),
                ],
                orphaned_resources=V1alpha1OrphanedResourcesMonitorSettings(
                    ignore=[
                        V1alpha1OrphanedResourceKey(
                            group="group_example",
                            kind="kind_example",
                            name="name_example",
                        ),
                    ],
                    warn=True,
                ),
                roles=[
                    V1alpha1ProjectRole(
                        description="description_example",
                        groups=[
                            "groups_example",
                        ],
                        jwt_tokens=[
                            V1alpha1JWTToken(
                                exp="exp_example",
                                iat="iat_example",
                                id="id_example",
                            ),
                        ],
                        name="name_example",
                        policies=[
                            "policies_example",
                        ],
                    ),
                ],
                signature_keys=[
                    V1alpha1SignatureKey(
                        key_id="key_id_example",
                    ),
                ],
                source_repos=[
                    "source_repos_example",
                ],
                sync_windows=[
                    V1alpha1SyncWindow(
                        applications=[
                            "applications_example",
                        ],
                        clusters=[
                            "clusters_example",
                        ],
                        duration="duration_example",
                        kind="kind_example",
                        manual_sync=True,
                        namespaces=[
                            "namespaces_example",
                        ],
                        schedule="schedule_example",
                    ),
                ],
            ),
            status=V1alpha1AppProjectStatus(
                jwt_tokens_by_role={
                    "key": V1alpha1JWTTokens(
                        items=[
                            V1alpha1JWTToken(
                                exp="exp_example",
                                iat="iat_example",
                                id="id_example",
                            ),
                        ],
                    ),
                },
            ),
        ),
        upsert=True,
    ) # ProjectProjectCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new project
        api_response = api_instance.project_service_create(body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ProjectServiceApi->project_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectProjectCreateRequest**](ProjectProjectCreateRequest.md)|  |

### Return type

[**V1alpha1AppProject**](V1alpha1AppProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_create_token**
> ProjectProjectTokenResponse project_service_create_token(project, role, body)

Create a new project token

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import project_service_api
from argocd_python_client.model.project_project_token_response import ProjectProjectTokenResponse
from argocd_python_client.model.project_project_token_create_request import ProjectProjectTokenCreateRequest
from argocd_python_client.model.runtime_error import RuntimeError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_service_api.ProjectServiceApi(api_client)
    project = "project_example" # str | 
    role = "role_example" # str | 
    body = ProjectProjectTokenCreateRequest(
        description="description_example",
        expires_in="expires_in_example",
        id="id_example",
        project="project_example",
        role="role_example",
    ) # ProjectProjectTokenCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new project token
        api_response = api_instance.project_service_create_token(project, role, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ProjectServiceApi->project_service_create_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  |
 **role** | **str**|  |
 **body** | [**ProjectProjectTokenCreateRequest**](ProjectProjectTokenCreateRequest.md)|  |

### Return type

[**ProjectProjectTokenResponse**](ProjectProjectTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_delete**
> bool, date, datetime, dict, float, int, list, str, none_type project_service_delete(name)

Delete deletes a project

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import project_service_api
from argocd_python_client.model.runtime_error import RuntimeError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_service_api.ProjectServiceApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete deletes a project
        api_response = api_instance.project_service_delete(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ProjectServiceApi->project_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_delete_token**
> bool, date, datetime, dict, float, int, list, str, none_type project_service_delete_token(project, role, iat)

Delete a new project token

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import project_service_api
from argocd_python_client.model.runtime_error import RuntimeError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_service_api.ProjectServiceApi(api_client)
    project = "project_example" # str | 
    role = "role_example" # str | 
    iat = "iat_example" # str | 
    id = "id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a new project token
        api_response = api_instance.project_service_delete_token(project, role, iat)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ProjectServiceApi->project_service_delete_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a new project token
        api_response = api_instance.project_service_delete_token(project, role, iat, id=id)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ProjectServiceApi->project_service_delete_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  |
 **role** | **str**|  |
 **iat** | **str**|  |
 **id** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_get**
> V1alpha1AppProject project_service_get(name)

Get returns a project by name

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import project_service_api
from argocd_python_client.model.v1alpha1_app_project import V1alpha1AppProject
from argocd_python_client.model.runtime_error import RuntimeError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_service_api.ProjectServiceApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get returns a project by name
        api_response = api_instance.project_service_get(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ProjectServiceApi->project_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**V1alpha1AppProject**](V1alpha1AppProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_get_global_projects**
> ProjectGlobalProjectsResponse project_service_get_global_projects(name)

Get returns a virtual project by name

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import project_service_api
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.project_global_projects_response import ProjectGlobalProjectsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_service_api.ProjectServiceApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get returns a virtual project by name
        api_response = api_instance.project_service_get_global_projects(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ProjectServiceApi->project_service_get_global_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**ProjectGlobalProjectsResponse**](ProjectGlobalProjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_get_sync_windows_state**
> ProjectSyncWindowsResponse project_service_get_sync_windows_state(name)

GetSchedulesState returns true if there are any active sync syncWindows

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import project_service_api
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.project_sync_windows_response import ProjectSyncWindowsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_service_api.ProjectServiceApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # GetSchedulesState returns true if there are any active sync syncWindows
        api_response = api_instance.project_service_get_sync_windows_state(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ProjectServiceApi->project_service_get_sync_windows_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**ProjectSyncWindowsResponse**](ProjectSyncWindowsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_list**
> V1alpha1AppProjectList project_service_list()

List returns list of projects

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import project_service_api
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.v1alpha1_app_project_list import V1alpha1AppProjectList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_service_api.ProjectServiceApi(api_client)
    name = "name_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List returns list of projects
        api_response = api_instance.project_service_list(name=name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ProjectServiceApi->project_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional]

### Return type

[**V1alpha1AppProjectList**](V1alpha1AppProjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_list_events**
> V1EventList project_service_list_events(name)

ListEvents returns a list of project events

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import project_service_api
from argocd_python_client.model.v1_event_list import V1EventList
from argocd_python_client.model.runtime_error import RuntimeError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_service_api.ProjectServiceApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # ListEvents returns a list of project events
        api_response = api_instance.project_service_list_events(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ProjectServiceApi->project_service_list_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**V1EventList**](V1EventList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_update**
> V1alpha1AppProject project_service_update(project_metadata_name, body)

Update updates a project

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import project_service_api
from argocd_python_client.model.v1alpha1_app_project import V1alpha1AppProject
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.project_project_update_request import ProjectProjectUpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_service_api.ProjectServiceApi(api_client)
    project_metadata_name = "project.metadata.name_example" # str | Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional
    body = ProjectProjectUpdateRequest(
        project=V1alpha1AppProject(
            metadata=V1ObjectMeta(
                annotations={
                    "key": "key_example",
                },
                cluster_name="cluster_name_example",
                creation_timestamp="creation_timestamp_example",
                deletion_grace_period_seconds="deletion_grace_period_seconds_example",
                deletion_timestamp="deletion_timestamp_example",
                finalizers=[
                    "finalizers_example",
                ],
                generate_name="generate_name_example",
                labels={
                    "key": "key_example",
                },
                managed_fields=[
                    V1ManagedFieldsEntry(
                        api_version="api_version_example",
                        fields_type="fields_type_example",
                        fields_v1=V1FieldsV1(
                            raw='YQ==',
                        ),
                        manager="manager_example",
                        operation="operation_example",
                        time="time_example",
                    ),
                ],
                name="name_example",
                namespace="namespace_example",
                owner_references=[
                    V1OwnerReference(
                        api_version="api_version_example",
                        block_owner_deletion=True,
                        controller=True,
                        kind="kind_example",
                        name="name_example",
                        uid="uid_example",
                    ),
                ],
                resource_version="resource_version_example",
                self_link="self_link_example",
                uid="uid_example",
            ),
            spec=V1alpha1AppProjectSpec(
                cluster_resource_blacklist=[
                    V1GroupKind(
                        group="group_example",
                        kind="kind_example",
                    ),
                ],
                cluster_resource_whitelist=[
                    V1GroupKind(
                        group="group_example",
                        kind="kind_example",
                    ),
                ],
                description="description_example",
                destinations=[
                    V1alpha1ApplicationDestination(
                        name="name_example",
                        namespace="namespace_example",
                        server="server_example",
                    ),
                ],
                namespace_resource_blacklist=[
                    V1GroupKind(
                        group="group_example",
                        kind="kind_example",
                    ),
                ],
                namespace_resource_whitelist=[
                    V1GroupKind(
                        group="group_example",
                        kind="kind_example",
                    ),
                ],
                orphaned_resources=V1alpha1OrphanedResourcesMonitorSettings(
                    ignore=[
                        V1alpha1OrphanedResourceKey(
                            group="group_example",
                            kind="kind_example",
                            name="name_example",
                        ),
                    ],
                    warn=True,
                ),
                roles=[
                    V1alpha1ProjectRole(
                        description="description_example",
                        groups=[
                            "groups_example",
                        ],
                        jwt_tokens=[
                            V1alpha1JWTToken(
                                exp="exp_example",
                                iat="iat_example",
                                id="id_example",
                            ),
                        ],
                        name="name_example",
                        policies=[
                            "policies_example",
                        ],
                    ),
                ],
                signature_keys=[
                    V1alpha1SignatureKey(
                        key_id="key_id_example",
                    ),
                ],
                source_repos=[
                    "source_repos_example",
                ],
                sync_windows=[
                    V1alpha1SyncWindow(
                        applications=[
                            "applications_example",
                        ],
                        clusters=[
                            "clusters_example",
                        ],
                        duration="duration_example",
                        kind="kind_example",
                        manual_sync=True,
                        namespaces=[
                            "namespaces_example",
                        ],
                        schedule="schedule_example",
                    ),
                ],
            ),
            status=V1alpha1AppProjectStatus(
                jwt_tokens_by_role={
                    "key": V1alpha1JWTTokens(
                        items=[
                            V1alpha1JWTToken(
                                exp="exp_example",
                                iat="iat_example",
                                id="id_example",
                            ),
                        ],
                    ),
                },
            ),
        ),
    ) # ProjectProjectUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update updates a project
        api_response = api_instance.project_service_update(project_metadata_name, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ProjectServiceApi->project_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_metadata_name** | **str**| Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional |
 **body** | [**ProjectProjectUpdateRequest**](ProjectProjectUpdateRequest.md)|  |

### Return type

[**V1alpha1AppProject**](V1alpha1AppProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

