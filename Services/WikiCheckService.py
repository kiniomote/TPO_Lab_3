from selenium import webdriver

driver = webdriver.Chrome('D:\Program Files\Chrome\chromedriver')
driver.get('https://www.google.com/')
element = driver.find_element_by_name('q')
element.send_keys('unit testing')
element.submit()
x_path = "//a[@href='https://en.wikipedia.org/wiki/Unit_testing']"
driver.find_element_by_xpath(x_path).click()
search = driver.find_element_by_xpath("//input[@id='searchInput']")
search.send_keys('NUnit')
search.submit()
URL = 'https://en.wikipedia.org/wiki/NUnit'
print(driver.current_url == URL)
print(driver.find_element_by_xpath("//*[@title='NUnit – Russian']").text == 'Русский')
