# argocd-python-client
Description of all APIs

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: version not set
- Package version: 1.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/RyanSiu1995/argocd-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/RyanSiu1995/argocd-python-client.git`)

Then import the package:
```python
import argocd_python_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import argocd_python_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import argocd_python_client
from pprint import pprint
from argocd_python_client.api import account_service_api
from argocd_python_client.model.account_account import AccountAccount
from argocd_python_client.model.account_accounts_list import AccountAccountsList
from argocd_python_client.model.account_can_i_response import AccountCanIResponse
from argocd_python_client.model.account_create_token_request import AccountCreateTokenRequest
from argocd_python_client.model.account_create_token_response import AccountCreateTokenResponse
from argocd_python_client.model.account_update_password_request import AccountUpdatePasswordRequest
from argocd_python_client.model.runtime_error import RuntimeError
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with argocd_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_service_api.AccountServiceApi(api_client)
    resource = "resource_example" # str | 
action = "action_example" # str | 
subresource = "subresource_example" # str | 

    try:
        # CanI checks if the current account has permission to perform an action
        api_response = api_instance.account_service_can_i(resource, action, subresource)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling AccountServiceApi->account_service_can_i: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountServiceApi* | [**account_service_can_i**](docs/AccountServiceApi.md#account_service_can_i) | **GET** /api/v1/account/can-i/{resource}/{action}/{subresource} | CanI checks if the current account has permission to perform an action
*AccountServiceApi* | [**account_service_create_token**](docs/AccountServiceApi.md#account_service_create_token) | **POST** /api/v1/account/{name}/token | CreateToken creates a token
*AccountServiceApi* | [**account_service_delete_token**](docs/AccountServiceApi.md#account_service_delete_token) | **DELETE** /api/v1/account/{name}/token/{id} | DeleteToken deletes a token
*AccountServiceApi* | [**account_service_get_account**](docs/AccountServiceApi.md#account_service_get_account) | **GET** /api/v1/account/{name} | GetAccount returns an account
*AccountServiceApi* | [**account_service_list_accounts**](docs/AccountServiceApi.md#account_service_list_accounts) | **GET** /api/v1/account | ListAccounts returns the list of accounts
*AccountServiceApi* | [**account_service_update_password**](docs/AccountServiceApi.md#account_service_update_password) | **PUT** /api/v1/account/password | UpdatePassword updates an account&#39;s password to a new value
*ApplicationServiceApi* | [**application_service_create**](docs/ApplicationServiceApi.md#application_service_create) | **POST** /api/v1/applications | Create creates an application
*ApplicationServiceApi* | [**application_service_delete**](docs/ApplicationServiceApi.md#application_service_delete) | **DELETE** /api/v1/applications/{name} | Delete deletes an application
*ApplicationServiceApi* | [**application_service_delete_resource**](docs/ApplicationServiceApi.md#application_service_delete_resource) | **DELETE** /api/v1/applications/{name}/resource | DeleteResource deletes a single application resource
*ApplicationServiceApi* | [**application_service_get**](docs/ApplicationServiceApi.md#application_service_get) | **GET** /api/v1/applications/{name} | Get returns an application by name
*ApplicationServiceApi* | [**application_service_get_application_sync_windows**](docs/ApplicationServiceApi.md#application_service_get_application_sync_windows) | **GET** /api/v1/applications/{name}/syncwindows | Get returns sync windows of the application
*ApplicationServiceApi* | [**application_service_get_manifests**](docs/ApplicationServiceApi.md#application_service_get_manifests) | **GET** /api/v1/applications/{name}/manifests | GetManifests returns application manifests
*ApplicationServiceApi* | [**application_service_get_resource**](docs/ApplicationServiceApi.md#application_service_get_resource) | **GET** /api/v1/applications/{name}/resource | GetResource returns single application resource
*ApplicationServiceApi* | [**application_service_list**](docs/ApplicationServiceApi.md#application_service_list) | **GET** /api/v1/applications | List returns list of applications
*ApplicationServiceApi* | [**application_service_list_resource_actions**](docs/ApplicationServiceApi.md#application_service_list_resource_actions) | **GET** /api/v1/applications/{name}/resource/actions | ListResourceActions returns list of resource actions
*ApplicationServiceApi* | [**application_service_list_resource_events**](docs/ApplicationServiceApi.md#application_service_list_resource_events) | **GET** /api/v1/applications/{name}/events | ListResourceEvents returns a list of event resources
*ApplicationServiceApi* | [**application_service_managed_resources**](docs/ApplicationServiceApi.md#application_service_managed_resources) | **GET** /api/v1/applications/{applicationName}/managed-resources | ManagedResources returns list of managed resources
*ApplicationServiceApi* | [**application_service_patch**](docs/ApplicationServiceApi.md#application_service_patch) | **PATCH** /api/v1/applications/{name} | Patch patch an application
*ApplicationServiceApi* | [**application_service_patch_resource**](docs/ApplicationServiceApi.md#application_service_patch_resource) | **POST** /api/v1/applications/{name}/resource | PatchResource patch single application resource
*ApplicationServiceApi* | [**application_service_pod_logs**](docs/ApplicationServiceApi.md#application_service_pod_logs) | **GET** /api/v1/applications/{name}/pods/{podName}/logs | PodLogs returns stream of log entries for the specified pod. Pod
*ApplicationServiceApi* | [**application_service_pod_logs2**](docs/ApplicationServiceApi.md#application_service_pod_logs2) | **GET** /api/v1/applications/{name}/logs | PodLogs returns stream of log entries for the specified pod. Pod
*ApplicationServiceApi* | [**application_service_resource_tree**](docs/ApplicationServiceApi.md#application_service_resource_tree) | **GET** /api/v1/applications/{applicationName}/resource-tree | ResourceTree returns resource tree
*ApplicationServiceApi* | [**application_service_revision_metadata**](docs/ApplicationServiceApi.md#application_service_revision_metadata) | **GET** /api/v1/applications/{name}/revisions/{revision}/metadata | Get the meta-data (author, date, tags, message) for a specific revision of the application
*ApplicationServiceApi* | [**application_service_rollback**](docs/ApplicationServiceApi.md#application_service_rollback) | **POST** /api/v1/applications/{name}/rollback | Rollback syncs an application to its target state
*ApplicationServiceApi* | [**application_service_run_resource_action**](docs/ApplicationServiceApi.md#application_service_run_resource_action) | **POST** /api/v1/applications/{name}/resource/actions | RunResourceAction run resource action
*ApplicationServiceApi* | [**application_service_sync**](docs/ApplicationServiceApi.md#application_service_sync) | **POST** /api/v1/applications/{name}/sync | Sync syncs an application to its target state
*ApplicationServiceApi* | [**application_service_terminate_operation**](docs/ApplicationServiceApi.md#application_service_terminate_operation) | **DELETE** /api/v1/applications/{name}/operation | TerminateOperation terminates the currently running operation
*ApplicationServiceApi* | [**application_service_update**](docs/ApplicationServiceApi.md#application_service_update) | **PUT** /api/v1/applications/{application.metadata.name} | Update updates an application
*ApplicationServiceApi* | [**application_service_update_spec**](docs/ApplicationServiceApi.md#application_service_update_spec) | **PUT** /api/v1/applications/{name}/spec | UpdateSpec updates an application spec
*ApplicationServiceApi* | [**application_service_watch**](docs/ApplicationServiceApi.md#application_service_watch) | **GET** /api/v1/stream/applications | Watch returns stream of application change events
*ApplicationServiceApi* | [**application_service_watch_resource_tree**](docs/ApplicationServiceApi.md#application_service_watch_resource_tree) | **GET** /api/v1/stream/applications/{applicationName}/resource-tree | Watch returns stream of application resource tree
*CertificateServiceApi* | [**certificate_service_create_certificate**](docs/CertificateServiceApi.md#certificate_service_create_certificate) | **POST** /api/v1/certificates | Creates repository certificates on the server
*CertificateServiceApi* | [**certificate_service_delete_certificate**](docs/CertificateServiceApi.md#certificate_service_delete_certificate) | **DELETE** /api/v1/certificates | Delete the certificates that match the RepositoryCertificateQuery
*CertificateServiceApi* | [**certificate_service_list_certificates**](docs/CertificateServiceApi.md#certificate_service_list_certificates) | **GET** /api/v1/certificates | List all available repository certificates
*ClusterServiceApi* | [**cluster_service_create**](docs/ClusterServiceApi.md#cluster_service_create) | **POST** /api/v1/clusters | Create creates a cluster
*ClusterServiceApi* | [**cluster_service_delete**](docs/ClusterServiceApi.md#cluster_service_delete) | **DELETE** /api/v1/clusters/{server} | Delete deletes a cluster
*ClusterServiceApi* | [**cluster_service_get**](docs/ClusterServiceApi.md#cluster_service_get) | **GET** /api/v1/clusters/{server} | Get returns a cluster by server address
*ClusterServiceApi* | [**cluster_service_invalidate_cache**](docs/ClusterServiceApi.md#cluster_service_invalidate_cache) | **POST** /api/v1/clusters/{server}/invalidate-cache | InvalidateCache invalidates cluster cache
*ClusterServiceApi* | [**cluster_service_list**](docs/ClusterServiceApi.md#cluster_service_list) | **GET** /api/v1/clusters | List returns list of clusters
*ClusterServiceApi* | [**cluster_service_rotate_auth**](docs/ClusterServiceApi.md#cluster_service_rotate_auth) | **POST** /api/v1/clusters/{server}/rotate-auth | RotateAuth rotates the bearer token used for a cluster
*ClusterServiceApi* | [**cluster_service_update**](docs/ClusterServiceApi.md#cluster_service_update) | **PUT** /api/v1/clusters/{cluster.server} | Update updates a cluster
*GPGKeyServiceApi* | [**g_pg_key_service_create**](docs/GPGKeyServiceApi.md#g_pg_key_service_create) | **POST** /api/v1/gpgkeys | Create one or more GPG public keys in the server&#39;s configuration
*GPGKeyServiceApi* | [**g_pg_key_service_delete**](docs/GPGKeyServiceApi.md#g_pg_key_service_delete) | **DELETE** /api/v1/gpgkeys | Delete specified GPG public key from the server&#39;s configuration
*GPGKeyServiceApi* | [**g_pg_key_service_get**](docs/GPGKeyServiceApi.md#g_pg_key_service_get) | **GET** /api/v1/gpgkeys/{keyID} | Get information about specified GPG public key from the server
*GPGKeyServiceApi* | [**g_pg_key_service_list**](docs/GPGKeyServiceApi.md#g_pg_key_service_list) | **GET** /api/v1/gpgkeys | List all available repository certificates
*ProjectServiceApi* | [**project_service_create**](docs/ProjectServiceApi.md#project_service_create) | **POST** /api/v1/projects | Create a new project
*ProjectServiceApi* | [**project_service_create_token**](docs/ProjectServiceApi.md#project_service_create_token) | **POST** /api/v1/projects/{project}/roles/{role}/token | Create a new project token
*ProjectServiceApi* | [**project_service_delete**](docs/ProjectServiceApi.md#project_service_delete) | **DELETE** /api/v1/projects/{name} | Delete deletes a project
*ProjectServiceApi* | [**project_service_delete_token**](docs/ProjectServiceApi.md#project_service_delete_token) | **DELETE** /api/v1/projects/{project}/roles/{role}/token/{iat} | Delete a new project token
*ProjectServiceApi* | [**project_service_get**](docs/ProjectServiceApi.md#project_service_get) | **GET** /api/v1/projects/{name} | Get returns a project by name
*ProjectServiceApi* | [**project_service_get_global_projects**](docs/ProjectServiceApi.md#project_service_get_global_projects) | **GET** /api/v1/projects/{name}/globalprojects | Get returns a virtual project by name
*ProjectServiceApi* | [**project_service_get_sync_windows_state**](docs/ProjectServiceApi.md#project_service_get_sync_windows_state) | **GET** /api/v1/projects/{name}/syncwindows | GetSchedulesState returns true if there are any active sync syncWindows
*ProjectServiceApi* | [**project_service_list**](docs/ProjectServiceApi.md#project_service_list) | **GET** /api/v1/projects | List returns list of projects
*ProjectServiceApi* | [**project_service_list_events**](docs/ProjectServiceApi.md#project_service_list_events) | **GET** /api/v1/projects/{name}/events | ListEvents returns a list of project events
*ProjectServiceApi* | [**project_service_update**](docs/ProjectServiceApi.md#project_service_update) | **PUT** /api/v1/projects/{project.metadata.name} | Update updates a project
*RepoCredsServiceApi* | [**repo_creds_service_create_repository_credentials**](docs/RepoCredsServiceApi.md#repo_creds_service_create_repository_credentials) | **POST** /api/v1/repocreds | CreateRepositoryCredentials creates a new repository credential set
*RepoCredsServiceApi* | [**repo_creds_service_delete_repository_credentials**](docs/RepoCredsServiceApi.md#repo_creds_service_delete_repository_credentials) | **DELETE** /api/v1/repocreds/{url} | DeleteRepositoryCredentials deletes a repository credential set from the configuration
*RepoCredsServiceApi* | [**repo_creds_service_list_repository_credentials**](docs/RepoCredsServiceApi.md#repo_creds_service_list_repository_credentials) | **GET** /api/v1/repocreds | ListRepositoryCredentials gets a list of all configured repository credential sets
*RepoCredsServiceApi* | [**repo_creds_service_update_repository_credentials**](docs/RepoCredsServiceApi.md#repo_creds_service_update_repository_credentials) | **PUT** /api/v1/repocreds/{creds.url} | UpdateRepositoryCredentials updates a repository credential set
*RepositoryServiceApi* | [**repository_service_create_repository**](docs/RepositoryServiceApi.md#repository_service_create_repository) | **POST** /api/v1/repositories | CreateRepository creates a new repository configuration
*RepositoryServiceApi* | [**repository_service_delete_repository**](docs/RepositoryServiceApi.md#repository_service_delete_repository) | **DELETE** /api/v1/repositories/{repo} | DeleteRepository deletes a repository from the configuration
*RepositoryServiceApi* | [**repository_service_get**](docs/RepositoryServiceApi.md#repository_service_get) | **GET** /api/v1/repositories/{repo} | Get returns a repository or its credentials
*RepositoryServiceApi* | [**repository_service_get_app_details**](docs/RepositoryServiceApi.md#repository_service_get_app_details) | **POST** /api/v1/repositories/{source.repoURL}/appdetails | GetAppDetails returns application details by given path
*RepositoryServiceApi* | [**repository_service_get_helm_charts**](docs/RepositoryServiceApi.md#repository_service_get_helm_charts) | **GET** /api/v1/repositories/{repo}/helmcharts | GetHelmCharts returns list of helm charts in the specified repository
*RepositoryServiceApi* | [**repository_service_list_apps**](docs/RepositoryServiceApi.md#repository_service_list_apps) | **GET** /api/v1/repositories/{repo}/apps | ListApps returns list of apps in the repe
*RepositoryServiceApi* | [**repository_service_list_refs**](docs/RepositoryServiceApi.md#repository_service_list_refs) | **GET** /api/v1/repositories/{repo}/refs | 
*RepositoryServiceApi* | [**repository_service_list_repositories**](docs/RepositoryServiceApi.md#repository_service_list_repositories) | **GET** /api/v1/repositories | ListRepositories gets a list of all configured repositories
*RepositoryServiceApi* | [**repository_service_update_repository**](docs/RepositoryServiceApi.md#repository_service_update_repository) | **PUT** /api/v1/repositories/{repo.repo} | UpdateRepository updates a repository configuration
*RepositoryServiceApi* | [**repository_service_validate_access**](docs/RepositoryServiceApi.md#repository_service_validate_access) | **POST** /api/v1/repositories/{repo}/validate | ValidateAccess validates access to a repository with given parameters
*SessionServiceApi* | [**session_service_create**](docs/SessionServiceApi.md#session_service_create) | **POST** /api/v1/session | Create a new JWT for authentication and set a cookie if using HTTP
*SessionServiceApi* | [**session_service_delete**](docs/SessionServiceApi.md#session_service_delete) | **DELETE** /api/v1/session | Delete an existing JWT cookie if using HTTP
*SessionServiceApi* | [**session_service_get_user_info**](docs/SessionServiceApi.md#session_service_get_user_info) | **GET** /api/v1/session/userinfo | Get the current user&#39;s info
*SettingsServiceApi* | [**settings_service_get**](docs/SettingsServiceApi.md#settings_service_get) | **GET** /api/v1/settings | Get returns Argo CD settings
*VersionServiceApi* | [**version_service_version**](docs/VersionServiceApi.md#version_service_version) | **GET** /api/version | Version returns version information of the API server


## Documentation For Models

 - [AccountAccount](docs/AccountAccount.md)
 - [AccountAccountsList](docs/AccountAccountsList.md)
 - [AccountCanIResponse](docs/AccountCanIResponse.md)
 - [AccountCreateTokenRequest](docs/AccountCreateTokenRequest.md)
 - [AccountCreateTokenResponse](docs/AccountCreateTokenResponse.md)
 - [AccountToken](docs/AccountToken.md)
 - [AccountUpdatePasswordRequest](docs/AccountUpdatePasswordRequest.md)
 - [ApplicationApplicationPatchRequest](docs/ApplicationApplicationPatchRequest.md)
 - [ApplicationApplicationResourceResponse](docs/ApplicationApplicationResourceResponse.md)
 - [ApplicationApplicationRollbackRequest](docs/ApplicationApplicationRollbackRequest.md)
 - [ApplicationApplicationSyncRequest](docs/ApplicationApplicationSyncRequest.md)
 - [ApplicationApplicationSyncWindow](docs/ApplicationApplicationSyncWindow.md)
 - [ApplicationApplicationSyncWindowsResponse](docs/ApplicationApplicationSyncWindowsResponse.md)
 - [ApplicationLogEntry](docs/ApplicationLogEntry.md)
 - [ApplicationManagedResourcesResponse](docs/ApplicationManagedResourcesResponse.md)
 - [ApplicationResourceActionsListResponse](docs/ApplicationResourceActionsListResponse.md)
 - [ApplicationSyncOptions](docs/ApplicationSyncOptions.md)
 - [Applicationv1alpha1EnvEntry](docs/Applicationv1alpha1EnvEntry.md)
 - [ClusterConnector](docs/ClusterConnector.md)
 - [ClusterDexConfig](docs/ClusterDexConfig.md)
 - [ClusterGoogleAnalyticsConfig](docs/ClusterGoogleAnalyticsConfig.md)
 - [ClusterHelp](docs/ClusterHelp.md)
 - [ClusterOIDCConfig](docs/ClusterOIDCConfig.md)
 - [ClusterPlugin](docs/ClusterPlugin.md)
 - [ClusterSettings](docs/ClusterSettings.md)
 - [GpgkeyGnuPGPublicKeyCreateResponse](docs/GpgkeyGnuPGPublicKeyCreateResponse.md)
 - [OidcClaim](docs/OidcClaim.md)
 - [ProjectGlobalProjectsResponse](docs/ProjectGlobalProjectsResponse.md)
 - [ProjectProjectCreateRequest](docs/ProjectProjectCreateRequest.md)
 - [ProjectProjectTokenCreateRequest](docs/ProjectProjectTokenCreateRequest.md)
 - [ProjectProjectTokenResponse](docs/ProjectProjectTokenResponse.md)
 - [ProjectProjectUpdateRequest](docs/ProjectProjectUpdateRequest.md)
 - [ProjectSyncWindowsResponse](docs/ProjectSyncWindowsResponse.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RepositoryAppInfo](docs/RepositoryAppInfo.md)
 - [RepositoryHelmAppSpec](docs/RepositoryHelmAppSpec.md)
 - [RepositoryHelmChart](docs/RepositoryHelmChart.md)
 - [RepositoryHelmChartsResponse](docs/RepositoryHelmChartsResponse.md)
 - [RepositoryKsonnetAppSpec](docs/RepositoryKsonnetAppSpec.md)
 - [RepositoryKsonnetEnvironment](docs/RepositoryKsonnetEnvironment.md)
 - [RepositoryKsonnetEnvironmentDestination](docs/RepositoryKsonnetEnvironmentDestination.md)
 - [RepositoryKustomizeAppSpec](docs/RepositoryKustomizeAppSpec.md)
 - [RepositoryManifestResponse](docs/RepositoryManifestResponse.md)
 - [RepositoryRefs](docs/RepositoryRefs.md)
 - [RepositoryRepoAppDetailsQuery](docs/RepositoryRepoAppDetailsQuery.md)
 - [RepositoryRepoAppDetailsResponse](docs/RepositoryRepoAppDetailsResponse.md)
 - [RepositoryRepoAppsResponse](docs/RepositoryRepoAppsResponse.md)
 - [RuntimeError](docs/RuntimeError.md)
 - [RuntimeStreamError](docs/RuntimeStreamError.md)
 - [SessionGetUserInfoResponse](docs/SessionGetUserInfoResponse.md)
 - [SessionSessionCreateRequest](docs/SessionSessionCreateRequest.md)
 - [SessionSessionResponse](docs/SessionSessionResponse.md)
 - [StreamResultOfApplicationLogEntry](docs/StreamResultOfApplicationLogEntry.md)
 - [StreamResultOfV1alpha1ApplicationTree](docs/StreamResultOfV1alpha1ApplicationTree.md)
 - [StreamResultOfV1alpha1ApplicationWatchEvent](docs/StreamResultOfV1alpha1ApplicationWatchEvent.md)
 - [V1Event](docs/V1Event.md)
 - [V1EventList](docs/V1EventList.md)
 - [V1EventSeries](docs/V1EventSeries.md)
 - [V1EventSource](docs/V1EventSource.md)
 - [V1FieldsV1](docs/V1FieldsV1.md)
 - [V1GroupKind](docs/V1GroupKind.md)
 - [V1ListMeta](docs/V1ListMeta.md)
 - [V1LoadBalancerIngress](docs/V1LoadBalancerIngress.md)
 - [V1ManagedFieldsEntry](docs/V1ManagedFieldsEntry.md)
 - [V1MicroTime](docs/V1MicroTime.md)
 - [V1NodeSystemInfo](docs/V1NodeSystemInfo.md)
 - [V1ObjectMeta](docs/V1ObjectMeta.md)
 - [V1ObjectReference](docs/V1ObjectReference.md)
 - [V1OwnerReference](docs/V1OwnerReference.md)
 - [V1PortStatus](docs/V1PortStatus.md)
 - [V1alpha1AWSAuthConfig](docs/V1alpha1AWSAuthConfig.md)
 - [V1alpha1AppProject](docs/V1alpha1AppProject.md)
 - [V1alpha1AppProjectList](docs/V1alpha1AppProjectList.md)
 - [V1alpha1AppProjectSpec](docs/V1alpha1AppProjectSpec.md)
 - [V1alpha1AppProjectStatus](docs/V1alpha1AppProjectStatus.md)
 - [V1alpha1Application](docs/V1alpha1Application.md)
 - [V1alpha1ApplicationCondition](docs/V1alpha1ApplicationCondition.md)
 - [V1alpha1ApplicationDestination](docs/V1alpha1ApplicationDestination.md)
 - [V1alpha1ApplicationList](docs/V1alpha1ApplicationList.md)
 - [V1alpha1ApplicationSource](docs/V1alpha1ApplicationSource.md)
 - [V1alpha1ApplicationSourceDirectory](docs/V1alpha1ApplicationSourceDirectory.md)
 - [V1alpha1ApplicationSourceHelm](docs/V1alpha1ApplicationSourceHelm.md)
 - [V1alpha1ApplicationSourceJsonnet](docs/V1alpha1ApplicationSourceJsonnet.md)
 - [V1alpha1ApplicationSourceKsonnet](docs/V1alpha1ApplicationSourceKsonnet.md)
 - [V1alpha1ApplicationSourceKustomize](docs/V1alpha1ApplicationSourceKustomize.md)
 - [V1alpha1ApplicationSourcePlugin](docs/V1alpha1ApplicationSourcePlugin.md)
 - [V1alpha1ApplicationSpec](docs/V1alpha1ApplicationSpec.md)
 - [V1alpha1ApplicationStatus](docs/V1alpha1ApplicationStatus.md)
 - [V1alpha1ApplicationSummary](docs/V1alpha1ApplicationSummary.md)
 - [V1alpha1ApplicationTree](docs/V1alpha1ApplicationTree.md)
 - [V1alpha1ApplicationWatchEvent](docs/V1alpha1ApplicationWatchEvent.md)
 - [V1alpha1Backoff](docs/V1alpha1Backoff.md)
 - [V1alpha1Cluster](docs/V1alpha1Cluster.md)
 - [V1alpha1ClusterCacheInfo](docs/V1alpha1ClusterCacheInfo.md)
 - [V1alpha1ClusterConfig](docs/V1alpha1ClusterConfig.md)
 - [V1alpha1ClusterInfo](docs/V1alpha1ClusterInfo.md)
 - [V1alpha1ClusterList](docs/V1alpha1ClusterList.md)
 - [V1alpha1Command](docs/V1alpha1Command.md)
 - [V1alpha1ComparedTo](docs/V1alpha1ComparedTo.md)
 - [V1alpha1ConfigManagementPlugin](docs/V1alpha1ConfigManagementPlugin.md)
 - [V1alpha1ConnectionState](docs/V1alpha1ConnectionState.md)
 - [V1alpha1ExecProviderConfig](docs/V1alpha1ExecProviderConfig.md)
 - [V1alpha1GnuPGPublicKey](docs/V1alpha1GnuPGPublicKey.md)
 - [V1alpha1GnuPGPublicKeyList](docs/V1alpha1GnuPGPublicKeyList.md)
 - [V1alpha1HealthStatus](docs/V1alpha1HealthStatus.md)
 - [V1alpha1HelmFileParameter](docs/V1alpha1HelmFileParameter.md)
 - [V1alpha1HelmParameter](docs/V1alpha1HelmParameter.md)
 - [V1alpha1HostInfo](docs/V1alpha1HostInfo.md)
 - [V1alpha1HostResourceInfo](docs/V1alpha1HostResourceInfo.md)
 - [V1alpha1Info](docs/V1alpha1Info.md)
 - [V1alpha1InfoItem](docs/V1alpha1InfoItem.md)
 - [V1alpha1JWTToken](docs/V1alpha1JWTToken.md)
 - [V1alpha1JWTTokens](docs/V1alpha1JWTTokens.md)
 - [V1alpha1JsonnetVar](docs/V1alpha1JsonnetVar.md)
 - [V1alpha1KnownTypeField](docs/V1alpha1KnownTypeField.md)
 - [V1alpha1KsonnetParameter](docs/V1alpha1KsonnetParameter.md)
 - [V1alpha1KustomizeOptions](docs/V1alpha1KustomizeOptions.md)
 - [V1alpha1Operation](docs/V1alpha1Operation.md)
 - [V1alpha1OperationInitiator](docs/V1alpha1OperationInitiator.md)
 - [V1alpha1OperationState](docs/V1alpha1OperationState.md)
 - [V1alpha1OrphanedResourceKey](docs/V1alpha1OrphanedResourceKey.md)
 - [V1alpha1OrphanedResourcesMonitorSettings](docs/V1alpha1OrphanedResourcesMonitorSettings.md)
 - [V1alpha1OverrideIgnoreDiff](docs/V1alpha1OverrideIgnoreDiff.md)
 - [V1alpha1ProjectRole](docs/V1alpha1ProjectRole.md)
 - [V1alpha1RepoCreds](docs/V1alpha1RepoCreds.md)
 - [V1alpha1RepoCredsList](docs/V1alpha1RepoCredsList.md)
 - [V1alpha1Repository](docs/V1alpha1Repository.md)
 - [V1alpha1RepositoryCertificate](docs/V1alpha1RepositoryCertificate.md)
 - [V1alpha1RepositoryCertificateList](docs/V1alpha1RepositoryCertificateList.md)
 - [V1alpha1RepositoryList](docs/V1alpha1RepositoryList.md)
 - [V1alpha1ResourceAction](docs/V1alpha1ResourceAction.md)
 - [V1alpha1ResourceActionParam](docs/V1alpha1ResourceActionParam.md)
 - [V1alpha1ResourceDiff](docs/V1alpha1ResourceDiff.md)
 - [V1alpha1ResourceIgnoreDifferences](docs/V1alpha1ResourceIgnoreDifferences.md)
 - [V1alpha1ResourceNetworkingInfo](docs/V1alpha1ResourceNetworkingInfo.md)
 - [V1alpha1ResourceNode](docs/V1alpha1ResourceNode.md)
 - [V1alpha1ResourceOverride](docs/V1alpha1ResourceOverride.md)
 - [V1alpha1ResourceRef](docs/V1alpha1ResourceRef.md)
 - [V1alpha1ResourceResult](docs/V1alpha1ResourceResult.md)
 - [V1alpha1ResourceStatus](docs/V1alpha1ResourceStatus.md)
 - [V1alpha1RetryStrategy](docs/V1alpha1RetryStrategy.md)
 - [V1alpha1RevisionHistory](docs/V1alpha1RevisionHistory.md)
 - [V1alpha1RevisionMetadata](docs/V1alpha1RevisionMetadata.md)
 - [V1alpha1SignatureKey](docs/V1alpha1SignatureKey.md)
 - [V1alpha1SyncOperation](docs/V1alpha1SyncOperation.md)
 - [V1alpha1SyncOperationResource](docs/V1alpha1SyncOperationResource.md)
 - [V1alpha1SyncOperationResult](docs/V1alpha1SyncOperationResult.md)
 - [V1alpha1SyncPolicy](docs/V1alpha1SyncPolicy.md)
 - [V1alpha1SyncPolicyAutomated](docs/V1alpha1SyncPolicyAutomated.md)
 - [V1alpha1SyncStatus](docs/V1alpha1SyncStatus.md)
 - [V1alpha1SyncStrategy](docs/V1alpha1SyncStrategy.md)
 - [V1alpha1SyncStrategyApply](docs/V1alpha1SyncStrategyApply.md)
 - [V1alpha1SyncStrategyHook](docs/V1alpha1SyncStrategyHook.md)
 - [V1alpha1SyncWindow](docs/V1alpha1SyncWindow.md)
 - [V1alpha1TLSClientConfig](docs/V1alpha1TLSClientConfig.md)
 - [VersionVersionMessage](docs/VersionVersionMessage.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in argocd_python_client.apis and argocd_python_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from argocd_python_client.api.default_api import DefaultApi`
- `from argocd_python_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import argocd_python_client
from argocd_python_client.apis import *
from argocd_python_client.models import *
```

