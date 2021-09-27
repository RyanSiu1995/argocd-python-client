# argocd_python_client.SessionServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**session_service_create**](SessionServiceApi.md#session_service_create) | **POST** /api/v1/session | Create a new JWT for authentication and set a cookie if using HTTP
[**session_service_delete**](SessionServiceApi.md#session_service_delete) | **DELETE** /api/v1/session | Delete an existing JWT cookie if using HTTP
[**session_service_get_user_info**](SessionServiceApi.md#session_service_get_user_info) | **GET** /api/v1/session/userinfo | Get the current user&#39;s info


# **session_service_create**
> SessionSessionResponse session_service_create(body)

Create a new JWT for authentication and set a cookie if using HTTP

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import session_service_api
from argocd_python_client.model.session_session_response import SessionSessionResponse
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.session_session_create_request import SessionSessionCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = session_service_api.SessionServiceApi(api_client)
    body = SessionSessionCreateRequest(
        password="password_example",
        token="token_example",
        username="username_example",
    ) # SessionSessionCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new JWT for authentication and set a cookie if using HTTP
        api_response = api_instance.session_service_create(body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling SessionServiceApi->session_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SessionSessionCreateRequest**](SessionSessionCreateRequest.md)|  |

### Return type

[**SessionSessionResponse**](SessionSessionResponse.md)

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

# **session_service_delete**
> SessionSessionResponse session_service_delete()

Delete an existing JWT cookie if using HTTP

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import session_service_api
from argocd_python_client.model.session_session_response import SessionSessionResponse
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
    api_instance = session_service_api.SessionServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete an existing JWT cookie if using HTTP
        api_response = api_instance.session_service_delete()
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling SessionServiceApi->session_service_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SessionSessionResponse**](SessionSessionResponse.md)

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

# **session_service_get_user_info**
> SessionGetUserInfoResponse session_service_get_user_info()

Get the current user's info

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import session_service_api
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.session_get_user_info_response import SessionGetUserInfoResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = session_service_api.SessionServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the current user's info
        api_response = api_instance.session_service_get_user_info()
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling SessionServiceApi->session_service_get_user_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SessionGetUserInfoResponse**](SessionGetUserInfoResponse.md)

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

