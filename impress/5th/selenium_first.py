#import chromedriver
from selenium import webdriver

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'

driver_path = '/usr/bin/google-chrome'
driver = webdriver.Chrome()

driver.get(url)
for quote in driver.find_elements_by_class_name('quote'):
    print(quote.text)

input("Press ENTER to close the automated browser")
driver.quit()
