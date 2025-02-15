
from dotenv import load_dotenv
import os
from allure_commons._allure import step
from selene import browser
from selene.support.conditions import have
import allure
import time
from selene.core.query import text_content

load_dotenv()
login=os.getenv('LOGIN_USER_DEMO_SHOP')
WEB_URL = os.getenv('LOCAL_URL_WEB')

class Page_asserts:
    @allure.step("Authorization")
    def authorization(self):
        with step("Assert with UI"):
            browser.open(WEB_URL)
            browser.element('[href="/customer/info"]').should(have.text(f'{login}'))
    @allure.step("Adding product to cart")
    def cart_add(self):
        with step("Check_UI_cart"):
            browser.open(WEB_URL + "/cart")
            browser.element('[class="product-name"]').should(have.text('$25 Virtual Gift Card'))
            browser.element('[class="attributes"]').should(have.text('From: Papa <papa@gmail.com>'))
            browser.element('[class="attributes"]').should(have.text('For: Mama <mama@gmail.com>'))

    @allure.step("Adding product to cart")
    def cart_add_cloud(self):
       with step("Check_UI_cart"):
            browser.open(WEB_URL + "/cart")
            browser.element('[class="product-name"]').should(have.text('$25 Virtual Gift Card'))
            text = browser.element('.attributes').get(query=text_content)
            assert text == '\n                                    From: Papa <papa@gmail.com>For: Mama <mama@gmail.com>\n                                '
    @allure.step("Clearing the cart")
    def cart_clear(self):
        with step("Check_UI_cart_empty"):
            browser.open(WEB_URL + "/cart")
            browser.element('[class="order-summary-content"]').should(have.text('Your Shopping Cart is empty!'))