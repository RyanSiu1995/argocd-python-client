# argocd_python_client.ClusterServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_service_create**](ClusterServiceApi.md#cluster_service_create) | **POST** /api/v1/clusters | Create creates a cluster
[**cluster_service_delete**](ClusterServiceApi.md#cluster_service_delete) | **DELETE** /api/v1/clusters/{server} | Delete deletes a cluster
[**cluster_service_get**](ClusterServiceApi.md#cluster_service_get) | **GET** /api/v1/clusters/{server} | Get returns a cluster by server address
[**cluster_service_invalidate_cache**](ClusterServiceApi.md#cluster_service_invalidate_cache) | **POST** /api/v1/clusters/{server}/invalidate-cache | InvalidateCache invalidates cluster cache
[**cluster_service_list**](ClusterServiceApi.md#cluster_service_list) | **GET** /api/v1/clusters | List returns list of clusters
[**cluster_service_rotate_auth**](ClusterServiceApi.md#cluster_service_rotate_auth) | **POST** /api/v1/clusters/{server}/rotate-auth | RotateAuth rotates the bearer token used for a cluster
[**cluster_service_update**](ClusterServiceApi.md#cluster_service_update) | **PUT** /api/v1/clusters/{cluster.server} | Update updates a cluster


# **cluster_service_create**
> V1alpha1Cluster cluster_service_create(body)

Create creates a cluster

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import cluster_service_api
from argocd_python_client.model.v1alpha1_cluster import V1alpha1Cluster
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
    api_instance = cluster_service_api.ClusterServiceApi(api_client)
    body = V1alpha1Cluster(
        config=V1alpha1ClusterConfig(
            aws_auth_config=V1alpha1AWSAuthConfig(
                cluster_name="cluster_name_example",
                role_arn="role_arn_example",
            ),
            bearer_token="bearer_token_example",
            exec_provider_config=V1alpha1ExecProviderConfig(
                api_version="api_version_example",
                args=[
                    "args_example",
                ],
                command="command_example",
                env={
                    "key": "key_example",
                },
                install_hint="install_hint_example",
            ),
            password="password_example",
            tls_client_config=V1alpha1TLSClientConfig(
                ca_data='YQ==',
                cert_data='YQ==',
                insecure=True,
                key_data='YQ==',
                server_name="server_name_example",
            ),
            username="username_example",
        ),
        connection_state=V1alpha1ConnectionState(
            attempted_at="attempted_at_example",
            message="message_example",
            status="status_example",
        ),
        info=V1alpha1ClusterInfo(
            applications_count="applications_count_example",
            cache_info=V1alpha1ClusterCacheInfo(
                apis_count="apis_count_example",
                last_cache_sync_time="last_cache_sync_time_example",
                resources_count="resources_count_example",
            ),
            connection_state=V1alpha1ConnectionState(
                attempted_at="attempted_at_example",
                message="message_example",
                status="status_example",
            ),
            server_version="server_version_example",
        ),
        name="name_example",
        namespaces=[
            "namespaces_example",
        ],
        refresh_requested_at="refresh_requested_at_example",
        server="server_example",
        server_version="server_version_example",
        shard="shard_example",
    ) # V1alpha1Cluster | 
    upsert = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create creates a cluster
        api_response = api_instance.cluster_service_create(body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ClusterServiceApi->cluster_service_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create creates a cluster
        api_response = api_instance.cluster_service_create(body, upsert=upsert)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ClusterServiceApi->cluster_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1Cluster**](V1alpha1Cluster.md)|  |
 **upsert** | **bool**|  | [optional]

### Return type

[**V1alpha1Cluster**](V1alpha1Cluster.md)

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

# **cluster_service_delete**
> bool, date, datetime, dict, float, int, list, str, none_type cluster_service_delete(server)

Delete deletes a cluster

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import cluster_service_api
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
    api_instance = cluster_service_api.ClusterServiceApi(api_client)
    server = "server_example" # str | 
    name = "name_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete deletes a cluster
        api_response = api_instance.cluster_service_delete(server)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ClusterServiceApi->cluster_service_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete deletes a cluster
        api_response = api_instance.cluster_service_delete(server, name=name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ClusterServiceApi->cluster_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**|  |
 **name** | **str**|  | [optional]

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

# **cluster_service_get**
> V1alpha1Cluster cluster_service_get(server)

Get returns a cluster by server address

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import cluster_service_api
from argocd_python_client.model.v1alpha1_cluster import V1alpha1Cluster
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
    api_instance = cluster_service_api.ClusterServiceApi(api_client)
    server = "server_example" # str | 
    name = "name_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get returns a cluster by server address
        api_response = api_instance.cluster_service_get(server)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ClusterServiceApi->cluster_service_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get returns a cluster by server address
        api_response = api_instance.cluster_service_get(server, name=name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ClusterServiceApi->cluster_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**|  |
 **name** | **str**|  | [optional]

### Return type

[**V1alpha1Cluster**](V1alpha1Cluster.md)

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

# **cluster_service_invalidate_cache**
> V1alpha1Cluster cluster_service_invalidate_cache(server)

InvalidateCache invalidates cluster cache

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import cluster_service_api
from argocd_python_client.model.v1alpha1_cluster import V1alpha1Cluster
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
    api_instance = cluster_service_api.ClusterServiceApi(api_client)
    server = "server_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # InvalidateCache invalidates cluster cache
        api_response = api_instance.cluster_service_invalidate_cache(server)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ClusterServiceApi->cluster_service_invalidate_cache: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**|  |

### Return type

[**V1alpha1Cluster**](V1alpha1Cluster.md)

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

# **cluster_service_list**
> V1alpha1ClusterList cluster_service_list()

List returns list of clusters

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import cluster_service_api
from argocd_python_client.model.v1alpha1_cluster_list import V1alpha1ClusterList
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
    api_instance = cluster_service_api.ClusterServiceApi(api_client)
    server = "server_example" # str |  (optional)
    name = "name_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List returns list of clusters
        api_response = api_instance.cluster_service_list(server=server, name=name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ClusterServiceApi->cluster_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**|  | [optional]
 **name** | **str**|  | [optional]

### Return type

[**V1alpha1ClusterList**](V1alpha1ClusterList.md)

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

# **cluster_service_rotate_auth**
> bool, date, datetime, dict, float, int, list, str, none_type cluster_service_rotate_auth(server)

RotateAuth rotates the bearer token used for a cluster

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import cluster_service_api
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
    api_instance = cluster_service_api.ClusterServiceApi(api_client)
    server = "server_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # RotateAuth rotates the bearer token used for a cluster
        api_response = api_instance.cluster_service_rotate_auth(server)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ClusterServiceApi->cluster_service_rotate_auth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**|  |

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

# **cluster_service_update**
> V1alpha1Cluster cluster_service_update(cluster_server, body)

Update updates a cluster

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import cluster_service_api
from argocd_python_client.model.v1alpha1_cluster import V1alpha1Cluster
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
    api_instance = cluster_service_api.ClusterServiceApi(api_client)
    cluster_server = "cluster.server_example" # str | Server is the API server URL of the Kubernetes cluster
    body = V1alpha1Cluster(
        config=V1alpha1ClusterConfig(
            aws_auth_config=V1alpha1AWSAuthConfig(
                cluster_name="cluster_name_example",
                role_arn="role_arn_example",
            ),
            bearer_token="bearer_token_example",
            exec_provider_config=V1alpha1ExecProviderConfig(
                api_version="api_version_example",
                args=[
                    "args_example",
                ],
                command="command_example",
                env={
                    "key": "key_example",
                },
                install_hint="install_hint_example",
            ),
            password="password_example",
            tls_client_config=V1alpha1TLSClientConfig(
                ca_data='YQ==',
                cert_data='YQ==',
                insecure=True,
                key_data='YQ==',
                server_name="server_name_example",
            ),
            username="username_example",
        ),
        connection_state=V1alpha1ConnectionState(
            attempted_at="attempted_at_example",
            message="message_example",
            status="status_example",
        ),
        info=V1alpha1ClusterInfo(
            applications_count="applications_count_example",
            cache_info=V1alpha1ClusterCacheInfo(
                apis_count="apis_count_example",
                last_cache_sync_time="last_cache_sync_time_example",
                resources_count="resources_count_example",
            ),
            connection_state=V1alpha1ConnectionState(
                attempted_at="attempted_at_example",
                message="message_example",
                status="status_example",
            ),
            server_version="server_version_example",
        ),
        name="name_example",
        namespaces=[
            "namespaces_example",
        ],
        refresh_requested_at="refresh_requested_at_example",
        server="server_example",
        server_version="server_version_example",
        shard="shard_example",
    ) # V1alpha1Cluster | 
    updated_fields = [
        "updatedFields_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update updates a cluster
        api_response = api_instance.cluster_service_update(cluster_server, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ClusterServiceApi->cluster_service_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update updates a cluster
        api_response = api_instance.cluster_service_update(cluster_server, body, updated_fields=updated_fields)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ClusterServiceApi->cluster_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_server** | **str**| Server is the API server URL of the Kubernetes cluster |
 **body** | [**V1alpha1Cluster**](V1alpha1Cluster.md)|  |
 **updated_fields** | **[str]**|  | [optional]

### Return type

[**V1alpha1Cluster**](V1alpha1Cluster.md)

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

