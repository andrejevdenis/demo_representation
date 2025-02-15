import logging
from dotenv import load_dotenv
import os
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser
import allure
from bs4 import BeautifulSoup
from jsonschema import validate


load_dotenv()
login=os.getenv('LOGIN_USER_DEMO_SHOP')
password=os.getenv('PASSWORD_USER_DEMO_SHOP')
WEB_URL = os.getenv('LOCAL_URL_WEB')

class Page_steps:
    @allure.step("Authorization")
    def authorization(self):
        with step("Authorization with API"):
            api_url = "https://demowebshop.tricentis.com/login"
            payload1 = f'Email={login}&Password={password}&RememberMe=false'
            headers1 = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'ARRAffinity=69007df75624f8922b4afe298eba2ebc421f44c0e52dfaff025620f7ee7984f2; ARRAffinitySameSite=69007df75624f8922b4afe298eba2ebc421f44c0e52dfaff025620f7ee7984f2; __utmc=78382081; __utmz=78382081.1737173346.1.1.utmcsr=school.qa.guru|utmccn=(referral)|utmcmd=referral|utmcct=/; __RequestVerificationToken=Lp_0NJ40tPTcZU2xBocNJ6xCiA2ltcsNfnPizq0eE_fGHXvYowSgbIrflcUDFF7WL1EkL2x4cfl8GaV0r1JV2VhBxGTyxxTIUUFEavxCVhk1; ASP.NET_SessionId=rfe0osvzjvi3053fi2gaxd1o; NopCommerce.RecentlyViewedProducts=RecentlyViewedProductIds=2; __utma=78382081.1332902260.1737173346.1737250982.1737255051.5; __utmt=1; Nop.customer=0446ee6b-ea81-4727-8ab6-52707b96b33f; __utmb=78382081.33.10.1737255051',
                'Origin': 'https://demowebshop.tricentis.com',
                'Referer': 'https://demowebshop.tricentis.com/login',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
            }

            result = requests.request("POST", api_url, headers=headers1, data=payload1, allow_redirects=False)
            logging.info('Authorization')
            logging.info(result.request.url)
            logging.info(result.status_code)
        with step("Response validation"):
            assert result.status_code == 302
        with step("Setup for UI assertations"):
            cookie = result.cookies.get("NOPCOMMERCE.AUTH")
            browser.open(WEB_URL)
            browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})


    @allure.step("Adding product to cart")
    def cart_add(self):
        with step("Add_product_to_cart"):
            api_url = "https://demowebshop.tricentis.com/addproducttocart/details/2/1"
            payload = "giftcard_2.RecipientName=Mama&giftcard_2.RecipientEmail=mama@gmail.com&giftcard_2.SenderName=Papa&giftcard_2.SenderEmail=papa@gmail.com&giftcard_2.Message=&addtocart_2.EnteredQuantity=1"
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'ARRAffinity=69007df75624f8922b4afe298eba2ebc421f44c0e52dfaff025620f7ee7984f2; ARRAffinitySameSite=69007df75624f8922b4afe298eba2ebc421f44c0e52dfaff025620f7ee7984f2; __utmc=78382081; __utmz=78382081.1737173346.1.1.utmcsr=school.qa.guru|utmccn=(referral)|utmcmd=referral|utmcct=/; __RequestVerificationToken=Lp_0NJ40tPTcZU2xBocNJ6xCiA2ltcsNfnPizq0eE_fGHXvYowSgbIrflcUDFF7WL1EkL2x4cfl8GaV0r1JV2VhBxGTyxxTIUUFEavxCVhk1; ASP.NET_SessionId=rfe0osvzjvi3053fi2gaxd1o; NopCommerce.RecentlyViewedProducts=RecentlyViewedProductIds=2; NOPCOMMERCE.AUTH=773198AC35C81A746A95512535263CD66271082BEF45B1C4D3478CF419420B97F67AF4E256452FAD64F227070D6BB1128C706B51B78222353319750AFD48D3866E805D5FF10C75FAE7ABDBF4FAC7B45F91C5D64B31B47992B45806A04E27174B1EE63B64B5A523DCA1370E70B24838A2D2C6D095ED08DC2547130488938EBF3BD50D77ED1B3592B33797FE0FE4112EAD3AA64866F28B50BA10E850BE671D7C55; Nop.customer=7c02f59d-216f-490b-b181-752c6b96c555; __utma=78382081.1332902260.1737173346.1737250982.1737255051.5; __utmt=1; __utmb=78382081.9.10.1737255051',
                'Origin': 'https://demowebshop.tricentis.com',
                'Referer': 'https://demowebshop.tricentis.com/25-virtual-gift-card',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
            }

        result = requests.request("POST", api_url, headers=headers, data=payload)
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info('API Add product to cart')
        logging.info(result.request.url)
        logging.info(result.status_code)
        with step("Response validation"):
            assert result.status_code == 200


    @allure.step("Clearing the cart")
    def cart_clear(self):

        with step("Setup for cart clearing"):
            url2 = "https://demowebshop.tricentis.com/cart"

            headers2 = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Cookie': 'ARRAffinity=69007df75624f8922b4afe298eba2ebc421f44c0e52dfaff025620f7ee7984f2; ARRAffinitySameSite=69007df75624f8922b4afe298eba2ebc421f44c0e52dfaff025620f7ee7984f2; __utmc=78382081; __utmz=78382081.1737173346.1.1.utmcsr=school.qa.guru|utmccn=(referral)|utmcmd=referral|utmcct=/; __RequestVerificationToken=Lp_0NJ40tPTcZU2xBocNJ6xCiA2ltcsNfnPizq0eE_fGHXvYowSgbIrflcUDFF7WL1EkL2x4cfl8GaV0r1JV2VhBxGTyxxTIUUFEavxCVhk1; ASP.NET_SessionId=rfe0osvzjvi3053fi2gaxd1o; NopCommerce.RecentlyViewedProducts=RecentlyViewedProductIds=2; __utma=78382081.1332902260.1737173346.1737250982.1737255051.5; NOPCOMMERCE.AUTH=A6FA29E7115C59A9A7C414563AB049CB26FC61423B140AA90E95BBCFD55284CCE4ACFCC3E9BD051CB5974F162D0D2508B2FCE5A3A87229FB37748C85A70FA39AD29F81F16E837EBDC593BA1916FD1D626629330074A18BA7EF46A27E0FCFBBB6E4DF95F528694E8CA9E83E4AC1550842E1C92E35224F54499E1ABAFEDC4C0B587BB89527C33080E0DBF7F323A69FB1BB40B9B1670AFB7163F060E5E9CF45A5B0; Nop.customer=7c02f59d-216f-490b-b181-752c6b96c555; __utmt=1; __utmb=78382081.50.10.1737255051',
                'Referer': 'https://demowebshop.tricentis.com/25-virtual-gift-card',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
            }

            result2 = requests.request("GET", url2, headers=headers2)
            logging.info('API Setup for cart clearing')
            logging.info(result2.request.url)
            logging.info(result2.status_code)
        with step("Response validation"):
            assert result2.status_code == 200
            html_content = result2.text
            soup = BeautifulSoup(html_content, "html.parser")
            element = soup.find("input", type="checkbox")
            attribute_value = element.get("value")
            if element:
                print(f'Cart_ID:{attribute_value}')
            else:
                print("Element not found.")


        with step("Cart clear"):
            payload2 = {'removefromcart': attribute_value,
                        'updatecart': 'Update shopping cart',
                        'discountcouponcode': '',
                        'giftcardcouponcode': ''}

            result3 = requests.request("POST", url2, headers=headers2, data=payload2)
            logging.info("API API Cart clear")
            logging.info(result3.request.url)
            logging.info(result3.status_code)
            with step("Response validation"):
                assert result2.status_code == 200