
import time

class BasePage(object):
	def __init__(self, browser, url):
		self.browser = browser
		self.url = url
		
	def open(self):
		self.get()
		print('-----------------def open(self)')
		time.sleep(3)

	def get(self):
		self.browser.get(self.url)
		print('-----------------def get(self)')
		time.sleep(3)












