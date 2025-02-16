import pytest

def pytest_addoption(parser):
    parser.addoption("--context", action="store",required=False, default="all", choices=['app_cloud','app_local_real','all','mobile_app','local','cloud', 'web', 'web_cloud', 'web_local', 'api', 'api_local', 'api_cloud'],
                     help="Context for load options")

@pytest.fixture
def context(request):
    return request.config.getoption("--context")