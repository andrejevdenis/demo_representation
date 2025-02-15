import os
import allure
from allure_commons._allure import step
import pytest
from selene import browser
from selenium import webdriver
from tests.web.utils import attach
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv


@pytest.fixture(scope='function', autouse=True)
def web_management(context):
    load_dotenv()
    with allure.step('Set options'):
        if context in ('all', 'web', 'cloud', 'web_cloud'):
            options = Options()
            selenoid_capabilities = {
                "browserName": "chrome",
                "browserVersion": '126',
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True
                }
            }
            options.capabilities.update(selenoid_capabilities)
            browser.config.driver = webdriver.Remote(command_executor=os.getenv('REMOTE_URL_WEB'),options=options)
            browser.open(os.getenv('LOCAL_URL_WEB'))
            browser.driver.maximize_window()
            browser.config.timeout = 12
        else:
            pytest.skip()

    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    with step('Tear down app session'):
         browser.quit()

