from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Drivers\\Chrome 89.0.4389.23\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://122.170.14.195:8080/uth/gadgetsgallery/catalog/index.php")

print("--------------- Login to User Account ----------------")

driver.find_element_by_link_text("log yourself in").click()
driver.find_element_by_name("email_address").send_keys("python@abccompany.in")
driver.find_element_by_name("password").send_keys("abc")
#Here, Email_address and Password are incorrect for Security Purpose.
driver.find_element_by_id("tdb1").click()

print("--------------- Select Products and Add into the Cart ----------------")

driver.find_element_by_link_text("Headphones").click()
driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[2]/a").click()
driver.find_element_by_xpath("//button[text()='Add to Cart']").click()

manufacturer = Select(driver.find_element_by_name("manufacturers_id"))
manufacturer.select_by_visible_text("Canon")
driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div/div[1]/div[2]/table/tbody/tr[3]/td[2]/a").click()
driver.find_element_by_xpath("//button[text()='Add to Cart']").click()

print("--------------- Checkout and Payment Procedure ----------------")

driver.find_element_by_id("tdb3").click()
driver.find_element_by_xpath("//button[text()='Continue']").click()
driver.find_element_by_xpath("//input[@name='payment' and @value='cod']").click()
#//*[text()='Cash on Delivery']//parent::td//following-sibling::td/input <---(Another type of XPath)

driver.find_element_by_name("comments").send_keys("Request to send my order with gift wrap.")
driver.find_element_by_xpath("//button[text()='Continue']").click()

print("-------------------- Shopping Cart Procedure -----------------------")

productPrices = driver.find_elements_by_xpath("//div[@class='contentContainer']/div/table/tbody/tr/td[2]/table/tbody/tr/td[3]")

totalAmount = 0

for prod in range(0, len(productPrices)):
    priceText = str(productPrices[prod].text)
    Remove_Rs_PriceText = priceText.replace("Rs.", "")
    final_val = float(Remove_Rs_PriceText.replace(",", ""))
    totalAmount = totalAmount + final_val

print("Amount before flat rate is -->", totalAmount)

flatRate = str(driver.find_element_by_xpath("//*[text()='Flat Rate (Best Way):']//following-sibling::td").text)
final_flatRate = float(flatRate.replace("Rs.", ""))

expected_Total_amount = totalAmount + final_flatRate
#print(expected_Total_amount)
finalExpectedTotal = '%.2f'%expected_Total_amount    #To get 2 digit after the point(.)


actualPrice = str(driver.find_element_by_xpath("//*[@id='content']/div[2]/form/div/div[2]/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/strong").text)

remove_Rs_actualPrice = actualPrice.replace("Rs.", "")
final_actualPrice = remove_Rs_actualPrice.replace(",", "")

actualTotal = float(final_actualPrice)
finalActualTotal = '%.2f'%actualTotal              #To get 2 digit after the point(.)

print("Actual Amount is:-->", finalActualTotal)
print("Expected Amount is:-->", finalExpectedTotal)


if actualTotal == expected_Total_amount:
    print("Pass")
else:
    print("Fail")

driver.find_element_by_xpath("//button[text()='Confirm Order']").click()
driver.find_element_by_xpath("//button[text()='Continue']").click()

driver.find_element_by_link_text("My Account").click()
driver.find_element_by_link_text("View the orders I have made.").click()

allView = driver.find_elements_by_xpath("//*[text()='View']")

for viewB in range(0, len(allView)):
    allView[0].click()
    break

actualPrice1 = str(driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div[2]/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/strong").text)
remove_Rs_actualPrice1 = actualPrice1.replace("Rs.", "")
myAccount_actualPrice = remove_Rs_actualPrice1.replace(",", "")
myAccount_billingTotal = float(myAccount_actualPrice)
print("Billing Total of My Account:-->", myAccount_billingTotal)

driver.find_element_by_link_text("Log Off").click()
driver.find_element_by_id("tdb1").click()
'''
Now, Going to Admin Panel (For Checking Total Price into the Admin panel should be same and
Comparing with the Total price of the User side.)
'''
driver.get("http://122.170.14.195:8080/uth/gadgetsgallery/catalog/admin/login.php")

driver.find_element_by_name("username").send_keys("Python User")
driver.find_element_by_name("password").send_keys("abc")
#Here, Email_address and Password are incorrect for Security Purpose.
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(1)

driver.find_element_by_link_text("Orders").click()

wait = WebDriverWait(driver, 5)    #Explicit WebDriverWait
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='ui-accordion-adminAppMenu-panel-6']/ul/li/a")))

driver.find_element_by_xpath("//*[@id='ui-accordion-adminAppMenu-panel-6']/ul/li/a").click()

adminOrderText = driver.find_element_by_xpath("//*[@id='defaultSelected']/td[2]").text
print("Admin Order Test is:-->", adminOrderText)








