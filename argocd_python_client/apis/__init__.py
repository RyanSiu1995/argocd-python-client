
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.account_service_api import AccountServiceApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from argocd_python_client.api.account_service_api import AccountServiceApi
from argocd_python_client.api.application_service_api import ApplicationServiceApi
from argocd_python_client.api.certificate_service_api import CertificateServiceApi
from argocd_python_client.api.cluster_service_api import ClusterServiceApi
from argocd_python_client.api.gpg_key_service_api import GPGKeyServiceApi
from argocd_python_client.api.project_service_api import ProjectServiceApi
from argocd_python_client.api.repo_creds_service_api import RepoCredsServiceApi
from argocd_python_client.api.repository_service_api import RepositoryServiceApi
from argocd_python_client.api.session_service_api import SessionServiceApi
from argocd_python_client.api.settings_service_api import SettingsServiceApi
from argocd_python_client.api.version_service_api import VersionServiceApi
