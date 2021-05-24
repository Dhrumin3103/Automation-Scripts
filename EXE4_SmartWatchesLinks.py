from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Drivers\\Chrome 89.0.4389.23\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://122.170.14.195:8080/uth/gadgetsgallery/catalog/index.php")

driver.find_element_by_link_text("Smartwatches").click()

allProducts = driver.find_elements_by_xpath("//*[@class='contentText']/div[1]/div[2]/table/tbody/tr/td[2]")
#Common XPath to fetch all Smartwatches.

for prod in range(0, len(allProducts)):
    print(allProducts[prod].text)
































