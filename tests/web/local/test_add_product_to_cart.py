import allure
from allure_commons.types import Severity
from page.web.page_steps import Page_steps
from page.web.page_asserts import Page_asserts

page_steps=Page_steps()
page_asserts=Page_asserts()

@allure.tag('E2E Web local')
@allure.feature('Successful adding product to cart')
@allure.story('Successful adding product to cart')
@allure.title('Add product to cart')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AndreevDK")
@allure.link('https://demowebshop.tricentis.com/', name='Demo web SHOP')
def test_add_product_to_cart():
        page_steps.add_product_to_cart()
        page_asserts.add_product_to_cart()