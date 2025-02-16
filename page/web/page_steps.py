import os

import allure
from selene import browser
from dotenv import load_dotenv

load_dotenv()
login=os.getenv('LOGIN_USER_DEMO_SHOP')
password=os.getenv('PASSWORD_USER_DEMO_SHOP')

class Page_steps:
    @allure.step("Authorization")
    def authorization(self):
        with allure.step("Go to login page"):
            browser.element('[href="/login"]').click()
        with allure.step("Fill email"):
            browser.element('[id="Email"]').type(f'{login}')
        with allure.step("Fill Password"):
            browser.element('[id="Password"]').type(f'{password}')
            browser.element('[class="button-1 login-button"]').click()

    @allure.step("Add product to cart")
    def add_product_to_cart(self):
        with allure.step("Choose product"):
            browser.element('[href="/25-virtual-gift-card"]').click()
        with allure.step("Fill form for Virtual Gift Card"):
            browser.element('[id="giftcard_2_RecipientName"]').type(f'Papa')
            browser.element('[id="giftcard_2_RecipientEmail"]').type(f'papa@gmail.com')
            browser.element('[id="giftcard_2_SenderName"]').type(f'Mama')
            browser.element('[id="giftcard_2_SenderEmail"]').type(f'mama@gmail.com')
            browser.element('[id="add-to-cart-button-2"]').click()
            browser.element('[href="/cart"]').click()

    @allure.step("Add product to cart")
    def add_product_to_cart_cloud(self):
        with allure.step("Choose product"):
            browser.element('[href="/25-virtual-gift-card"]').click()
        with allure.step("Fill form for Virtual Gift Card"):
            browser.element('[id="giftcard_2_RecipientName"]').type(f'Papa')
            browser.element('[id="giftcard_2_RecipientEmail"]').type(f'papa@gmail.com')
            browser.element('[id="giftcard_2_SenderName"]').type(f'Mama')
            browser.element('[id="giftcard_2_SenderEmail"]').type(f'mama@gmail.com')
            browser.element('[id="add-to-cart-button-2"]').click()
            browser.element('[href="/cart"]').click()