
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_Add_to_cart_SHOULD_EXIST(browser):
	browser.get(link)
	time.sleep(1)
	basketbtn = browser.find_element_by_css_selector(".btn-add-to-basket")
	assert(basketbtn), "ERROR:  button 'Add to cart' IS NOT EXIST !!!"
	print("SUCSESS:  button 'Add to cart' EXIST !!!")





