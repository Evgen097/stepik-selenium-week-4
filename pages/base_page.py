
import time
from selenium.common.exceptions import (NoSuchElementException)

class BasePage(object):
	def __init__(self, browser, url, timeout=2):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)
		
	def open(self):
		self.get()
		print('-----------------def open(self)')
		time.sleep(1)

	def get(self):
		self.browser.get(self.url)
		print('-----------------def get(self)')
		time.sleep(1)

	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True
		










