import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from dotenv import load_dotenv
import os

class Page_steps:
    load_dotenv()
    login = os.getenv('LOGIN_USER')
    password = os.getenv('PASSWORD_USER')

    @allure.step("Product search and add to cart")
    def search_and_add_to_cart(self):
        with allure.step("Open search page"):
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/confirm_current_settlement_button')).click()
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/skip_auth_button')).click()

        with allure.step("Skip_update_notification"):
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/negative_button')).click()

        with allure.step("Start search process"):
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/text_input_start_icon')).click()
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/search_edit')).type('Samsung S24')
            result = browser.all((AppiumBy.ID, 'ru.dns.shop.android:id/text'))
            result.first.should(have.text('samsung s24')).click()

        with allure.step("Add product to cart"):
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/buy_button')).click()

    @allure.step("Authorization")
    def authorization(self):
        with allure.step("Open account menu"):
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/confirm_current_settlement_button')).click()
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/login_button')).click()
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/navigate_to_password_auth_button')).click()

        with allure.step("Start authorization process"):
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/login_edit')).type(f'{self.login}')
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/password_edit')).type(f'{self.password}')
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/login_button')).click()

        with allure.step("Skip_update_notification"):
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/negative_button')).click()

        with allure.step("Go to user account page"):
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/nav_profile')).click()