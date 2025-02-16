import allure
from allure_commons.types import Severity
from page.api.page_steps import Page_steps
from page.api.page_asserts import Page_asserts

page_steps=Page_steps()
page_asserts=Page_asserts()

@allure.tag('API local')
@allure.feature('Successful authorization')
@allure.story('Successful authorization')
@allure.title('Authorization')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AndreevDK")
@allure.link('https://demowebshop.tricentis.com/', name='Demo web SHOP')
def test_authorization():
        page_steps.authorization()
        page_asserts.authorization()
