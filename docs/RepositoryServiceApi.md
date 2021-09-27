# argocd_python_client.RepositoryServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repository_service_create_repository**](RepositoryServiceApi.md#repository_service_create_repository) | **POST** /api/v1/repositories | CreateRepository creates a new repository configuration
[**repository_service_delete_repository**](RepositoryServiceApi.md#repository_service_delete_repository) | **DELETE** /api/v1/repositories/{repo} | DeleteRepository deletes a repository from the configuration
[**repository_service_get**](RepositoryServiceApi.md#repository_service_get) | **GET** /api/v1/repositories/{repo} | Get returns a repository or its credentials
[**repository_service_get_app_details**](RepositoryServiceApi.md#repository_service_get_app_details) | **POST** /api/v1/repositories/{source.repoURL}/appdetails | GetAppDetails returns application details by given path
[**repository_service_get_helm_charts**](RepositoryServiceApi.md#repository_service_get_helm_charts) | **GET** /api/v1/repositories/{repo}/helmcharts | GetHelmCharts returns list of helm charts in the specified repository
[**repository_service_list_apps**](RepositoryServiceApi.md#repository_service_list_apps) | **GET** /api/v1/repositories/{repo}/apps | ListApps returns list of apps in the repe
[**repository_service_list_refs**](RepositoryServiceApi.md#repository_service_list_refs) | **GET** /api/v1/repositories/{repo}/refs | 
[**repository_service_list_repositories**](RepositoryServiceApi.md#repository_service_list_repositories) | **GET** /api/v1/repositories | ListRepositories gets a list of all configured repositories
[**repository_service_update_repository**](RepositoryServiceApi.md#repository_service_update_repository) | **PUT** /api/v1/repositories/{repo.repo} | UpdateRepository updates a repository configuration
[**repository_service_validate_access**](RepositoryServiceApi.md#repository_service_validate_access) | **POST** /api/v1/repositories/{repo}/validate | ValidateAccess validates access to a repository with given parameters


# **repository_service_create_repository**
> V1alpha1Repository repository_service_create_repository(body)

CreateRepository creates a new repository configuration

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import repository_service_api
from argocd_python_client.model.v1alpha1_repository import V1alpha1Repository
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
    api_instance = repository_service_api.RepositoryServiceApi(api_client)
    body = V1alpha1Repository(
        connection_state=V1alpha1ConnectionState(
            attempted_at=V1Time(
                nanos=1,
                seconds="seconds_example",
            ),
            message="message_example",
            status="status_example",
        ),
        enable_lfs=True,
        enable_oci=True,
        github_app_enterprise_base_url="github_app_enterprise_base_url_example",
        github_app_id="github_app_id_example",
        github_app_installation_id="github_app_installation_id_example",
        github_app_private_key="github_app_private_key_example",
        inherited_creds=True,
        insecure=True,
        insecure_ignore_host_key=True,
        name="name_example",
        password="password_example",
        repo="repo_example",
        ssh_private_key="ssh_private_key_example",
        tls_client_cert_data="tls_client_cert_data_example",
        tls_client_cert_key="tls_client_cert_key_example",
        type="type_example",
        username="username_example",
    ) # V1alpha1Repository | Repository definition
    upsert = True # bool | Whether to create in upsert mode. (optional)
    creds_only = True # bool | Whether to operate on credential set instead of repository. (optional)

    # example passing only required values which don't have defaults set
    try:
        # CreateRepository creates a new repository configuration
        api_response = api_instance.repository_service_create_repository(body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_create_repository: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # CreateRepository creates a new repository configuration
        api_response = api_instance.repository_service_create_repository(body, upsert=upsert, creds_only=creds_only)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_create_repository: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1Repository**](V1alpha1Repository.md)| Repository definition |
 **upsert** | **bool**| Whether to create in upsert mode. | [optional]
 **creds_only** | **bool**| Whether to operate on credential set instead of repository. | [optional]

### Return type

[**V1alpha1Repository**](V1alpha1Repository.md)

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

# **repository_service_delete_repository**
> bool, date, datetime, dict, float, int, list, str, none_type repository_service_delete_repository(repo)

DeleteRepository deletes a repository from the configuration

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import repository_service_api
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
    api_instance = repository_service_api.RepositoryServiceApi(api_client)
    repo = "repo_example" # str | Repo URL for query
    force_refresh = True # bool | Whether to force a cache refresh on repo's connection state. (optional)

    # example passing only required values which don't have defaults set
    try:
        # DeleteRepository deletes a repository from the configuration
        api_response = api_instance.repository_service_delete_repository(repo)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_delete_repository: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DeleteRepository deletes a repository from the configuration
        api_response = api_instance.repository_service_delete_repository(repo, force_refresh=force_refresh)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_delete_repository: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query |
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#39;s connection state. | [optional]

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

# **repository_service_get**
> V1alpha1Repository repository_service_get(repo)

Get returns a repository or its credentials

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import repository_service_api
from argocd_python_client.model.v1alpha1_repository import V1alpha1Repository
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
    api_instance = repository_service_api.RepositoryServiceApi(api_client)
    repo = "repo_example" # str | Repo URL for query
    force_refresh = True # bool | Whether to force a cache refresh on repo's connection state. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get returns a repository or its credentials
        api_response = api_instance.repository_service_get(repo)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get returns a repository or its credentials
        api_response = api_instance.repository_service_get(repo, force_refresh=force_refresh)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query |
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#39;s connection state. | [optional]

### Return type

[**V1alpha1Repository**](V1alpha1Repository.md)

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

# **repository_service_get_app_details**
> RepositoryRepoAppDetailsResponse repository_service_get_app_details(source_repo_url, body)

GetAppDetails returns application details by given path

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import repository_service_api
from argocd_python_client.model.repository_repo_app_details_query import RepositoryRepoAppDetailsQuery
from argocd_python_client.model.repository_repo_app_details_response import RepositoryRepoAppDetailsResponse
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
    api_instance = repository_service_api.RepositoryServiceApi(api_client)
    source_repo_url = "source.repoURL_example" # str | RepoURL is the URL to the repository (Git or Helm) that contains the application manifests
    body = RepositoryRepoAppDetailsQuery(
        app_name="app_name_example",
        source=V1alpha1ApplicationSource(
            chart="chart_example",
            directory=V1alpha1ApplicationSourceDirectory(
                exclude="exclude_example",
                include="include_example",
                jsonnet=V1alpha1ApplicationSourceJsonnet(
                    ext_vars=[
                        V1alpha1JsonnetVar(
                            code=True,
                            name="name_example",
                            value="value_example",
                        ),
                    ],
                    libs=[
                        "libs_example",
                    ],
                    tlas=[
                        V1alpha1JsonnetVar(
                            code=True,
                            name="name_example",
                            value="value_example",
                        ),
                    ],
                ),
                recurse=True,
            ),
            helm=V1alpha1ApplicationSourceHelm(
                file_parameters=[
                    V1alpha1HelmFileParameter(
                        name="name_example",
                        path="path_example",
                    ),
                ],
                parameters=[
                    V1alpha1HelmParameter(
                        force_string=True,
                        name="name_example",
                        value="value_example",
                    ),
                ],
                release_name="release_name_example",
                value_files=[
                    "value_files_example",
                ],
                values="values_example",
                version="version_example",
            ),
            ksonnet=V1alpha1ApplicationSourceKsonnet(
                environment="environment_example",
                parameters=[
                    V1alpha1KsonnetParameter(
                        component="component_example",
                        name="name_example",
                        value="value_example",
                    ),
                ],
            ),
            kustomize=V1alpha1ApplicationSourceKustomize(
                common_annotations={
                    "key": "key_example",
                },
                common_labels={
                    "key": "key_example",
                },
                images=[
                    "images_example",
                ],
                name_prefix="name_prefix_example",
                name_suffix="name_suffix_example",
                version="version_example",
            ),
            path="path_example",
            plugin=V1alpha1ApplicationSourcePlugin(
                env=[
                    Applicationv1alpha1EnvEntry(
                        name="name_example",
                        value="value_example",
                    ),
                ],
                name="name_example",
            ),
            repo_url="repo_url_example",
            target_revision="target_revision_example",
        ),
    ) # RepositoryRepoAppDetailsQuery | 

    # example passing only required values which don't have defaults set
    try:
        # GetAppDetails returns application details by given path
        api_response = api_instance.repository_service_get_app_details(source_repo_url, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_get_app_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_repo_url** | **str**| RepoURL is the URL to the repository (Git or Helm) that contains the application manifests |
 **body** | [**RepositoryRepoAppDetailsQuery**](RepositoryRepoAppDetailsQuery.md)|  |

### Return type

[**RepositoryRepoAppDetailsResponse**](RepositoryRepoAppDetailsResponse.md)

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

# **repository_service_get_helm_charts**
> RepositoryHelmChartsResponse repository_service_get_helm_charts(repo)

GetHelmCharts returns list of helm charts in the specified repository

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import repository_service_api
from argocd_python_client.model.repository_helm_charts_response import RepositoryHelmChartsResponse
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
    api_instance = repository_service_api.RepositoryServiceApi(api_client)
    repo = "repo_example" # str | Repo URL for query
    force_refresh = True # bool | Whether to force a cache refresh on repo's connection state. (optional)

    # example passing only required values which don't have defaults set
    try:
        # GetHelmCharts returns list of helm charts in the specified repository
        api_response = api_instance.repository_service_get_helm_charts(repo)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_get_helm_charts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GetHelmCharts returns list of helm charts in the specified repository
        api_response = api_instance.repository_service_get_helm_charts(repo, force_refresh=force_refresh)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_get_helm_charts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query |
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#39;s connection state. | [optional]

### Return type

[**RepositoryHelmChartsResponse**](RepositoryHelmChartsResponse.md)

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

# **repository_service_list_apps**
> RepositoryRepoAppsResponse repository_service_list_apps(repo)

ListApps returns list of apps in the repe

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import repository_service_api
from argocd_python_client.model.repository_repo_apps_response import RepositoryRepoAppsResponse
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
    api_instance = repository_service_api.RepositoryServiceApi(api_client)
    repo = "repo_example" # str | 
    revision = "revision_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ListApps returns list of apps in the repe
        api_response = api_instance.repository_service_list_apps(repo)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_list_apps: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ListApps returns list of apps in the repe
        api_response = api_instance.repository_service_list_apps(repo, revision=revision)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_list_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**|  |
 **revision** | **str**|  | [optional]

### Return type

[**RepositoryRepoAppsResponse**](RepositoryRepoAppsResponse.md)

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

# **repository_service_list_refs**
> RepositoryRefs repository_service_list_refs(repo)



### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import repository_service_api
from argocd_python_client.model.repository_refs import RepositoryRefs
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
    api_instance = repository_service_api.RepositoryServiceApi(api_client)
    repo = "repo_example" # str | Repo URL for query
    force_refresh = True # bool | Whether to force a cache refresh on repo's connection state. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.repository_service_list_refs(repo)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_list_refs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.repository_service_list_refs(repo, force_refresh=force_refresh)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_list_refs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query |
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#39;s connection state. | [optional]

### Return type

[**RepositoryRefs**](RepositoryRefs.md)

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

# **repository_service_list_repositories**
> V1alpha1RepositoryList repository_service_list_repositories()

ListRepositories gets a list of all configured repositories

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import repository_service_api
from argocd_python_client.model.v1alpha1_repository_list import V1alpha1RepositoryList
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
    api_instance = repository_service_api.RepositoryServiceApi(api_client)
    repo = "repo_example" # str | Repo URL for query. (optional)
    force_refresh = True # bool | Whether to force a cache refresh on repo's connection state. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ListRepositories gets a list of all configured repositories
        api_response = api_instance.repository_service_list_repositories(repo=repo, force_refresh=force_refresh)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_list_repositories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query. | [optional]
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#39;s connection state. | [optional]

### Return type

[**V1alpha1RepositoryList**](V1alpha1RepositoryList.md)

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

# **repository_service_update_repository**
> V1alpha1Repository repository_service_update_repository(repo_repo, body)

UpdateRepository updates a repository configuration

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import repository_service_api
from argocd_python_client.model.v1alpha1_repository import V1alpha1Repository
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
    api_instance = repository_service_api.RepositoryServiceApi(api_client)
    repo_repo = "repo.repo_example" # str | Repo contains the URL to the remote repository
    body = V1alpha1Repository(
        connection_state=V1alpha1ConnectionState(
            attempted_at=V1Time(
                nanos=1,
                seconds="seconds_example",
            ),
            message="message_example",
            status="status_example",
        ),
        enable_lfs=True,
        enable_oci=True,
        github_app_enterprise_base_url="github_app_enterprise_base_url_example",
        github_app_id="github_app_id_example",
        github_app_installation_id="github_app_installation_id_example",
        github_app_private_key="github_app_private_key_example",
        inherited_creds=True,
        insecure=True,
        insecure_ignore_host_key=True,
        name="name_example",
        password="password_example",
        repo="repo_example",
        ssh_private_key="ssh_private_key_example",
        tls_client_cert_data="tls_client_cert_data_example",
        tls_client_cert_key="tls_client_cert_key_example",
        type="type_example",
        username="username_example",
    ) # V1alpha1Repository | 

    # example passing only required values which don't have defaults set
    try:
        # UpdateRepository updates a repository configuration
        api_response = api_instance.repository_service_update_repository(repo_repo, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_update_repository: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_repo** | **str**| Repo contains the URL to the remote repository |
 **body** | [**V1alpha1Repository**](V1alpha1Repository.md)|  |

### Return type

[**V1alpha1Repository**](V1alpha1Repository.md)

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

# **repository_service_validate_access**
> bool, date, datetime, dict, float, int, list, str, none_type repository_service_validate_access(repo, body)

ValidateAccess validates access to a repository with given parameters

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import repository_service_api
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
    api_instance = repository_service_api.RepositoryServiceApi(api_client)
    repo = "repo_example" # str | The URL to the repo
    body = "body_example" # str | The URL to the repo
    username = "username_example" # str | Username for accessing repo. (optional)
    password = "password_example" # str | Password for accessing repo. (optional)
    ssh_private_key = "sshPrivateKey_example" # str | Private key data for accessing SSH repository. (optional)
    insecure = True # bool | Whether to skip certificate or host key validation. (optional)
    tls_client_cert_data = "tlsClientCertData_example" # str | TLS client cert data for accessing HTTPS repository. (optional)
    tls_client_cert_key = "tlsClientCertKey_example" # str | TLS client cert key for accessing HTTPS repository. (optional)
    type = "type_example" # str | The type of the repo. (optional)
    name = "name_example" # str | The name of the repo. (optional)
    enable_oci = True # bool | Whether helm-oci support should be enabled for this repo. (optional)
    github_app_private_key = "githubAppPrivateKey_example" # str | Github App Private Key PEM data. (optional)
    github_app_id = "githubAppID_example" # str | Github App ID of the app used to access the repo. (optional)
    github_app_installation_id = "githubAppInstallationID_example" # str | Github App Installation ID of the installed GitHub App. (optional)
    github_app_enterprise_base_url = "githubAppEnterpriseBaseUrl_example" # str | Github App Enterprise base url if empty will default to https://api.github.com. (optional)

    # example passing only required values which don't have defaults set
    try:
        # ValidateAccess validates access to a repository with given parameters
        api_response = api_instance.repository_service_validate_access(repo, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_validate_access: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ValidateAccess validates access to a repository with given parameters
        api_response = api_instance.repository_service_validate_access(repo, body, username=username, password=password, ssh_private_key=ssh_private_key, insecure=insecure, tls_client_cert_data=tls_client_cert_data, tls_client_cert_key=tls_client_cert_key, type=type, name=name, enable_oci=enable_oci, github_app_private_key=github_app_private_key, github_app_id=github_app_id, github_app_installation_id=github_app_installation_id, github_app_enterprise_base_url=github_app_enterprise_base_url)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling RepositoryServiceApi->repository_service_validate_access: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The URL to the repo |
 **body** | **str**| The URL to the repo |
 **username** | **str**| Username for accessing repo. | [optional]
 **password** | **str**| Password for accessing repo. | [optional]
 **ssh_private_key** | **str**| Private key data for accessing SSH repository. | [optional]
 **insecure** | **bool**| Whether to skip certificate or host key validation. | [optional]
 **tls_client_cert_data** | **str**| TLS client cert data for accessing HTTPS repository. | [optional]
 **tls_client_cert_key** | **str**| TLS client cert key for accessing HTTPS repository. | [optional]
 **type** | **str**| The type of the repo. | [optional]
 **name** | **str**| The name of the repo. | [optional]
 **enable_oci** | **bool**| Whether helm-oci support should be enabled for this repo. | [optional]
 **github_app_private_key** | **str**| Github App Private Key PEM data. | [optional]
 **github_app_id** | **str**| Github App ID of the app used to access the repo. | [optional]
 **github_app_installation_id** | **str**| Github App Installation ID of the installed GitHub App. | [optional]
 **github_app_enterprise_base_url** | **str**| Github App Enterprise base url if empty will default to https://api.github.com. | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

