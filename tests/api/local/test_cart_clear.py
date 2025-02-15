import allure
from allure_commons.types import Severity
from tests.api.page.page_steps import Page_steps
from tests.api.page.page_asserts import Page_asserts

page_steps=Page_steps()
page_asserts=Page_asserts()

@allure.tag('API local')
@allure.feature('Successful clearing the cart')
@allure.story('Successful clearing the cart')
@allure.title('Authorization')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AndreevDK")
@allure.link('https://demowebshop.tricentis.com/', name='Demo web SHOP')
def test_cart_clear():
        page_steps.cart_add()
        page_steps.cart_clear()
        page_steps.authorization()
        page_asserts.cart_clear()
