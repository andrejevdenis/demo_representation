import allure
from allure_commons.types import Severity
from tests.mobile_app.page.page_steps import Page_steps
from tests.mobile_app.page.page_asserts import Page_asserts
import time

page_steps=Page_steps()
page_asserts=Page_asserts()

@allure.tag('E2E Mobile cloud')
@allure.feature('Search and add product to cart')
@allure.story('Successful cart fill by searching item')
@allure.title('Search assert and cart fill test')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AndreevDK")
@allure.link('https://www.dns-shop.ru/', name='DNS SHOP digital and household devices store')
def test_search_and_add_to_cart():
        time.sleep(3)
        page_steps.search_and_add_to_cart()
        page_asserts.search_and_add_to_cart()
