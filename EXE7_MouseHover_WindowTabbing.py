from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Drivers\\Chrome 89.0.4389.23\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.unicodetechnologies.in/")

mainMenu = driver.find_element_by_xpath("//a[text()='Courses']")
subMenu = driver.find_element_by_xpath("//*[@id='menu-item-139']/ul/li[4]/a")

action = ActionChains(driver) #driver get his whole control to 'ActionChains Class' & driver pointion to webpage.
action.move_to_element(mainMenu).perform()
action.move_to_element(subMenu).click().perform()
time.sleep(2)

unicodeLink = driver.find_element_by_link_text("Unicode Technologies")
#When one Element is not clickble throgh Selenium than We can use JavaScript method on this page as a 2nd way.

driver.execute_script("arguments[0].click();", unicodeLink)
#arguments[0].click(); is a JavaScript method & it is comman code to use click bu javaScript.
#Here, You must have to defind WebElement as a 2nd perameter where you want to click.

print("----------------Window Tabbing-----------")
windowId = driver.window_handles    #window_handles methos is returns List.

window1 = windowId[0]
window2 = windowId[1]

driver.switch_to.window(window2)  #Now driver is pointing to page2(2nd new tab)
driver.find_element_by_link_text("F.A.Q").click()



