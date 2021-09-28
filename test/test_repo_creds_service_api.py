"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


import unittest

import argocd_python_client
from argocd_python_client.api.repo_creds_service_api import RepoCredsServiceApi  # noqa: E501


class TestRepoCredsServiceApi(unittest.TestCase):
    """RepoCredsServiceApi unit test stubs"""

    def setUp(self):
        self.api = RepoCredsServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_repo_creds_service_create_repository_credentials(self):
        """Test case for repo_creds_service_create_repository_credentials

        CreateRepositoryCredentials creates a new repository credential set  # noqa: E501
        """
        pass

    def test_repo_creds_service_delete_repository_credentials(self):
        """Test case for repo_creds_service_delete_repository_credentials

        DeleteRepositoryCredentials deletes a repository credential set from the configuration  # noqa: E501
        """
        pass

    def test_repo_creds_service_list_repository_credentials(self):
        """Test case for repo_creds_service_list_repository_credentials

        ListRepositoryCredentials gets a list of all configured repository credential sets  # noqa: E501
        """
        pass

    def test_repo_creds_service_update_repository_credentials(self):
        """Test case for repo_creds_service_update_repository_credentials

        UpdateRepositoryCredentials updates a repository credential set  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
