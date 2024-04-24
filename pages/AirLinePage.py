import pages.PageElements as pe
import utilities.CustomLogger as cl
from base.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class AirLinePage(BasePage):

    def __init__(self, driver, context):
        super().__init__(driver, context)
        self.driver = driver
        self.context = context
        self.departure_place = "인천"
        self.arrival_place = "오사카"

    def click_roundtrip_tap(self):
        BasePage.click_element(self, AppiumBy.XPATH, pe.naver_airline_roundtrip_tap)

    def click_departure_menu(self):
        BasePage.click_element(self, AppiumBy.XPATH, pe.naver_airline_departure_menu)

    def input_departure_place(self):
        BasePage.send_key_element(self, AppiumBy.XPATH, pe.naver_airline_departure_search_field, self.departure_place)

    def click_departure_place(self):
        BasePage.click_element(self, AppiumBy.XPATH, pe.naver_ariline_departure_place)

    def click_arrival_menu(self):
        BasePage.click_element(self, AppiumBy.XPATH, pe.naver_ariline_arrival_menu)

    def input_arrival_place(self):
        BasePage.send_key_element(self, AppiumBy.XPATH, pe.naver_airline_arrival_search_field, self.arrival_place)

    def click_arrival_place(self):
        BasePage.click_element(self, AppiumBy.XPATH, pe.naver_airline_arrival_place)

    def check_airline_setup(self):
        BasePage.is_displayed(self, AppiumBy.XPATH, pe.naver_airline_setup)
