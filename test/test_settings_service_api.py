"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.settings_service_api import SettingsServiceApi  # noqa: E501


class TestSettingsServiceApi(unittest.TestCase):
    """SettingsServiceApi unit test stubs"""

    def setUp(self):
        self.api = SettingsServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_settings_service_get(self):
        """Test case for settings_service_get

        Get returns Argo CD settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
