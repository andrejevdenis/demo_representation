import allure

from allure_commons.types import Severity
from page.mobile_app.page_steps import Page_steps
from page.mobile_app.page_asserts import Page_asserts

page_steps=Page_steps()
page_asserts=Page_asserts()

@allure.tag('E2E Mobile local_real')
@allure.feature('Authorization')
@allure.story('Successful user authorization')
@allure.title('User authorization test')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AndreevDK")
@allure.link('https://www.dns-shop.ru/', name='DNS SHOP digital and household devices store')
def test_users_authorization():
        page_steps.authorization()
        page_asserts.authorization()
