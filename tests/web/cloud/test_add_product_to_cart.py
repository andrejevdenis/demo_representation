import allure
from allure_commons.types import Severity
from tests.web.page.page_steps import Page_steps
from tests.web.page.page_asserts import Page_asserts

page_steps=Page_steps()
page_asserts=Page_asserts()

@allure.tag('E2E Web cloud')
@allure.feature('Successful adding product to cart')
@allure.story('Successful adding product to cart')
@allure.title('Add product to cart')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AndreevDK")
@allure.link('https://demowebshop.tricentis.com/', name='Demo web SHOP')
def test_add_product_to_cart_cloud():
        page_steps.add_product_to_cart_cloud()
        page_asserts.add_product_to_cart_cloud()