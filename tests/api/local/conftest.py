import os
import allure
from allure_commons._allure import step
import allure_commons
import pytest
from selene import browser, support
from tests.web.utils import attach
from dotenv import load_dotenv

@pytest.fixture(scope='function', autouse=True)
def web_management(context):
    load_dotenv()
    with allure.step('Set options'):
        if context in ('all', 'api', 'local', 'api_local'):
            browser.open(os.getenv('LOCAL_URL_WEB'))
            browser.driver.maximize_window()
            browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)
        else:
            pytest.skip()

    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    with step('Tear down app session'):
         browser.quit()