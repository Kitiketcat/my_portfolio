import os

from page.base_page import WebPage
from page.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        self.web_driver = web_driver
        self.input_main_wrapper = web_driver.find_element_by_xpath("your_xpath_locator_for_input_main_wrapper")
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.barksfifth.com/'

        super().__init__(web_driver, url)

    btn_headers_home = WebElement(xpath='(//*[@subnavcolor="--color-white"]//*[@allow-nav=""])[1]')
    btn_headers_new_arrivals = WebElement(xpath='(//*[@subnavcolor="--color-white"]//*[@allow-nav=""])[2]')
    btn_headers_apparel = WebElement(xpath='(//*[@subnavcolor="--color-white"]//*[@allow-nav=""])[3]')
    btn_headers_designer_collection = WebElement(xpath='(//*[@subnavcolor="--color-white"]//*[@allow-nav=""])[4]')
    btn_headers_outerwear = WebElement(xpath='(//*[@subnavcolor="--color-white"]//*[@allow-nav=""])[5]')
    btn_headers_accessories = WebElement(xpath='(//*[@subnavcolor="--color-white"]//*[@allow-nav=""])[6]')
    btn_headers_gift_card = WebElement(xpath='(//*[@subnavcolor="--color-white"]//*[@allow-nav=""])[7]')
    btn_headers_shop_all = WebElement(xpath='(//*[@subnavcolor="--color-white"]//*[@allow-nav=""])[8]')

    btn_footers_contact = WebElement(xpath='(//*[@isdark="true"]//*[@allow-nav=""])[1]')
    btn_footers_account = WebElement(xpath='(//*[@isdark="true"]//*[@allow-nav=""])[2]')
    btn_footers_track_my_order = WebElement(xpath='(//*[@isdark="true"]//*[@allow-nav=""])[3]')
    btn_footers_privacy_policy = WebElement(xpath='(//*[@isdark="true"]//*[@allow-nav=""])[4]')
    btn_footers_size_chart = WebElement(xpath='(//*[@isdark="true"]//*[@allow-nav=""])[5]')

