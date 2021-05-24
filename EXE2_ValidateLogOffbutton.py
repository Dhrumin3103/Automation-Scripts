from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

checkLogoff = False

driver = webdriver.Chrome(executable_path="C:\\Drivers\\Chrome 89.0.4389.23\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)   #it will give timeout Error this is globle time for waiting for every elements.
driver.get("http://122.170.14.195:8080/uth/gadgetsgallery/catalog/index.php")

driver.find_element_by_link_text("log yourself in").click()

driver.find_element_by_name("email_address").send_keys("python@abccompany.in")
driver.find_element_by_name("password").send_keys("abc")

#Here, Email_address and Password are incorrect for Security Purpose.

driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(2)

try:
    checkLogoff = driver.find_element_by_link_text("Log Off").is_displayed()
    checkLogoff = True

except Exception as e:
    checkLogoff = False

if checkLogoff:
    print("User has been Logged In")
    driver.find_element_by_link_text("Log Off").click()
    driver.find_element_by_id("tdb1").click()
else:
    print("Invalid Credentials")
