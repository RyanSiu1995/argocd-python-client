# openapi_client.CertificateServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificate_service_create_certificate**](CertificateServiceApi.md#certificate_service_create_certificate) | **POST** /api/v1/certificates | Creates repository certificates on the server
[**certificate_service_delete_certificate**](CertificateServiceApi.md#certificate_service_delete_certificate) | **DELETE** /api/v1/certificates | Delete the certificates that match the RepositoryCertificateQuery
[**certificate_service_list_certificates**](CertificateServiceApi.md#certificate_service_list_certificates) | **GET** /api/v1/certificates | List all available repository certificates


# **certificate_service_create_certificate**
> V1alpha1RepositoryCertificateList certificate_service_create_certificate(body)

Creates repository certificates on the server

### Example

```python
import time
import openapi_client
from openapi_client.api import certificate_service_api
from openapi_client.model.runtime_error import RuntimeError
from openapi_client.model.v1alpha1_repository_certificate_list import V1alpha1RepositoryCertificateList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_service_api.CertificateServiceApi(api_client)
    body = V1alpha1RepositoryCertificateList(
        items=[
            V1alpha1RepositoryCertificate(
                cert_data='YQ==',
                cert_info="cert_info_example",
                cert_sub_type="cert_sub_type_example",
                cert_type="cert_type_example",
                server_name="server_name_example",
            ),
        ],
        metadata=V1ListMeta(
            _continue="_continue_example",
            remaining_item_count="remaining_item_count_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
        ),
    ) # V1alpha1RepositoryCertificateList | List of certificates to be created
    upsert = True # bool | Whether to upsert already existing certificates. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates repository certificates on the server
        api_response = api_instance.certificate_service_create_certificate(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateServiceApi->certificate_service_create_certificate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates repository certificates on the server
        api_response = api_instance.certificate_service_create_certificate(body, upsert=upsert)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateServiceApi->certificate_service_create_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1RepositoryCertificateList**](V1alpha1RepositoryCertificateList.md)| List of certificates to be created |
 **upsert** | **bool**| Whether to upsert already existing certificates. | [optional]

### Return type

[**V1alpha1RepositoryCertificateList**](V1alpha1RepositoryCertificateList.md)

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

# **certificate_service_delete_certificate**
> V1alpha1RepositoryCertificateList certificate_service_delete_certificate()

Delete the certificates that match the RepositoryCertificateQuery

### Example

```python
import time
import openapi_client
from openapi_client.api import certificate_service_api
from openapi_client.model.runtime_error import RuntimeError
from openapi_client.model.v1alpha1_repository_certificate_list import V1alpha1RepositoryCertificateList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_service_api.CertificateServiceApi(api_client)
    host_name_pattern = "hostNamePattern_example" # str | A file-glob pattern (not regular expression) the host name has to match. (optional)
    cert_type = "certType_example" # str | The type of the certificate to match (ssh or https). (optional)
    cert_sub_type = "certSubType_example" # str | The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete the certificates that match the RepositoryCertificateQuery
        api_response = api_instance.certificate_service_delete_certificate(host_name_pattern=host_name_pattern, cert_type=cert_type, cert_sub_type=cert_sub_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateServiceApi->certificate_service_delete_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name_pattern** | **str**| A file-glob pattern (not regular expression) the host name has to match. | [optional]
 **cert_type** | **str**| The type of the certificate to match (ssh or https). | [optional]
 **cert_sub_type** | **str**| The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). | [optional]

### Return type

[**V1alpha1RepositoryCertificateList**](V1alpha1RepositoryCertificateList.md)

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

# **certificate_service_list_certificates**
> V1alpha1RepositoryCertificateList certificate_service_list_certificates()

List all available repository certificates

### Example

```python
import time
import openapi_client
from openapi_client.api import certificate_service_api
from openapi_client.model.runtime_error import RuntimeError
from openapi_client.model.v1alpha1_repository_certificate_list import V1alpha1RepositoryCertificateList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_service_api.CertificateServiceApi(api_client)
    host_name_pattern = "hostNamePattern_example" # str | A file-glob pattern (not regular expression) the host name has to match. (optional)
    cert_type = "certType_example" # str | The type of the certificate to match (ssh or https). (optional)
    cert_sub_type = "certSubType_example" # str | The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all available repository certificates
        api_response = api_instance.certificate_service_list_certificates(host_name_pattern=host_name_pattern, cert_type=cert_type, cert_sub_type=cert_sub_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateServiceApi->certificate_service_list_certificates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name_pattern** | **str**| A file-glob pattern (not regular expression) the host name has to match. | [optional]
 **cert_type** | **str**| The type of the certificate to match (ssh or https). | [optional]
 **cert_sub_type** | **str**| The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). | [optional]

### Return type

[**V1alpha1RepositoryCertificateList**](V1alpha1RepositoryCertificateList.md)

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

