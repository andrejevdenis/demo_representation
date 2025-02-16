import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from dotenv import load_dotenv
import os

class Page_asserts:
    load_dotenv()
    login = os.getenv('LOGIN_USER')
    password = os.getenv('PASSWORD_USER')

    @allure.step("Product search and add to cart")
    def search_and_add_to_cart(self):
        with allure.step("Verify user login is displayed"):
            result = browser.all((AppiumBy.ID, 'ru.dns.shop.android:id/product_title_text'))
            result.first.should(have.text('Samsung Galaxy S24'))

        with allure.step("Check that the cart has 1 new item"):
            result=browser.all((AppiumBy.ACCESSIBILITY_ID, 'Корзина, 1 новое уведомление'))
            result.should(have.size_greater_than(0))

    @allure.step("Authorization")
    def authorization(self):

        with allure.step("Verify user login is displayed"):
            browser.element((AppiumBy.ID, 'ru.dns.shop.android:id/display_login_text')).should(have.text(f'{self.login}'))