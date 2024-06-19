import allure
import pytest
import pytest_check as check
from locators.locators_main_page import MainPage


def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)


    elements = [
        (page.btn_headers_home, 'HOME', 'https://www.barksfifth.com/'),
        (page.btn_headers_new_arrivals, 'NEW ARRIVALS', 'https://www.barksfifth.com/new-arrivals'),
        (page.btn_headers_apparel, 'APPAREL', 'https://www.barksfifth.com/apparel'),
        (page.btn_headers_designer_collection, 'DESIGNER COLLECTION', 'https://www.barksfifth.com/designer-collection'),
        (page.btn_headers_outerwear, 'OUTERWEAR', 'https://www.barksfifth.com/outerwear'),
        (page.btn_headers_accessories, 'ACCESSORIES', 'https://www.barksfifth.com/accessories'),
        (page.btn_headers_gift_card, 'GIFT CARD', 'https://squareup.com/gift/MLVAZ5R6NM95E/order'),
        (page.btn_headers_shop_all, 'SHOP ALL', 'https://www.barksfifth.com/s/shop')
                    ]

    for elements_btn, elements_text, elements_link in elements:
        with allure.step(f'Проверка кнопки {elements_text}'):
            check.is_true(elements_btn.is_visible())
            check.is_true(elements_btn.is_clickable())
            check.equal(elements_btn.get_text(), elements_text)
            check.equal(elements_btn.get_attribute('href'), elements_link)

def teat_footer(web_browser):
    """Этот тест проверяет футер главной страницы"""

    page = MainPage(web_browser)

    elements = [
        (page.btn_footers_contact, 'Contact', 'https://www.barksfifth.com/contact'),
        (page.btn_footers_account, 'Account', 'https://www.barksfifth.com/account'),
        (page.btn_footers_track_my_order, 'Track My Order', 'https://www.barksfifth.com/track-my-order'),
        (page.btn_footers_privacy_policy, 'Privacy Policy', 'https://www.barksfifth.com/privacy-policy'),
        (page.btn_footers_size_chart, 'Size Chart', 'https://www.barksfifth.com/size-chart')
               ]

    for elements_btn, elements_text, elements_link in elements:
        with allure.step(f'Проверка кнопки {elements_text}'):
            check.is_true(elements_btn.is_visible())
            check.is_true(elements_btn.is_clickable())
            check.equal(elements_btn.get_text(), elements_text)
            check.equal(page.input_main_wrapper.get_attribute('href'), elements_link)

