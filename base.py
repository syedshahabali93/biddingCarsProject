import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import undetected_chromedriver as uc
import json
import os.path


def launch_browser():
    print("Launching Browser")
    global driver, wait1, wait2, wait3
    # options =webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--log-level=1")
    # options.add_argument("--start-maximized")
    # options.add_argument("--window-size=1980x1080")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-setuid-sandbox")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--single-process")
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option("useAutomationExtension", False)
    # options.add_argument("--no-sandbox")
    # chromedriver_path = "C:\work\elearnio-new\chromedriver.exe"

    # d = DesiredCapabilities.CHROME
    # d['goog:loggingPrefs'] = {'browser': 'ALL'}
    # d['goog:loggingPrefs'] = {'performance': 'ALL'}
    #
    # driver = webdriver.Chrome(executable_path = chromedriver_path, options = options, desired_capabilities = d, service_log_path="chrome2.log",  service_args=["--verbose", "--log-path=chrome1.log"])
    driver = uc.Chrome();
    wait1 = WebDriverWait(driver, 10)
    driver.maximize_window()

def load_url(base_url):
    print("Loading url")
    driver.get(base_url)

def wait_and_enter_text(ele, text):
    print("Entering Email or password")
    print(text)
    wait1.until(EC.visibility_of_element_located((ele))).send_keys(text)

def wait_and_click(element_name, ele):
    print("Clicking on: " + element_name)
    wait1.until(EC.visibility_of_element_located((ele))).click()

def wait_and_find_element(ele):
    return wait1.until(EC.visibility_of_element_located((ele)))

def wait_for_element_invisible(ele):
    wait1.until(EC.invisibility_of_element_located((ele)))

def drag_and_drop(element, x, y):
    ActionChains(driver).drag_and_drop_by_offset(element, x, y).perform()

def is_element_present(ele):
    count = len(driver.find_elements(*ele))
    if(count==0):
        return False
    else:
        return True

def pressEnterOnElement(ele):
    wait1.until(EC.visibility_of_element_located((ele))).send_keys(Keys.ENTER)


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

