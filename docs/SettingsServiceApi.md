# openapi_client.SettingsServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_service_get**](SettingsServiceApi.md#settings_service_get) | **GET** /api/v1/settings | Get returns Argo CD settings


# **settings_service_get**
> ClusterSettings settings_service_get()

Get returns Argo CD settings

### Example

```python
import time
import openapi_client
from openapi_client.api import settings_service_api
from openapi_client.model.runtime_error import RuntimeError
from openapi_client.model.cluster_settings import ClusterSettings
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = settings_service_api.SettingsServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get returns Argo CD settings
        api_response = api_instance.settings_service_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SettingsServiceApi->settings_service_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterSettings**](ClusterSettings.md)

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

