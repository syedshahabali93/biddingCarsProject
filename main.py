from base import *
from constants import *
from googleSheets import GoogleSheet
from locators import *


def findCarsByVin():
    p1 = GoogleSheet()
    vinnumbers = p1.fetchSheetData()

    launch_browser()
    load_url(base_url)

    for vin in vinnumbers:
        wait_and_find_element(searchVehicleField)
        wait_and_enter_text(searchVehicleField, vin)
        pressEnterOnElement(searchVehicleField)
        break
    # wait_and_find_element(login_password_input)
    # wait_and_enter_text(login_password_input, password)
    # wait_and_find_element(login_button)
    # wait_and_click("login_button", login_button)
    # wait_and_find_element(my_trainings_show_all_button)
    # capture_screenshot("browser-home-page.PNG")


findCarsByVin()
