import os
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
class Config(BaseModel):
    USER_NAME: str = os.getenv('USER_NAME')
    ACCESS_KEY: str = os.getenv('ACCESS_KEY')
    REMOTE_URL: str = os.getenv('REMOTE_URL')
    LOCAL_URL: str = os.getenv('LOCAL_URL')
    PLATFORM_NAME: str = os.getenv('PLATFORM_NAME')
    PLATFORM_VERSION: str = os.getenv('PLATFORM_VERSION', '')
    DEVICE_NAME: str = os.getenv('DEVICE_NAME')
    APP: str = os.getenv('APP')
    LOCAL_APP: str = os.path.abspath(os.path.join(os.path.dirname(__file__), os.getenv('APP_LOCAL')))
    APP_ACTIVITY: str = os.getenv('APP_ACTIVITY')
    APP_PACKAGE: str = os.getenv('APP_PACKAGE')
    REMOTE_URL_WEB: str = os.getenv('REMOTE_URL_WEB')

    def to_mobile_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'app_cloud':
            options.set_capability('remote_url', self.REMOTE_URL)
            options.set_capability('deviceName', self.DEVICE_NAME)
            options.set_capability('platformName', self.PLATFORM_NAME)
            options.set_capability('platformVersion', self.PLATFORM_VERSION)
            options.set_capability('app', self.APP)
            options.set_capability('bstack:options', {
                "projectName": "Python_project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack_test",
                "userName": self.USER_NAME,
                "accessKey": self.ACCESS_KEY
            })
            options.set_capability('appActivity', self.APP_ACTIVITY)
            options.set_capability('appPackage', self.APP_PACKAGE)

        if context == 'app_local_real':
            options.set_capability('remote_url', self.LOCAL_URL)
            options.set_capability('platformName', self.PLATFORM_NAME)
            options.set_capability('app', self.LOCAL_APP)
            options.set_capability('appActivity', self.APP_ACTIVITY)
            options.set_capability('appPackage', self.APP_PACKAGE)

        return options

config_app = Config()
