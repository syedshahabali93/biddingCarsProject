import undetected_chromedriver as uc
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

def launch_browser():
    print("Launching Browser")
    global driver, wait1
    driver = uc.Chrome(use_subprocess=True)
    wait1 = WebDriverWait(driver, 10)
    driver.maximize_window()

def load_url(base_url):
    print("Loading url")
    driver.get(base_url)

def wait_and_enter_text(ele, text):
    wait1.until(EC.visibility_of_element_located(ele)).send_keys(text)

def wait_and_click(element_name, ele):
    print("Clicking on: " + element_name)
    wait1.until(EC.visibility_of_element_located(ele)).click()

def wait_and_find_element(ele):
    return wait1.until(EC.visibility_of_element_located(ele))

def wait_and_find_element_by_id(id):
    return wait1.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='"+id+"']")))

def wait_for_element_invisible(ele):
    wait1.until(EC.invisibility_of_element_located(ele))

def drag_and_drop(element, x, y):
    ActionChains(driver).drag_and_drop_by_offset(element, x, y).perform()

def is_element_present(ele):
    count = len(driver.find_elements(*ele))
    if(count==0):
        return False
    else:
        return True

def capture_screenshot(filename):
    driver.get_screenshot_as_file(filename)

def close_browser():
    if(browser_already_open()):
        driver.quit()

def browser_already_open():
    try:
        global driver
        if(len(driver.window_handles) == 1):
            return True
        else:
            return False
    except Exception as e:
        return False

def getWindowsList():
    return driver.window_handles

def switchToWindow(win):
    return driver.switch_to.window(win)

def getElementText(ele):
    return wait1.until(EC.visibility_of_element_located(ele)).text

def getElementTextUpdate(ele):
    return driver.find_element_by_xpath(ele).text

def getElementAttribute(ele, attr):
    return wait1.until(EC.visibility_of_element_located(ele)).get_attribute(attr)

def waitForElementAndPressEnter(ele):
    wait1.until(EC.visibility_of_element_located(ele)).send_keys(Keys.ENTER)

def closeCurrentWindow():
    driver.close()

def getPageURL():
    return driver.current_url

def getElementsList(ele):
    return driver.find_elements(By.XPATH, ele)
