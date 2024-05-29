import allure
import pytest
import pytest_check as check
from locators.locators_main_page import MainPage


def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)


    elements = [
        (page.btn_headers_home, 'HOME', '/'),
        (page.btn_headers_new_arrivals, 'NEW ARRIVALS', '/new-arrivals'),
        (page.btn_headers_apparel, 'APPAREL', '/apparel'),
        (page.btn_headers_designer_collection, 'DESIGNER COLLECTION', '/designer-collection'),
        (page.btn_headers_outerwear, 'OUTERWEAR', '/outerwear'),
        (page.btn_headers_accessories, 'ACCESSORIES', '/accessories'),
        (page.btn_headers_gift_card, 'GIFT CARD', '/gift-card'),
        (page.btn_headers_shop_all, 'SHOP ALL', '/shop-all')
                ]

    for elements_btn, elements_text, elements_link in elements:
        with allure.step(f'Проверка кнопки {elements_text}'):
            check.is_true(elements_btn.is_visible())
            check.is_true(elements_btn.is_clickable())
            check.equal(elements_btn.get_text(), elements_text)
            check.equal(page.input_main_wrapper.get_attribute('href'), elements_link)

def teat_footer(web_browser):
    """Этот тест проверяет футер главной страницы"""

    page = MainPage(web_browser)

    elements = [
        (page.btn_footers_contact, 'Contact', '/contact'),
        (page.btn_footers_account, 'Account', '/account'),
        (page.btn_footers_track_my_order, 'Track My Order', '/track-my-order'),
        (page.btn_footers_privacy_policy, 'Privacy Policy', '/privacy-policy'),
        (page.btn_footers_size_chart, 'Size Chart', '/size-chart')
               ]

    for elements_btn, elements_text, elements_link in elements:
        with allure.step(f'Проверка кнопки {elements_text}'):
            check.is_true(elements_btn.is_visible())
            check.is_true(elements_btn.is_clickable())
            check.equal(elements_btn.get_text(), elements_text)
            check.equal(page.input_main_wrapper.get_attribute('href'), elements_link)

