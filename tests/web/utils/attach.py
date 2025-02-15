import os

import allure
from allure_commons.types import AttachmentType

def add_screenshot(browser):
    allure.attach(
        browser.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG
    )
def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

def add_html(browser):
    allure.attach(browser.driver.page_source, name="Html", attachment_type=AttachmentType.HTML)

def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')