"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


import unittest

import argocd_python_client
from argocd_python_client.api.repository_service_api import RepositoryServiceApi  # noqa: E501


class TestRepositoryServiceApi(unittest.TestCase):
    """RepositoryServiceApi unit test stubs"""

    def setUp(self):
        self.api = RepositoryServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_repository_service_create_repository(self):
        """Test case for repository_service_create_repository

        CreateRepository creates a new repository configuration  # noqa: E501
        """
        pass

    def test_repository_service_delete_repository(self):
        """Test case for repository_service_delete_repository

        DeleteRepository deletes a repository from the configuration  # noqa: E501
        """
        pass

    def test_repository_service_get(self):
        """Test case for repository_service_get

        Get returns a repository or its credentials  # noqa: E501
        """
        pass

    def test_repository_service_get_app_details(self):
        """Test case for repository_service_get_app_details

        GetAppDetails returns application details by given path  # noqa: E501
        """
        pass

    def test_repository_service_get_helm_charts(self):
        """Test case for repository_service_get_helm_charts

        GetHelmCharts returns list of helm charts in the specified repository  # noqa: E501
        """
        pass

    def test_repository_service_list_apps(self):
        """Test case for repository_service_list_apps

        ListApps returns list of apps in the repe  # noqa: E501
        """
        pass

    def test_repository_service_list_refs(self):
        """Test case for repository_service_list_refs

        """
        pass

    def test_repository_service_list_repositories(self):
        """Test case for repository_service_list_repositories

        ListRepositories gets a list of all configured repositories  # noqa: E501
        """
        pass

    def test_repository_service_update_repository(self):
        """Test case for repository_service_update_repository

        UpdateRepository updates a repository configuration  # noqa: E501
        """
        pass

    def test_repository_service_validate_access(self):
        """Test case for repository_service_validate_access

        ValidateAccess validates access to a repository with given parameters  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
