"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import argocd_python_client
from argocd_python_client.model.v1_time import V1Time
from argocd_python_client.model.v1alpha1_application_condition import V1alpha1ApplicationCondition
from argocd_python_client.model.v1alpha1_application_summary import V1alpha1ApplicationSummary
from argocd_python_client.model.v1alpha1_health_status import V1alpha1HealthStatus
from argocd_python_client.model.v1alpha1_operation_state import V1alpha1OperationState
from argocd_python_client.model.v1alpha1_resource_status import V1alpha1ResourceStatus
from argocd_python_client.model.v1alpha1_revision_history import V1alpha1RevisionHistory
from argocd_python_client.model.v1alpha1_sync_status import V1alpha1SyncStatus
globals()['V1Time'] = V1Time
globals()['V1alpha1ApplicationCondition'] = V1alpha1ApplicationCondition
globals()['V1alpha1ApplicationSummary'] = V1alpha1ApplicationSummary
globals()['V1alpha1HealthStatus'] = V1alpha1HealthStatus
globals()['V1alpha1OperationState'] = V1alpha1OperationState
globals()['V1alpha1ResourceStatus'] = V1alpha1ResourceStatus
globals()['V1alpha1RevisionHistory'] = V1alpha1RevisionHistory
globals()['V1alpha1SyncStatus'] = V1alpha1SyncStatus
from argocd_python_client.model.v1alpha1_application_status import V1alpha1ApplicationStatus


class TestV1alpha1ApplicationStatus(unittest.TestCase):
    """V1alpha1ApplicationStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1alpha1ApplicationStatus(self):
        """Test V1alpha1ApplicationStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = V1alpha1ApplicationStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
