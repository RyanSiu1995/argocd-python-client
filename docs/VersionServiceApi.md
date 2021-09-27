# openapi_client.VersionServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_service_version**](VersionServiceApi.md#version_service_version) | **GET** /api/version | Version returns version information of the API server


# **version_service_version**
> VersionVersionMessage version_service_version()

Version returns version information of the API server

### Example

```python
import time
import openapi_client
from openapi_client.api import version_service_api
from openapi_client.model.runtime_error import RuntimeError
from openapi_client.model.version_version_message import VersionVersionMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = version_service_api.VersionServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Version returns version information of the API server
        api_response = api_instance.version_service_version()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VersionServiceApi->version_service_version: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionVersionMessage**](VersionVersionMessage.md)

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

