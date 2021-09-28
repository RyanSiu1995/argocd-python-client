# argocd_python_client.ApplicationServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_service_create**](ApplicationServiceApi.md#application_service_create) | **POST** /api/v1/applications | Create creates an application
[**application_service_delete**](ApplicationServiceApi.md#application_service_delete) | **DELETE** /api/v1/applications/{name} | Delete deletes an application
[**application_service_delete_resource**](ApplicationServiceApi.md#application_service_delete_resource) | **DELETE** /api/v1/applications/{name}/resource | DeleteResource deletes a single application resource
[**application_service_get**](ApplicationServiceApi.md#application_service_get) | **GET** /api/v1/applications/{name} | Get returns an application by name
[**application_service_get_application_sync_windows**](ApplicationServiceApi.md#application_service_get_application_sync_windows) | **GET** /api/v1/applications/{name}/syncwindows | Get returns sync windows of the application
[**application_service_get_manifests**](ApplicationServiceApi.md#application_service_get_manifests) | **GET** /api/v1/applications/{name}/manifests | GetManifests returns application manifests
[**application_service_get_resource**](ApplicationServiceApi.md#application_service_get_resource) | **GET** /api/v1/applications/{name}/resource | GetResource returns single application resource
[**application_service_list**](ApplicationServiceApi.md#application_service_list) | **GET** /api/v1/applications | List returns list of applications
[**application_service_list_resource_actions**](ApplicationServiceApi.md#application_service_list_resource_actions) | **GET** /api/v1/applications/{name}/resource/actions | ListResourceActions returns list of resource actions
[**application_service_list_resource_events**](ApplicationServiceApi.md#application_service_list_resource_events) | **GET** /api/v1/applications/{name}/events | ListResourceEvents returns a list of event resources
[**application_service_managed_resources**](ApplicationServiceApi.md#application_service_managed_resources) | **GET** /api/v1/applications/{applicationName}/managed-resources | ManagedResources returns list of managed resources
[**application_service_patch**](ApplicationServiceApi.md#application_service_patch) | **PATCH** /api/v1/applications/{name} | Patch patch an application
[**application_service_patch_resource**](ApplicationServiceApi.md#application_service_patch_resource) | **POST** /api/v1/applications/{name}/resource | PatchResource patch single application resource
[**application_service_pod_logs**](ApplicationServiceApi.md#application_service_pod_logs) | **GET** /api/v1/applications/{name}/pods/{podName}/logs | PodLogs returns stream of log entries for the specified pod. Pod
[**application_service_pod_logs2**](ApplicationServiceApi.md#application_service_pod_logs2) | **GET** /api/v1/applications/{name}/logs | PodLogs returns stream of log entries for the specified pod. Pod
[**application_service_resource_tree**](ApplicationServiceApi.md#application_service_resource_tree) | **GET** /api/v1/applications/{applicationName}/resource-tree | ResourceTree returns resource tree
[**application_service_revision_metadata**](ApplicationServiceApi.md#application_service_revision_metadata) | **GET** /api/v1/applications/{name}/revisions/{revision}/metadata | Get the meta-data (author, date, tags, message) for a specific revision of the application
[**application_service_rollback**](ApplicationServiceApi.md#application_service_rollback) | **POST** /api/v1/applications/{name}/rollback | Rollback syncs an application to its target state
[**application_service_run_resource_action**](ApplicationServiceApi.md#application_service_run_resource_action) | **POST** /api/v1/applications/{name}/resource/actions | RunResourceAction run resource action
[**application_service_sync**](ApplicationServiceApi.md#application_service_sync) | **POST** /api/v1/applications/{name}/sync | Sync syncs an application to its target state
[**application_service_terminate_operation**](ApplicationServiceApi.md#application_service_terminate_operation) | **DELETE** /api/v1/applications/{name}/operation | TerminateOperation terminates the currently running operation
[**application_service_update**](ApplicationServiceApi.md#application_service_update) | **PUT** /api/v1/applications/{application.metadata.name} | Update updates an application
[**application_service_update_spec**](ApplicationServiceApi.md#application_service_update_spec) | **PUT** /api/v1/applications/{name}/spec | UpdateSpec updates an application spec
[**application_service_watch**](ApplicationServiceApi.md#application_service_watch) | **GET** /api/v1/stream/applications | Watch returns stream of application change events
[**application_service_watch_resource_tree**](ApplicationServiceApi.md#application_service_watch_resource_tree) | **GET** /api/v1/stream/applications/{applicationName}/resource-tree | Watch returns stream of application resource tree


# **application_service_create**
> V1alpha1Application application_service_create(body)

Create creates an application

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.v1alpha1_application import V1alpha1Application
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    body = V1alpha1Application(
        metadata=V1ObjectMeta(
            annotations={
                "key": "key_example",
            },
            cluster_name="cluster_name_example",
            creation_timestamp="creation_timestamp_example",
            deletion_grace_period_seconds="deletion_grace_period_seconds_example",
            deletion_timestamp="deletion_timestamp_example",
            finalizers=[
                "finalizers_example",
            ],
            generate_name="generate_name_example",
            labels={
                "key": "key_example",
            },
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=V1FieldsV1(
                        raw='YQ==',
                    ),
                    manager="manager_example",
                    operation="operation_example",
                    time="time_example",
                ),
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                ),
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        operation=V1alpha1Operation(
            info=[
                V1alpha1Info(
                    name="name_example",
                    value="value_example",
                ),
            ],
            initiated_by=V1alpha1OperationInitiator(
                automated=True,
                username="username_example",
            ),
            retry=V1alpha1RetryStrategy(
                backoff=V1alpha1Backoff(
                    duration="duration_example",
                    factor="factor_example",
                    max_duration="max_duration_example",
                ),
            ),
            sync=V1alpha1SyncOperation(
                dry_run=True,
                manifests=[
                    "manifests_example",
                ],
                prune=True,
                resources=[
                    V1alpha1SyncOperationResource(
                        group="group_example",
                        kind="kind_example",
                        name="name_example",
                        namespace="namespace_example",
                    ),
                ],
                revision="revision_example",
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
                sync_options=[
                    "sync_options_example",
                ],
                sync_strategy=V1alpha1SyncStrategy(
                    apply=V1alpha1SyncStrategyApply(
                        force=True,
                    ),
                    hook=V1alpha1SyncStrategyHook(
                        sync_strategy_apply=V1alpha1SyncStrategyApply(
                            force=True,
                        ),
                    ),
                ),
            ),
        ),
        spec=V1alpha1ApplicationSpec(
            destination=V1alpha1ApplicationDestination(
                name="name_example",
                namespace="namespace_example",
                server="server_example",
            ),
            ignore_differences=[
                V1alpha1ResourceIgnoreDifferences(
                    group="group_example",
                    json_pointers=[
                        "json_pointers_example",
                    ],
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                ),
            ],
            info=[
                V1alpha1Info(
                    name="name_example",
                    value="value_example",
                ),
            ],
            project="project_example",
            revision_history_limit="revision_history_limit_example",
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
            sync_policy=V1alpha1SyncPolicy(
                automated=V1alpha1SyncPolicyAutomated(
                    allow_empty=True,
                    prune=True,
                    self_heal=True,
                ),
                retry=V1alpha1RetryStrategy(
                    backoff=V1alpha1Backoff(
                        duration="duration_example",
                        factor="factor_example",
                        max_duration="max_duration_example",
                    ),
                ),
                sync_options=[
                    "sync_options_example",
                ],
            ),
        ),
        status=V1alpha1ApplicationStatus(
            conditions=[
                V1alpha1ApplicationCondition(
                    last_transition_time="last_transition_time_example",
                    message="message_example",
                    type="type_example",
                ),
            ],
            health=V1alpha1HealthStatus(
                message="message_example",
                status="status_example",
            ),
            history=[
                V1alpha1RevisionHistory(
                    deploy_started_at="deploy_started_at_example",
                    deployed_at="deployed_at_example",
                    id="id_example",
                    revision="revision_example",
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
                ),
            ],
            observed_at="observed_at_example",
            operation_state=V1alpha1OperationState(
                finished_at="finished_at_example",
                message="message_example",
                operation=V1alpha1Operation(
                    info=[
                        V1alpha1Info(
                            name="name_example",
                            value="value_example",
                        ),
                    ],
                    initiated_by=V1alpha1OperationInitiator(
                        automated=True,
                        username="username_example",
                    ),
                    retry=V1alpha1RetryStrategy(
                        backoff=V1alpha1Backoff(
                            duration="duration_example",
                            factor="factor_example",
                            max_duration="max_duration_example",
                        ),
                    ),
                    sync=V1alpha1SyncOperation(
                        dry_run=True,
                        manifests=[
                            "manifests_example",
                        ],
                        prune=True,
                        resources=[
                            V1alpha1SyncOperationResource(
                                group="group_example",
                                kind="kind_example",
                                name="name_example",
                                namespace="namespace_example",
                            ),
                        ],
                        revision="revision_example",
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
                        sync_options=[
                            "sync_options_example",
                        ],
                        sync_strategy=V1alpha1SyncStrategy(
                            apply=V1alpha1SyncStrategyApply(
                                force=True,
                            ),
                            hook=V1alpha1SyncStrategyHook(
                                sync_strategy_apply=V1alpha1SyncStrategyApply(
                                    force=True,
                                ),
                            ),
                        ),
                    ),
                ),
                phase="phase_example",
                retry_count="retry_count_example",
                started_at="started_at_example",
                sync_result=V1alpha1SyncOperationResult(
                    resources=[
                        V1alpha1ResourceResult(
                            group="group_example",
                            hook_phase="hook_phase_example",
                            hook_type="hook_type_example",
                            kind="kind_example",
                            message="message_example",
                            name="name_example",
                            namespace="namespace_example",
                            status="status_example",
                            sync_phase="sync_phase_example",
                            version="version_example",
                        ),
                    ],
                    revision="revision_example",
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
                ),
            ),
            reconciled_at="reconciled_at_example",
            resources=[
                V1alpha1ResourceStatus(
                    group="group_example",
                    health=V1alpha1HealthStatus(
                        message="message_example",
                        status="status_example",
                    ),
                    hook=True,
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                    requires_pruning=True,
                    status="status_example",
                    version="version_example",
                ),
            ],
            source_type="source_type_example",
            summary=V1alpha1ApplicationSummary(
                external_urls=[
                    "external_urls_example",
                ],
                images=[
                    "images_example",
                ],
            ),
            sync=V1alpha1SyncStatus(
                compared_to=V1alpha1ComparedTo(
                    destination=V1alpha1ApplicationDestination(
                        name="name_example",
                        namespace="namespace_example",
                        server="server_example",
                    ),
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
                ),
                revision="revision_example",
                status="status_example",
            ),
        ),
    ) # V1alpha1Application | 
    upsert = True # bool |  (optional)
    validate = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create creates an application
        api_response = api_instance.application_service_create(body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create creates an application
        api_response = api_instance.application_service_create(body, upsert=upsert, validate=validate)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1Application**](V1alpha1Application.md)|  |
 **upsert** | **bool**|  | [optional]
 **validate** | **bool**|  | [optional]

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

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

# **application_service_delete**
> bool, date, datetime, dict, float, int, list, str, none_type application_service_delete(name)

Delete deletes an application

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    cascade = True # bool |  (optional)
    propagation_policy = "propagationPolicy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete deletes an application
        api_response = api_instance.application_service_delete(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete deletes an application
        api_response = api_instance.application_service_delete(name, cascade=cascade, propagation_policy=propagation_policy)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **cascade** | **bool**|  | [optional]
 **propagation_policy** | **str**|  | [optional]

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

# **application_service_delete_resource**
> bool, date, datetime, dict, float, int, list, str, none_type application_service_delete_resource(name)

DeleteResource deletes a single application resource

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    namespace = "namespace_example" # str |  (optional)
    resource_name = "resourceName_example" # str |  (optional)
    version = "version_example" # str |  (optional)
    group = "group_example" # str |  (optional)
    kind = "kind_example" # str |  (optional)
    force = True # bool |  (optional)
    orphan = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # DeleteResource deletes a single application resource
        api_response = api_instance.application_service_delete_resource(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_delete_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DeleteResource deletes a single application resource
        api_response = api_instance.application_service_delete_resource(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, force=force, orphan=orphan)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_delete_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **namespace** | **str**|  | [optional]
 **resource_name** | **str**|  | [optional]
 **version** | **str**|  | [optional]
 **group** | **str**|  | [optional]
 **kind** | **str**|  | [optional]
 **force** | **bool**|  | [optional]
 **orphan** | **bool**|  | [optional]

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

# **application_service_get**
> V1alpha1Application application_service_get(name)

Get returns an application by name

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.v1alpha1_application import V1alpha1Application
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | the application's name
    refresh = "refresh_example" # str | forces application reconciliation if set to true. (optional)
    project = [
        "project_example",
    ] # [str] | the project names to restrict returned list applications. (optional)
    resource_version = "resourceVersion_example" # str | when specified with a watch call, shows changes that occur after that particular version of a resource. (optional)
    selector = "selector_example" # str | the selector to to restrict returned list to applications only with matched labels. (optional)
    repo = "repo_example" # str | the repoURL to restrict returned list applications. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get returns an application by name
        api_response = api_instance.application_service_get(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get returns an application by name
        api_response = api_instance.application_service_get(name, refresh=refresh, project=project, resource_version=resource_version, selector=selector, repo=repo)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the application&#39;s name |
 **refresh** | **str**| forces application reconciliation if set to true. | [optional]
 **project** | **[str]**| the project names to restrict returned list applications. | [optional]
 **resource_version** | **str**| when specified with a watch call, shows changes that occur after that particular version of a resource. | [optional]
 **selector** | **str**| the selector to to restrict returned list to applications only with matched labels. | [optional]
 **repo** | **str**| the repoURL to restrict returned list applications. | [optional]

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

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

# **application_service_get_application_sync_windows**
> ApplicationApplicationSyncWindowsResponse application_service_get_application_sync_windows(name)

Get returns sync windows of the application

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.application_application_sync_windows_response import ApplicationApplicationSyncWindowsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get returns sync windows of the application
        api_response = api_instance.application_service_get_application_sync_windows(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_get_application_sync_windows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**ApplicationApplicationSyncWindowsResponse**](ApplicationApplicationSyncWindowsResponse.md)

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

# **application_service_get_manifests**
> RepositoryManifestResponse application_service_get_manifests(name)

GetManifests returns application manifests

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.repository_manifest_response import RepositoryManifestResponse
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    revision = "revision_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # GetManifests returns application manifests
        api_response = api_instance.application_service_get_manifests(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_get_manifests: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GetManifests returns application manifests
        api_response = api_instance.application_service_get_manifests(name, revision=revision)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_get_manifests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **revision** | **str**|  | [optional]

### Return type

[**RepositoryManifestResponse**](RepositoryManifestResponse.md)

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

# **application_service_get_resource**
> ApplicationApplicationResourceResponse application_service_get_resource(name)

GetResource returns single application resource

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.application_application_resource_response import ApplicationApplicationResourceResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    namespace = "namespace_example" # str |  (optional)
    resource_name = "resourceName_example" # str |  (optional)
    version = "version_example" # str |  (optional)
    group = "group_example" # str |  (optional)
    kind = "kind_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # GetResource returns single application resource
        api_response = api_instance.application_service_get_resource(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_get_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GetResource returns single application resource
        api_response = api_instance.application_service_get_resource(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_get_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **namespace** | **str**|  | [optional]
 **resource_name** | **str**|  | [optional]
 **version** | **str**|  | [optional]
 **group** | **str**|  | [optional]
 **kind** | **str**|  | [optional]

### Return type

[**ApplicationApplicationResourceResponse**](ApplicationApplicationResourceResponse.md)

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

# **application_service_list**
> V1alpha1ApplicationList application_service_list()

List returns list of applications

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.v1alpha1_application_list import V1alpha1ApplicationList
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | the application's name. (optional)
    refresh = "refresh_example" # str | forces application reconciliation if set to true. (optional)
    project = [
        "project_example",
    ] # [str] | the project names to restrict returned list applications. (optional)
    resource_version = "resourceVersion_example" # str | when specified with a watch call, shows changes that occur after that particular version of a resource. (optional)
    selector = "selector_example" # str | the selector to to restrict returned list to applications only with matched labels. (optional)
    repo = "repo_example" # str | the repoURL to restrict returned list applications. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List returns list of applications
        api_response = api_instance.application_service_list(name=name, refresh=refresh, project=project, resource_version=resource_version, selector=selector, repo=repo)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the application&#39;s name. | [optional]
 **refresh** | **str**| forces application reconciliation if set to true. | [optional]
 **project** | **[str]**| the project names to restrict returned list applications. | [optional]
 **resource_version** | **str**| when specified with a watch call, shows changes that occur after that particular version of a resource. | [optional]
 **selector** | **str**| the selector to to restrict returned list to applications only with matched labels. | [optional]
 **repo** | **str**| the repoURL to restrict returned list applications. | [optional]

### Return type

[**V1alpha1ApplicationList**](V1alpha1ApplicationList.md)

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

# **application_service_list_resource_actions**
> ApplicationResourceActionsListResponse application_service_list_resource_actions(name)

ListResourceActions returns list of resource actions

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.application_resource_actions_list_response import ApplicationResourceActionsListResponse
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    namespace = "namespace_example" # str |  (optional)
    resource_name = "resourceName_example" # str |  (optional)
    version = "version_example" # str |  (optional)
    group = "group_example" # str |  (optional)
    kind = "kind_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ListResourceActions returns list of resource actions
        api_response = api_instance.application_service_list_resource_actions(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_list_resource_actions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ListResourceActions returns list of resource actions
        api_response = api_instance.application_service_list_resource_actions(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_list_resource_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **namespace** | **str**|  | [optional]
 **resource_name** | **str**|  | [optional]
 **version** | **str**|  | [optional]
 **group** | **str**|  | [optional]
 **kind** | **str**|  | [optional]

### Return type

[**ApplicationResourceActionsListResponse**](ApplicationResourceActionsListResponse.md)

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

# **application_service_list_resource_events**
> V1EventList application_service_list_resource_events(name)

ListResourceEvents returns a list of event resources

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.v1_event_list import V1EventList
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    resource_namespace = "resourceNamespace_example" # str |  (optional)
    resource_name = "resourceName_example" # str |  (optional)
    resource_uid = "resourceUID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ListResourceEvents returns a list of event resources
        api_response = api_instance.application_service_list_resource_events(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_list_resource_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ListResourceEvents returns a list of event resources
        api_response = api_instance.application_service_list_resource_events(name, resource_namespace=resource_namespace, resource_name=resource_name, resource_uid=resource_uid)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_list_resource_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **resource_namespace** | **str**|  | [optional]
 **resource_name** | **str**|  | [optional]
 **resource_uid** | **str**|  | [optional]

### Return type

[**V1EventList**](V1EventList.md)

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

# **application_service_managed_resources**
> ApplicationManagedResourcesResponse application_service_managed_resources(application_name)

ManagedResources returns list of managed resources

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.application_managed_resources_response import ApplicationManagedResourcesResponse
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    application_name = "applicationName_example" # str | 
    namespace = "namespace_example" # str |  (optional)
    name = "name_example" # str |  (optional)
    version = "version_example" # str |  (optional)
    group = "group_example" # str |  (optional)
    kind = "kind_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ManagedResources returns list of managed resources
        api_response = api_instance.application_service_managed_resources(application_name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_managed_resources: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ManagedResources returns list of managed resources
        api_response = api_instance.application_service_managed_resources(application_name, namespace=namespace, name=name, version=version, group=group, kind=kind)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_managed_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  |
 **namespace** | **str**|  | [optional]
 **name** | **str**|  | [optional]
 **version** | **str**|  | [optional]
 **group** | **str**|  | [optional]
 **kind** | **str**|  | [optional]

### Return type

[**ApplicationManagedResourcesResponse**](ApplicationManagedResourcesResponse.md)

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

# **application_service_patch**
> V1alpha1Application application_service_patch(name, body)

Patch patch an application

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.v1alpha1_application import V1alpha1Application
from argocd_python_client.model.application_application_patch_request import ApplicationApplicationPatchRequest
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    body = ApplicationApplicationPatchRequest(
        name="name_example",
        patch="patch_example",
        patch_type="patch_type_example",
    ) # ApplicationApplicationPatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Patch patch an application
        api_response = api_instance.application_service_patch(name, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **body** | [**ApplicationApplicationPatchRequest**](ApplicationApplicationPatchRequest.md)|  |

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

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

# **application_service_patch_resource**
> ApplicationApplicationResourceResponse application_service_patch_resource(name, body)

PatchResource patch single application resource

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.application_application_resource_response import ApplicationApplicationResourceResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    body = "body_example" # str | 
    namespace = "namespace_example" # str |  (optional)
    resource_name = "resourceName_example" # str |  (optional)
    version = "version_example" # str |  (optional)
    group = "group_example" # str |  (optional)
    kind = "kind_example" # str |  (optional)
    patch_type = "patchType_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # PatchResource patch single application resource
        api_response = api_instance.application_service_patch_resource(name, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_patch_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # PatchResource patch single application resource
        api_response = api_instance.application_service_patch_resource(name, body, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, patch_type=patch_type)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_patch_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **body** | **str**|  |
 **namespace** | **str**|  | [optional]
 **resource_name** | **str**|  | [optional]
 **version** | **str**|  | [optional]
 **group** | **str**|  | [optional]
 **kind** | **str**|  | [optional]
 **patch_type** | **str**|  | [optional]

### Return type

[**ApplicationApplicationResourceResponse**](ApplicationApplicationResourceResponse.md)

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

# **application_service_pod_logs**
> StreamResultOfApplicationLogEntry application_service_pod_logs(name, pod_name)

PodLogs returns stream of log entries for the specified pod. Pod

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.stream_result_of_application_log_entry import StreamResultOfApplicationLogEntry
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    pod_name = "podName_example" # str | 
    namespace = "namespace_example" # str |  (optional)
    container = "container_example" # str |  (optional)
    since_seconds = "sinceSeconds_example" # str |  (optional)
    since_time_seconds = "sinceTime.seconds_example" # str | Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. (optional)
    since_time_nanos = 1 # int | Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. (optional)
    tail_lines = "tailLines_example" # str |  (optional)
    follow = True # bool |  (optional)
    until_time = "untilTime_example" # str |  (optional)
    filter = "filter_example" # str |  (optional)
    kind = "kind_example" # str |  (optional)
    group = "group_example" # str |  (optional)
    resource_name = "resourceName_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # PodLogs returns stream of log entries for the specified pod. Pod
        api_response = api_instance.application_service_pod_logs(name, pod_name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_pod_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # PodLogs returns stream of log entries for the specified pod. Pod
        api_response = api_instance.application_service_pod_logs(name, pod_name, namespace=namespace, container=container, since_seconds=since_seconds, since_time_seconds=since_time_seconds, since_time_nanos=since_time_nanos, tail_lines=tail_lines, follow=follow, until_time=until_time, filter=filter, kind=kind, group=group, resource_name=resource_name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_pod_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **pod_name** | **str**|  |
 **namespace** | **str**|  | [optional]
 **container** | **str**|  | [optional]
 **since_seconds** | **str**|  | [optional]
 **since_time_seconds** | **str**| Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. | [optional]
 **since_time_nanos** | **int**| Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. | [optional]
 **tail_lines** | **str**|  | [optional]
 **follow** | **bool**|  | [optional]
 **until_time** | **str**|  | [optional]
 **filter** | **str**|  | [optional]
 **kind** | **str**|  | [optional]
 **group** | **str**|  | [optional]
 **resource_name** | **str**|  | [optional]

### Return type

[**StreamResultOfApplicationLogEntry**](StreamResultOfApplicationLogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_pod_logs2**
> StreamResultOfApplicationLogEntry application_service_pod_logs2(name)

PodLogs returns stream of log entries for the specified pod. Pod

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.stream_result_of_application_log_entry import StreamResultOfApplicationLogEntry
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    namespace = "namespace_example" # str |  (optional)
    pod_name = "podName_example" # str |  (optional)
    container = "container_example" # str |  (optional)
    since_seconds = "sinceSeconds_example" # str |  (optional)
    since_time_seconds = "sinceTime.seconds_example" # str | Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. (optional)
    since_time_nanos = 1 # int | Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. (optional)
    tail_lines = "tailLines_example" # str |  (optional)
    follow = True # bool |  (optional)
    until_time = "untilTime_example" # str |  (optional)
    filter = "filter_example" # str |  (optional)
    kind = "kind_example" # str |  (optional)
    group = "group_example" # str |  (optional)
    resource_name = "resourceName_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # PodLogs returns stream of log entries for the specified pod. Pod
        api_response = api_instance.application_service_pod_logs2(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_pod_logs2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # PodLogs returns stream of log entries for the specified pod. Pod
        api_response = api_instance.application_service_pod_logs2(name, namespace=namespace, pod_name=pod_name, container=container, since_seconds=since_seconds, since_time_seconds=since_time_seconds, since_time_nanos=since_time_nanos, tail_lines=tail_lines, follow=follow, until_time=until_time, filter=filter, kind=kind, group=group, resource_name=resource_name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_pod_logs2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **namespace** | **str**|  | [optional]
 **pod_name** | **str**|  | [optional]
 **container** | **str**|  | [optional]
 **since_seconds** | **str**|  | [optional]
 **since_time_seconds** | **str**| Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. | [optional]
 **since_time_nanos** | **int**| Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. | [optional]
 **tail_lines** | **str**|  | [optional]
 **follow** | **bool**|  | [optional]
 **until_time** | **str**|  | [optional]
 **filter** | **str**|  | [optional]
 **kind** | **str**|  | [optional]
 **group** | **str**|  | [optional]
 **resource_name** | **str**|  | [optional]

### Return type

[**StreamResultOfApplicationLogEntry**](StreamResultOfApplicationLogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_resource_tree**
> V1alpha1ApplicationTree application_service_resource_tree(application_name)

ResourceTree returns resource tree

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.v1alpha1_application_tree import V1alpha1ApplicationTree
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    application_name = "applicationName_example" # str | 
    namespace = "namespace_example" # str |  (optional)
    name = "name_example" # str |  (optional)
    version = "version_example" # str |  (optional)
    group = "group_example" # str |  (optional)
    kind = "kind_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # ResourceTree returns resource tree
        api_response = api_instance.application_service_resource_tree(application_name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_resource_tree: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ResourceTree returns resource tree
        api_response = api_instance.application_service_resource_tree(application_name, namespace=namespace, name=name, version=version, group=group, kind=kind)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_resource_tree: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  |
 **namespace** | **str**|  | [optional]
 **name** | **str**|  | [optional]
 **version** | **str**|  | [optional]
 **group** | **str**|  | [optional]
 **kind** | **str**|  | [optional]

### Return type

[**V1alpha1ApplicationTree**](V1alpha1ApplicationTree.md)

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

# **application_service_revision_metadata**
> V1alpha1RevisionMetadata application_service_revision_metadata(name, revision)

Get the meta-data (author, date, tags, message) for a specific revision of the application

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.v1alpha1_revision_metadata import V1alpha1RevisionMetadata
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | the application's name
    revision = "revision_example" # str | the revision of the app

    # example passing only required values which don't have defaults set
    try:
        # Get the meta-data (author, date, tags, message) for a specific revision of the application
        api_response = api_instance.application_service_revision_metadata(name, revision)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_revision_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the application&#39;s name |
 **revision** | **str**| the revision of the app |

### Return type

[**V1alpha1RevisionMetadata**](V1alpha1RevisionMetadata.md)

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

# **application_service_rollback**
> V1alpha1Application application_service_rollback(name, body)

Rollback syncs an application to its target state

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.v1alpha1_application import V1alpha1Application
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.application_application_rollback_request import ApplicationApplicationRollbackRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    body = ApplicationApplicationRollbackRequest(
        dry_run=True,
        id="id_example",
        name="name_example",
        prune=True,
    ) # ApplicationApplicationRollbackRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Rollback syncs an application to its target state
        api_response = api_instance.application_service_rollback(name, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_rollback: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **body** | [**ApplicationApplicationRollbackRequest**](ApplicationApplicationRollbackRequest.md)|  |

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

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

# **application_service_run_resource_action**
> bool, date, datetime, dict, float, int, list, str, none_type application_service_run_resource_action(name, body)

RunResourceAction run resource action

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    body = "body_example" # str | 
    namespace = "namespace_example" # str |  (optional)
    resource_name = "resourceName_example" # str |  (optional)
    version = "version_example" # str |  (optional)
    group = "group_example" # str |  (optional)
    kind = "kind_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # RunResourceAction run resource action
        api_response = api_instance.application_service_run_resource_action(name, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_run_resource_action: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # RunResourceAction run resource action
        api_response = api_instance.application_service_run_resource_action(name, body, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_run_resource_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **body** | **str**|  |
 **namespace** | **str**|  | [optional]
 **resource_name** | **str**|  | [optional]
 **version** | **str**|  | [optional]
 **group** | **str**|  | [optional]
 **kind** | **str**|  | [optional]

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

# **application_service_sync**
> V1alpha1Application application_service_sync(name, body)

Sync syncs an application to its target state

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.v1alpha1_application import V1alpha1Application
from argocd_python_client.model.application_application_sync_request import ApplicationApplicationSyncRequest
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    body = ApplicationApplicationSyncRequest(
        dry_run=True,
        infos=[
            V1alpha1Info(
                name="name_example",
                value="value_example",
            ),
        ],
        manifests=[
            "manifests_example",
        ],
        name="name_example",
        prune=True,
        resources=[
            V1alpha1SyncOperationResource(
                group="group_example",
                kind="kind_example",
                name="name_example",
                namespace="namespace_example",
            ),
        ],
        retry_strategy=V1alpha1RetryStrategy(
            backoff=V1alpha1Backoff(
                duration="duration_example",
                factor="factor_example",
                max_duration="max_duration_example",
            ),
        ),
        revision="revision_example",
        strategy=V1alpha1SyncStrategy(
            apply=V1alpha1SyncStrategyApply(
                force=True,
            ),
            hook=V1alpha1SyncStrategyHook(
                sync_strategy_apply=V1alpha1SyncStrategyApply(
                    force=True,
                ),
            ),
        ),
        sync_options=ApplicationSyncOptions(
            items=[
                "items_example",
            ],
        ),
    ) # ApplicationApplicationSyncRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Sync syncs an application to its target state
        api_response = api_instance.application_service_sync(name, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **body** | [**ApplicationApplicationSyncRequest**](ApplicationApplicationSyncRequest.md)|  |

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

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

# **application_service_terminate_operation**
> bool, date, datetime, dict, float, int, list, str, none_type application_service_terminate_operation(name)

TerminateOperation terminates the currently running operation

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # TerminateOperation terminates the currently running operation
        api_response = api_instance.application_service_terminate_operation(name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_terminate_operation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

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

# **application_service_update**
> V1alpha1Application application_service_update(application_metadata_name, body)

Update updates an application

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.v1alpha1_application import V1alpha1Application
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    application_metadata_name = "application.metadata.name_example" # str | Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional
    body = V1alpha1Application(
        metadata=V1ObjectMeta(
            annotations={
                "key": "key_example",
            },
            cluster_name="cluster_name_example",
            creation_timestamp="creation_timestamp_example",
            deletion_grace_period_seconds="deletion_grace_period_seconds_example",
            deletion_timestamp="deletion_timestamp_example",
            finalizers=[
                "finalizers_example",
            ],
            generate_name="generate_name_example",
            labels={
                "key": "key_example",
            },
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=V1FieldsV1(
                        raw='YQ==',
                    ),
                    manager="manager_example",
                    operation="operation_example",
                    time="time_example",
                ),
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                ),
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        operation=V1alpha1Operation(
            info=[
                V1alpha1Info(
                    name="name_example",
                    value="value_example",
                ),
            ],
            initiated_by=V1alpha1OperationInitiator(
                automated=True,
                username="username_example",
            ),
            retry=V1alpha1RetryStrategy(
                backoff=V1alpha1Backoff(
                    duration="duration_example",
                    factor="factor_example",
                    max_duration="max_duration_example",
                ),
            ),
            sync=V1alpha1SyncOperation(
                dry_run=True,
                manifests=[
                    "manifests_example",
                ],
                prune=True,
                resources=[
                    V1alpha1SyncOperationResource(
                        group="group_example",
                        kind="kind_example",
                        name="name_example",
                        namespace="namespace_example",
                    ),
                ],
                revision="revision_example",
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
                sync_options=[
                    "sync_options_example",
                ],
                sync_strategy=V1alpha1SyncStrategy(
                    apply=V1alpha1SyncStrategyApply(
                        force=True,
                    ),
                    hook=V1alpha1SyncStrategyHook(
                        sync_strategy_apply=V1alpha1SyncStrategyApply(
                            force=True,
                        ),
                    ),
                ),
            ),
        ),
        spec=V1alpha1ApplicationSpec(
            destination=V1alpha1ApplicationDestination(
                name="name_example",
                namespace="namespace_example",
                server="server_example",
            ),
            ignore_differences=[
                V1alpha1ResourceIgnoreDifferences(
                    group="group_example",
                    json_pointers=[
                        "json_pointers_example",
                    ],
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                ),
            ],
            info=[
                V1alpha1Info(
                    name="name_example",
                    value="value_example",
                ),
            ],
            project="project_example",
            revision_history_limit="revision_history_limit_example",
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
            sync_policy=V1alpha1SyncPolicy(
                automated=V1alpha1SyncPolicyAutomated(
                    allow_empty=True,
                    prune=True,
                    self_heal=True,
                ),
                retry=V1alpha1RetryStrategy(
                    backoff=V1alpha1Backoff(
                        duration="duration_example",
                        factor="factor_example",
                        max_duration="max_duration_example",
                    ),
                ),
                sync_options=[
                    "sync_options_example",
                ],
            ),
        ),
        status=V1alpha1ApplicationStatus(
            conditions=[
                V1alpha1ApplicationCondition(
                    last_transition_time="last_transition_time_example",
                    message="message_example",
                    type="type_example",
                ),
            ],
            health=V1alpha1HealthStatus(
                message="message_example",
                status="status_example",
            ),
            history=[
                V1alpha1RevisionHistory(
                    deploy_started_at="deploy_started_at_example",
                    deployed_at="deployed_at_example",
                    id="id_example",
                    revision="revision_example",
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
                ),
            ],
            observed_at="observed_at_example",
            operation_state=V1alpha1OperationState(
                finished_at="finished_at_example",
                message="message_example",
                operation=V1alpha1Operation(
                    info=[
                        V1alpha1Info(
                            name="name_example",
                            value="value_example",
                        ),
                    ],
                    initiated_by=V1alpha1OperationInitiator(
                        automated=True,
                        username="username_example",
                    ),
                    retry=V1alpha1RetryStrategy(
                        backoff=V1alpha1Backoff(
                            duration="duration_example",
                            factor="factor_example",
                            max_duration="max_duration_example",
                        ),
                    ),
                    sync=V1alpha1SyncOperation(
                        dry_run=True,
                        manifests=[
                            "manifests_example",
                        ],
                        prune=True,
                        resources=[
                            V1alpha1SyncOperationResource(
                                group="group_example",
                                kind="kind_example",
                                name="name_example",
                                namespace="namespace_example",
                            ),
                        ],
                        revision="revision_example",
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
                        sync_options=[
                            "sync_options_example",
                        ],
                        sync_strategy=V1alpha1SyncStrategy(
                            apply=V1alpha1SyncStrategyApply(
                                force=True,
                            ),
                            hook=V1alpha1SyncStrategyHook(
                                sync_strategy_apply=V1alpha1SyncStrategyApply(
                                    force=True,
                                ),
                            ),
                        ),
                    ),
                ),
                phase="phase_example",
                retry_count="retry_count_example",
                started_at="started_at_example",
                sync_result=V1alpha1SyncOperationResult(
                    resources=[
                        V1alpha1ResourceResult(
                            group="group_example",
                            hook_phase="hook_phase_example",
                            hook_type="hook_type_example",
                            kind="kind_example",
                            message="message_example",
                            name="name_example",
                            namespace="namespace_example",
                            status="status_example",
                            sync_phase="sync_phase_example",
                            version="version_example",
                        ),
                    ],
                    revision="revision_example",
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
                ),
            ),
            reconciled_at="reconciled_at_example",
            resources=[
                V1alpha1ResourceStatus(
                    group="group_example",
                    health=V1alpha1HealthStatus(
                        message="message_example",
                        status="status_example",
                    ),
                    hook=True,
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                    requires_pruning=True,
                    status="status_example",
                    version="version_example",
                ),
            ],
            source_type="source_type_example",
            summary=V1alpha1ApplicationSummary(
                external_urls=[
                    "external_urls_example",
                ],
                images=[
                    "images_example",
                ],
            ),
            sync=V1alpha1SyncStatus(
                compared_to=V1alpha1ComparedTo(
                    destination=V1alpha1ApplicationDestination(
                        name="name_example",
                        namespace="namespace_example",
                        server="server_example",
                    ),
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
                ),
                revision="revision_example",
                status="status_example",
            ),
        ),
    ) # V1alpha1Application | 
    validate = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update updates an application
        api_response = api_instance.application_service_update(application_metadata_name, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update updates an application
        api_response = api_instance.application_service_update(application_metadata_name, body, validate=validate)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_metadata_name** | **str**| Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional |
 **body** | [**V1alpha1Application**](V1alpha1Application.md)|  |
 **validate** | **bool**|  | [optional]

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

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

# **application_service_update_spec**
> V1alpha1ApplicationSpec application_service_update_spec(name, body)

UpdateSpec updates an application spec

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.v1alpha1_application_spec import V1alpha1ApplicationSpec
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | 
    body = V1alpha1ApplicationSpec(
        destination=V1alpha1ApplicationDestination(
            name="name_example",
            namespace="namespace_example",
            server="server_example",
        ),
        ignore_differences=[
            V1alpha1ResourceIgnoreDifferences(
                group="group_example",
                json_pointers=[
                    "json_pointers_example",
                ],
                kind="kind_example",
                name="name_example",
                namespace="namespace_example",
            ),
        ],
        info=[
            V1alpha1Info(
                name="name_example",
                value="value_example",
            ),
        ],
        project="project_example",
        revision_history_limit="revision_history_limit_example",
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
        sync_policy=V1alpha1SyncPolicy(
            automated=V1alpha1SyncPolicyAutomated(
                allow_empty=True,
                prune=True,
                self_heal=True,
            ),
            retry=V1alpha1RetryStrategy(
                backoff=V1alpha1Backoff(
                    duration="duration_example",
                    factor="factor_example",
                    max_duration="max_duration_example",
                ),
            ),
            sync_options=[
                "sync_options_example",
            ],
        ),
    ) # V1alpha1ApplicationSpec | 
    validate = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # UpdateSpec updates an application spec
        api_response = api_instance.application_service_update_spec(name, body)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_update_spec: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UpdateSpec updates an application spec
        api_response = api_instance.application_service_update_spec(name, body, validate=validate)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_update_spec: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **body** | [**V1alpha1ApplicationSpec**](V1alpha1ApplicationSpec.md)|  |
 **validate** | **bool**|  | [optional]

### Return type

[**V1alpha1ApplicationSpec**](V1alpha1ApplicationSpec.md)

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

# **application_service_watch**
> StreamResultOfV1alpha1ApplicationWatchEvent application_service_watch()

Watch returns stream of application change events

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.runtime_error import RuntimeError
from argocd_python_client.model.stream_result_of_v1alpha1_application_watch_event import StreamResultOfV1alpha1ApplicationWatchEvent
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with argocd_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    name = "name_example" # str | the application's name. (optional)
    refresh = "refresh_example" # str | forces application reconciliation if set to true. (optional)
    project = [
        "project_example",
    ] # [str] | the project names to restrict returned list applications. (optional)
    resource_version = "resourceVersion_example" # str | when specified with a watch call, shows changes that occur after that particular version of a resource. (optional)
    selector = "selector_example" # str | the selector to to restrict returned list to applications only with matched labels. (optional)
    repo = "repo_example" # str | the repoURL to restrict returned list applications. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch returns stream of application change events
        api_response = api_instance.application_service_watch(name=name, refresh=refresh, project=project, resource_version=resource_version, selector=selector, repo=repo)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_watch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the application&#39;s name. | [optional]
 **refresh** | **str**| forces application reconciliation if set to true. | [optional]
 **project** | **[str]**| the project names to restrict returned list applications. | [optional]
 **resource_version** | **str**| when specified with a watch call, shows changes that occur after that particular version of a resource. | [optional]
 **selector** | **str**| the selector to to restrict returned list to applications only with matched labels. | [optional]
 **repo** | **str**| the repoURL to restrict returned list applications. | [optional]

### Return type

[**StreamResultOfV1alpha1ApplicationWatchEvent**](StreamResultOfV1alpha1ApplicationWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_watch_resource_tree**
> StreamResultOfV1alpha1ApplicationTree application_service_watch_resource_tree(application_name)

Watch returns stream of application resource tree

### Example

```python
import time
import argocd_python_client
from argocd_python_client.api import application_service_api
from argocd_python_client.model.stream_result_of_v1alpha1_application_tree import StreamResultOfV1alpha1ApplicationTree
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
    api_instance = application_service_api.ApplicationServiceApi(api_client)
    application_name = "applicationName_example" # str | 
    namespace = "namespace_example" # str |  (optional)
    name = "name_example" # str |  (optional)
    version = "version_example" # str |  (optional)
    group = "group_example" # str |  (optional)
    kind = "kind_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch returns stream of application resource tree
        api_response = api_instance.application_service_watch_resource_tree(application_name)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_watch_resource_tree: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Watch returns stream of application resource tree
        api_response = api_instance.application_service_watch_resource_tree(application_name, namespace=namespace, name=name, version=version, group=group, kind=kind)
        pprint(api_response)
    except argocd_python_client.ApiException as e:
        print("Exception when calling ApplicationServiceApi->application_service_watch_resource_tree: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  |
 **namespace** | **str**|  | [optional]
 **name** | **str**|  | [optional]
 **version** | **str**|  | [optional]
 **group** | **str**|  | [optional]
 **kind** | **str**|  | [optional]

### Return type

[**StreamResultOfV1alpha1ApplicationTree**](StreamResultOfV1alpha1ApplicationTree.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

