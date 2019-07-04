

import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

	def go_to_login_page(self):
		login_link = self.browser.find_element(By.CSS_SELECTOR, "#registration_link")
		login_link.click()
		print('-------------------go_to_login_page(self)')
		time.sleep(1)


#	def should_be_login_link(self):
#		self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

	def should_be_login_link(self):
		assert self.is_element_present (By.CSS_SELECTOR, "#registration_link"), "Login link is not presented"












