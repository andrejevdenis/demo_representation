import allure
from allure_commons._allure import step
from allure_commons.types import AttachmentType
import pytest
from selene import browser, support
import allure_commons
from appium import webdriver
import os
from tests.mobile_app.utils import attach

@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):

    with allure.step('Set options'):
        from config_all import config_app
        options = config_app.to_mobile_driver_options(context='app_cloud')
        if context in ('all', 'cloud', 'mobile', 'app_cloud'):
            browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
        else:
            pytest.skip()

    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)

    yield
    allure.attach(
        browser.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG
    )
    allure.attach(
        browser.driver.page_source, name='xml_dump', attachment_type=AttachmentType.XML
    )

    session_id = browser.driver.session_id

    with step('Tear down app session'):
         browser.quit()

    attach.attach_bstack_video(session_id)