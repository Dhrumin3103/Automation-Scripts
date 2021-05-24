from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Drivers\\Chrome 89.0.4389.23\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://122.170.14.195:8080/uth/gadgetsgallery/catalog/index.php")

print("---- Printing particular parts of the webpage ----")
catBox = driver.find_element_by_xpath("//*[@id='left_sidebar']/div[1]/div[2]")
#This is XPath of whole div tag which is covered whole categories's links and CatBox is pointing to div tag.

cat_links = catBox.find_elements_by_tag_name("a")
print(len(cat_links))

for link in range(len(cat_links)):
    print(cat_links[link].text)
    cat_links[link].click()
    print(driver.title)
    driver.back()
    catBox = driver.find_element_by_xpath("//*[@id='left_sidebar']/div[1]/div[2]")
    cat_links = catBox.find_elements_by_tag_name("a")