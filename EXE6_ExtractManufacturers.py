from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Drivers\\Chrome 89.0.4389.23\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://122.170.14.195:8080/uth/gadgetsgallery/catalog/index.php")

menuDD = driver.find_element_by_name("manufacturers_id")
menuValues = menuDD.find_elements_by_tag_name("option")

for menu in range(1, len(menuValues)):
    menuValues[menu].click()
    menuText = driver.find_element_by_xpath("//div[@id='content']/div[2]/h1").text
    print(menuText+"-->"+driver.title+"-->"+driver.current_url)
    time.sleep(1)
    driver.back()
    menuDD = driver.find_element_by_name("manufacturers_id")
    menuValues = menuDD.find_elements_by_tag_name("option")