"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import argocd_python_client
from argocd_python_client.model.v1alpha1_application_source import V1alpha1ApplicationSource
from argocd_python_client.model.v1alpha1_sync_operation_resource import V1alpha1SyncOperationResource
from argocd_python_client.model.v1alpha1_sync_strategy import V1alpha1SyncStrategy
globals()['V1alpha1ApplicationSource'] = V1alpha1ApplicationSource
globals()['V1alpha1SyncOperationResource'] = V1alpha1SyncOperationResource
globals()['V1alpha1SyncStrategy'] = V1alpha1SyncStrategy
from argocd_python_client.model.v1alpha1_sync_operation import V1alpha1SyncOperation


class TestV1alpha1SyncOperation(unittest.TestCase):
    """V1alpha1SyncOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1alpha1SyncOperation(self):
        """Test V1alpha1SyncOperation"""
        # FIXME: construct object with mandatory attributes with example values
        # model = V1alpha1SyncOperation()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
