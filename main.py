import os
from base import *
from googleSheets import *
from locators import *
from constants import *


def findCarsByVin():
    sheetObj = GoogleSheet()
    sheetLength = os.getenv('SHEET_LENGTH')
    sheetStart = os.getenv('SHEET_START')
    launch_browser()
    load_url(base_url)
    time.sleep(2)
    wait_and_find_element(login)
    wait_and_click('Clicking on Login Button', login)
    time.sleep(2)
    wait_and_find_element(email_field)
    wait_and_enter_text(email_field, email)
    wait_and_find_element(password_field)
    wait_and_enter_text(password_field, password)
    wait_and_find_element(sign_in)
    time.sleep(1)
    wait_and_click('Clicking on Sign-In Button', sign_in)
    time.sleep(2)

    for index in range(int(sheetLength)):
        row_number = int(sheetStart)+index
        vinNumberObject = sheetObj.fetchSheetData(row_number)
        print(vinNumberObject)
        if(vinNumberObject['vin'] == 'vin_not_exists'):
            continue
        vin = vinNumberObject['vin']
        ranges = vinNumberObject['range']
        try:
            print("Vin: " + str(vin))
            load_url(base_url)
            time.sleep(2)
            wait_and_find_element(search_field)
            wait_and_enter_text(search_field, vin)
            time.sleep(5)
            waitForElementAndPressEnter(search_field)
            try:
                car_search_link = (By.XPATH, "//a[contains(@href,'" + vin + "') and @class='damage-info']")
                time.sleep(5)
                wait_and_find_element(car_search_link)
                wait_and_click("Clicking on Car Link", car_search_link)
                total_windows = getWindowsList()
                switchToWindow(total_windows[1])
                time.sleep(7)
                try:
                    wait_and_find_element(lot_price)
                    lot_pr = getElementText(lot_price)
                except Exception as e:
                    lot_pr = ""
                    pass
                try:
                    wait_and_find_element(auction_fee)
                    auction_price = getElementText(auction_fee)
                except Exception as e:
                    auction_price = ""
                    pass
                print("in try")
                print(lot_pr)
                print(auction_price)
                print("\n")
                temp = [lot_pr, auction_price]
                sheetObj.uploadToSheet(temp, ranges, row_number)
                closeCurrentWindow()
                switchToWindow(total_windows[0])
                time.sleep(1)
            except Exception as e:
                wait_and_find_element(lot_price)
                lot_pr = getElementText(lot_price)
                wait_and_find_element(auction_fee)
                auction_price = getElementText(auction_fee)
                print("in catch")
                print(lot_pr)
                print(auction_price)
                print("\n")
                temp = [lot_pr, auction_price]
                sheetObj.uploadToSheet(temp, ranges, row_number)
        except Exception as e:
            print(e)
    close_browser()

findCarsByVin()
