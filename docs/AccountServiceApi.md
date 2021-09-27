# argocd_python_client.AccountServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_service_can_i**](AccountServiceApi.md#account_service_can_i) | **GET** /api/v1/account/can-i/{resource}/{action}/{subresource} | CanI checks if the current account has permission to perform an action
[**account_service_create_token**](AccountServiceApi.md#account_service_create_token) | **POST** /api/v1/account/{name}/token | CreateToken creates a token
[**account_service_delete_token**](AccountServiceApi.md#account_service_delete_token) | **DELETE** /api/v1/account/{name}/token/{id} | DeleteToken deletes a token
[**account_service_get_account**](AccountServiceApi.md#account_service_get_account) | **GET** /api/v1/account/{name} | GetAccount returns an account
[**account_service_list_accounts**](AccountServiceApi.md#account_service_list_accounts) | **GET** /api/v1/account | ListAccounts returns the list of accounts
[**account_service_update_password**](AccountServiceApi.md#account_service_update_password) | **PUT** /api/v1/account/password | UpdatePassword updates an account&#39;s password to a new value


# **account_service_can_i**
> AccountCanIResponse account_service_can_i(resource, action, subresource)

CanI checks if the current account has permission to perform an action

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import account_service_api
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.account_can_i_response import AccountCanIResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = account_service_api.AccountServiceApi(api_client)
    resource = "resource_example" # str | 
    action = "action_example" # str | 
    subresource = "subresource_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # CanI checks if the current account has permission to perform an action
        api_response = api_instance.account_service_can_i(resource, action, subresource)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling AccountServiceApi->account_service_can_i: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  |
 **action** | **str**|  |
 **subresource** | **str**|  |

### Return type

[**AccountCanIResponse**](AccountCanIResponse.md)

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

# **account_service_create_token**
> AccountCreateTokenResponse account_service_create_token(name, body)

CreateToken creates a token

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import account_service_api
from argocd_python_client.model.account_create_token_request import AccountCreateTokenRequest
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.account_create_token_response import AccountCreateTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = account_service_api.AccountServiceApi(api_client)
    name = "name_example" # str | 
    body = AccountCreateTokenRequest(
        expires_in="expires_in_example",
        id="id_example",
        name="name_example",
    ) # AccountCreateTokenRequest | 

    # example passing only required values which don't have defaults set
    try:
        # CreateToken creates a token
        api_response = api_instance.account_service_create_token(name, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling AccountServiceApi->account_service_create_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **body** | [**AccountCreateTokenRequest**](AccountCreateTokenRequest.md)|  |

### Return type

[**AccountCreateTokenResponse**](AccountCreateTokenResponse.md)

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

# **account_service_delete_token**
> bool, date, datetime, dict, float, int, list, str, none_type account_service_delete_token(name, id)

DeleteToken deletes a token

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import account_service_api
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
    api_instance = account_service_api.AccountServiceApi(api_client)
    name = "name_example" # str | 
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # DeleteToken deletes a token
        api_response = api_instance.account_service_delete_token(name, id)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling AccountServiceApi->account_service_delete_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **id** | **str**|  |

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

# **account_service_get_account**
> AccountAccount account_service_get_account(name)

GetAccount returns an account

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import account_service_api
from argocd_python_client.model.account_account import AccountAccount
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
    api_instance = account_service_api.AccountServiceApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # GetAccount returns an account
        api_response = api_instance.account_service_get_account(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling AccountServiceApi->account_service_get_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**AccountAccount**](AccountAccount.md)

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

# **account_service_list_accounts**
> AccountAccountsList account_service_list_accounts()

ListAccounts returns the list of accounts

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import account_service_api
from argocd_python_client.model.account_accounts_list import AccountAccountsList
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
    api_instance = account_service_api.AccountServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # ListAccounts returns the list of accounts
        api_response = api_instance.account_service_list_accounts()
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling AccountServiceApi->account_service_list_accounts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountAccountsList**](AccountAccountsList.md)

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

# **account_service_update_password**
> bool, date, datetime, dict, float, int, list, str, none_type account_service_update_password(body)

UpdatePassword updates an account's password to a new value

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import account_service_api
from argocd_python_client.model.account_update_password_request import AccountUpdatePasswordRequest
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
    api_instance = account_service_api.AccountServiceApi(api_client)
    body = AccountUpdatePasswordRequest(
        current_password="current_password_example",
        name="name_example",
        new_password="new_password_example",
    ) # AccountUpdatePasswordRequest | 

    # example passing only required values which don't have defaults set
    try:
        # UpdatePassword updates an account's password to a new value
        api_response = api_instance.account_service_update_password(body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling AccountServiceApi->account_service_update_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountUpdatePasswordRequest**](AccountUpdatePasswordRequest.md)|  |

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

