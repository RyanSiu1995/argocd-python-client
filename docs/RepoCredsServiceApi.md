# openapi_client.RepoCredsServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repo_creds_service_create_repository_credentials**](RepoCredsServiceApi.md#repo_creds_service_create_repository_credentials) | **POST** /api/v1/repocreds | CreateRepositoryCredentials creates a new repository credential set
[**repo_creds_service_delete_repository_credentials**](RepoCredsServiceApi.md#repo_creds_service_delete_repository_credentials) | **DELETE** /api/v1/repocreds/{url} | DeleteRepositoryCredentials deletes a repository credential set from the configuration
[**repo_creds_service_list_repository_credentials**](RepoCredsServiceApi.md#repo_creds_service_list_repository_credentials) | **GET** /api/v1/repocreds | ListRepositoryCredentials gets a list of all configured repository credential sets
[**repo_creds_service_update_repository_credentials**](RepoCredsServiceApi.md#repo_creds_service_update_repository_credentials) | **PUT** /api/v1/repocreds/{creds.url} | UpdateRepositoryCredentials updates a repository credential set


# **repo_creds_service_create_repository_credentials**
> V1alpha1RepoCreds repo_creds_service_create_repository_credentials(body)

CreateRepositoryCredentials creates a new repository credential set

### Example

```python
import time
import openapi_client
from openapi_client.api import repo_creds_service_api
from openapi_client.model.runtime_error import RuntimeError
from openapi_client.model.v1alpha1_repo_creds import V1alpha1RepoCreds
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = repo_creds_service_api.RepoCredsServiceApi(api_client)
    body = V1alpha1RepoCreds(
        github_app_enterprise_base_url="github_app_enterprise_base_url_example",
        github_app_id="github_app_id_example",
        github_app_installation_id="github_app_installation_id_example",
        github_app_private_key="github_app_private_key_example",
        password="password_example",
        ssh_private_key="ssh_private_key_example",
        tls_client_cert_data="tls_client_cert_data_example",
        tls_client_cert_key="tls_client_cert_key_example",
        url="url_example",
        username="username_example",
    ) # V1alpha1RepoCreds | Repository definition
    upsert = True # bool | Whether to create in upsert mode. (optional)

    # example passing only required values which don't have defaults set
    try:
        # CreateRepositoryCredentials creates a new repository credential set
        api_response = api_instance.repo_creds_service_create_repository_credentials(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RepoCredsServiceApi->repo_creds_service_create_repository_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # CreateRepositoryCredentials creates a new repository credential set
        api_response = api_instance.repo_creds_service_create_repository_credentials(body, upsert=upsert)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RepoCredsServiceApi->repo_creds_service_create_repository_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)| Repository definition |
 **upsert** | **bool**| Whether to create in upsert mode. | [optional]

### Return type

[**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)

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

# **repo_creds_service_delete_repository_credentials**
> bool, date, datetime, dict, float, int, list, str, none_type repo_creds_service_delete_repository_credentials(url)

DeleteRepositoryCredentials deletes a repository credential set from the configuration

### Example

```python
import time
import openapi_client
from openapi_client.api import repo_creds_service_api
from openapi_client.model.runtime_error import RuntimeError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = repo_creds_service_api.RepoCredsServiceApi(api_client)
    url = "url_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # DeleteRepositoryCredentials deletes a repository credential set from the configuration
        api_response = api_instance.repo_creds_service_delete_repository_credentials(url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RepoCredsServiceApi->repo_creds_service_delete_repository_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  |

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

# **repo_creds_service_list_repository_credentials**
> V1alpha1RepoCredsList repo_creds_service_list_repository_credentials()

ListRepositoryCredentials gets a list of all configured repository credential sets

### Example

```python
import time
import openapi_client
from openapi_client.api import repo_creds_service_api
from openapi_client.model.runtime_error import RuntimeError
from openapi_client.model.v1alpha1_repo_creds_list import V1alpha1RepoCredsList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = repo_creds_service_api.RepoCredsServiceApi(api_client)
    url = "url_example" # str | Repo URL for query. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ListRepositoryCredentials gets a list of all configured repository credential sets
        api_response = api_instance.repo_creds_service_list_repository_credentials(url=url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RepoCredsServiceApi->repo_creds_service_list_repository_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| Repo URL for query. | [optional]

### Return type

[**V1alpha1RepoCredsList**](V1alpha1RepoCredsList.md)

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

# **repo_creds_service_update_repository_credentials**
> V1alpha1RepoCreds repo_creds_service_update_repository_credentials(creds_url, body)

UpdateRepositoryCredentials updates a repository credential set

### Example

```python
import time
import openapi_client
from openapi_client.api import repo_creds_service_api
from openapi_client.model.runtime_error import RuntimeError
from openapi_client.model.v1alpha1_repo_creds import V1alpha1RepoCreds
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = repo_creds_service_api.RepoCredsServiceApi(api_client)
    creds_url = "creds.url_example" # str | URL is the URL that this credentials matches to
    body = V1alpha1RepoCreds(
        github_app_enterprise_base_url="github_app_enterprise_base_url_example",
        github_app_id="github_app_id_example",
        github_app_installation_id="github_app_installation_id_example",
        github_app_private_key="github_app_private_key_example",
        password="password_example",
        ssh_private_key="ssh_private_key_example",
        tls_client_cert_data="tls_client_cert_data_example",
        tls_client_cert_key="tls_client_cert_key_example",
        url="url_example",
        username="username_example",
    ) # V1alpha1RepoCreds | 

    # example passing only required values which don't have defaults set
    try:
        # UpdateRepositoryCredentials updates a repository credential set
        api_response = api_instance.repo_creds_service_update_repository_credentials(creds_url, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RepoCredsServiceApi->repo_creds_service_update_repository_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_url** | **str**| URL is the URL that this credentials matches to |
 **body** | [**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)|  |

### Return type

[**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)

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

