import os

import allure
from selene import browser, have
from dotenv import load_dotenv
from selene.core.query import text_content

load_dotenv()
login=os.getenv('LOGIN_USER_DEMO_SHOP')
password=os.getenv('PASSWORD_USER_DEMO_SHOP')

class Page_asserts:
    @allure.step("Authorization")
    def authorization(self):
        with allure.step("Verifi user login"):
            browser.element('[href="/customer/info"]').should(have.text(f'{login}'))

    @allure.step("Add product to cart")
    def add_product_to_cart(self):
        with (allure.step("Verifi product in cart")):
            browser.element('[class="product-name"]').should(have.text('$25 Virtual Gift Card'))
            browser.element('[class="attributes"]').should(have.text('From: Mama <mama@gmail.com>'))
            browser.element('[class="attributes"]').should(have.text('For: Papa <papa@gmail.com>'))

    @allure.step("Add product to cart")
    def add_product_to_cart_cloud(self):
        with (allure.step("Verifi product in cart")):
            browser.element('[class="product-name"]').should(have.text('$25 Virtual Gift Card'))
            text = browser.element('.attributes').get(query=text_content)
            assert text == '\n                                    From: Mama <mama@gmail.com>For: Papa <papa@gmail.com>\n                                '