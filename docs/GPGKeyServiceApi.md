# openapi_client.GPGKeyServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_pg_key_service_create**](GPGKeyServiceApi.md#g_pg_key_service_create) | **POST** /api/v1/gpgkeys | Create one or more GPG public keys in the server&#39;s configuration
[**g_pg_key_service_delete**](GPGKeyServiceApi.md#g_pg_key_service_delete) | **DELETE** /api/v1/gpgkeys | Delete specified GPG public key from the server&#39;s configuration
[**g_pg_key_service_get**](GPGKeyServiceApi.md#g_pg_key_service_get) | **GET** /api/v1/gpgkeys/{keyID} | Get information about specified GPG public key from the server
[**g_pg_key_service_list**](GPGKeyServiceApi.md#g_pg_key_service_list) | **GET** /api/v1/gpgkeys | List all available repository certificates


# **g_pg_key_service_create**
> GpgkeyGnuPGPublicKeyCreateResponse g_pg_key_service_create(body)

Create one or more GPG public keys in the server's configuration

### Example

```python
import time
import openapi_client
from openapi_client.api import gpg_key_service_api
from openapi_client.model.gpgkey_gnu_pg_public_key_create_response import GpgkeyGnuPGPublicKeyCreateResponse
from openapi_client.model.runtime_error import RuntimeError
from openapi_client.model.v1alpha1_gnu_pg_public_key import V1alpha1GnuPGPublicKey
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = gpg_key_service_api.GPGKeyServiceApi(api_client)
    body = V1alpha1GnuPGPublicKey(
        fingerprint="fingerprint_example",
        key_data="key_data_example",
        key_id="key_id_example",
        owner="owner_example",
        sub_type="sub_type_example",
        trust="trust_example",
    ) # V1alpha1GnuPGPublicKey | Raw key data of the GPG key(s) to create
    upsert = True # bool | Whether to upsert already existing public keys. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create one or more GPG public keys in the server's configuration
        api_response = api_instance.g_pg_key_service_create(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GPGKeyServiceApi->g_pg_key_service_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create one or more GPG public keys in the server's configuration
        api_response = api_instance.g_pg_key_service_create(body, upsert=upsert)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GPGKeyServiceApi->g_pg_key_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1GnuPGPublicKey**](V1alpha1GnuPGPublicKey.md)| Raw key data of the GPG key(s) to create |
 **upsert** | **bool**| Whether to upsert already existing public keys. | [optional]

### Return type

[**GpgkeyGnuPGPublicKeyCreateResponse**](GpgkeyGnuPGPublicKeyCreateResponse.md)

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

# **g_pg_key_service_delete**
> bool, date, datetime, dict, float, int, list, str, none_type g_pg_key_service_delete()

Delete specified GPG public key from the server's configuration

### Example

```python
import time
import openapi_client
from openapi_client.api import gpg_key_service_api
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
    api_instance = gpg_key_service_api.GPGKeyServiceApi(api_client)
    key_id = "keyID_example" # str | The GPG key ID to query for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete specified GPG public key from the server's configuration
        api_response = api_instance.g_pg_key_service_delete(key_id=key_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GPGKeyServiceApi->g_pg_key_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The GPG key ID to query for. | [optional]

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

# **g_pg_key_service_get**
> V1alpha1GnuPGPublicKey g_pg_key_service_get(key_id)

Get information about specified GPG public key from the server

### Example

```python
import time
import openapi_client
from openapi_client.api import gpg_key_service_api
from openapi_client.model.runtime_error import RuntimeError
from openapi_client.model.v1alpha1_gnu_pg_public_key import V1alpha1GnuPGPublicKey
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = gpg_key_service_api.GPGKeyServiceApi(api_client)
    key_id = "keyID_example" # str | The GPG key ID to query for

    # example passing only required values which don't have defaults set
    try:
        # Get information about specified GPG public key from the server
        api_response = api_instance.g_pg_key_service_get(key_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GPGKeyServiceApi->g_pg_key_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The GPG key ID to query for |

### Return type

[**V1alpha1GnuPGPublicKey**](V1alpha1GnuPGPublicKey.md)

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

# **g_pg_key_service_list**
> V1alpha1GnuPGPublicKeyList g_pg_key_service_list()

List all available repository certificates

### Example

```python
import time
import openapi_client
from openapi_client.api import gpg_key_service_api
from openapi_client.model.v1alpha1_gnu_pg_public_key_list import V1alpha1GnuPGPublicKeyList
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
    api_instance = gpg_key_service_api.GPGKeyServiceApi(api_client)
    key_id = "keyID_example" # str | The GPG key ID to query for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all available repository certificates
        api_response = api_instance.g_pg_key_service_list(key_id=key_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GPGKeyServiceApi->g_pg_key_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The GPG key ID to query for. | [optional]

### Return type

[**V1alpha1GnuPGPublicKeyList**](V1alpha1GnuPGPublicKeyList.md)

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

