from selenium import webdriver

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'

driver_path = '/usr/bin/'
driver = webdriver.Firefox(driver_path)

driver.get(url)
input('Press ENTER to close the automated browser')
driver.quit()
