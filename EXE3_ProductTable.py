from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Drivers\\Chrome 89.0.4389.23\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://122.170.14.195:8080/uth/gadgetsgallery/catalog/index.php")

prodTable = driver.find_elements_by_xpath("//table/tbody/tr/td/a[2]")
#Common XPath to fetch all products from Product Table.

for prod in range(0, len(prodTable)):
    print(prodTable[prod].text)
    prodTable[prod].click()
    time.sleep(1)
    driver.back()
    time.sleep(1)
    prodTable = driver.find_elements_by_xpath("//table/tbody/tr/td/a[2]")























