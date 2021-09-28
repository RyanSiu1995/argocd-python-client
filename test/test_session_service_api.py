"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


import unittest

import argocd_python_client
from argocd_python_client.api.session_service_api import SessionServiceApi  # noqa: E501


class TestSessionServiceApi(unittest.TestCase):
    """SessionServiceApi unit test stubs"""

    def setUp(self):
        self.api = SessionServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_session_service_create(self):
        """Test case for session_service_create

        Create a new JWT for authentication and set a cookie if using HTTP  # noqa: E501
        """
        pass

    def test_session_service_delete(self):
        """Test case for session_service_delete

        Delete an existing JWT cookie if using HTTP  # noqa: E501
        """
        pass

    def test_session_service_get_user_info(self):
        """Test case for session_service_get_user_info

        Get the current user's info  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
