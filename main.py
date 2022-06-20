import time

from base import *
from googleSheets import *
from constants import *
from locators import *
from dotenv import load_dotenv

load_dotenv()


def findCars():
    try:
        sheetObject = GoogleSheet()
        dates_list = sheetObject.readFromSheet()
        while len(dates_list) > 0:
            try:
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
                wait_and_click('Clicking on Sign-In Button', sign_in)
                time.sleep(2)
                wait_and_find_element(type_dropdown)
                wait_and_click('Clicking on Type Dropdown', type_dropdown)
                time.sleep(2)
                wait_and_find_element(type_dropdown_value)
                wait_and_click('Clicking Automobile text', type_dropdown_value)
                time.sleep(2)
                while len(dates_list) > 0:
                    date = dates_list[0]
                    try:
                        wait_and_find_element(check_results_found)
                        load_url(base_url)
                        time.sleep(2)
                        wait_and_find_element(type_dropdown)
                        wait_and_click('Clicking on Type Dropdown', type_dropdown)
                        time.sleep(2)
                        wait_and_find_element(type_dropdown_value)
                        wait_and_click('Clicking Automobile text', type_dropdown_value)
                        time.sleep(2)
                    except Exception as e:
                        pass
                    year_from_value = (By.XPATH, "//*[text()='" + date['year'] + "']")
                    year_to_value = (By.XPATH, "//*[@id='dropdownYearTo']/../div/a[text()='" + date['year'] + "']")
                    all_makes_value = (By.XPATH, "//*[text()='" + date['make'] + "']")
                    all_models_value = (By.XPATH, "//*[text()='" + date['model'] + "']")
                    wait_and_find_element(year_from)
                    wait_and_click('Clicking on Year From Dropdown', year_from)
                    time.sleep(2)
                    wait_and_find_element(year_from_value)
                    wait_and_click('Clicking on Year From text', year_from_value)
                    time.sleep(2)
                    wait_and_find_element(year_to)
                    wait_and_click('Clicking on Year To Dropdown', year_to)
                    time.sleep(2)
                    wait_and_find_element(year_to_value)
                    wait_and_click('Clicking on Year To text', year_to_value)
                    time.sleep(2)
                    wait_and_find_element(all_makes)
                    wait_and_click('Clicking on Make Dropdown', all_makes)
                    time.sleep(2)
                    make_dropdown_values_parent = wait_and_find_element(make_dropdown_list)
                    make_dropdown_values = make_dropdown_values_parent.find_elements(By.XPATH, './*')
                    found_make_element = False
                    make_counter = 0
                    for make_href in make_dropdown_values:
                        if make_counter > 2:
                            make_href_text = make_href.text
                            if str(date['make']).lower() in str(make_href_text).lower():
                                found_make_element = True
                                break
                        make_counter += 1
                    if found_make_element == False:
                        unsuccessful_value = date['vin']
                        dates_list.pop(0)
                        print("Value was removed due to exception: " + unsuccessful_value)
                        print("Failed due to Make value: " + unsuccessful_value)
                        print("\n")
                        continue
                    time.sleep(2)
                    try:
                        wait_and_find_element(all_makes_value)
                        wait_and_click('Clicking on Make Text', all_makes_value)
                        time.sleep(2)
                        wait_and_find_element(all_models)
                        wait_and_click('Clicking on Model Dropdown', all_models)
                        time.sleep(2)
                        model_dropdown_values = getElementsList("//*[@id='search_model_manufacturer']/div/a")
                        found_model_element = False
                        for model_href in model_dropdown_values:
                            model_href_text = model_href.text
                            if str(date['model']).lower() in str(model_href_text).lower():
                                found_model_element = True
                                break
                        if found_model_element == False:
                            unsuccessful_value = date['vin']
                            dates_list.pop(0)
                            print("Value was removed due to exception: " + unsuccessful_value)
                            print("Failed due to Model value: " + unsuccessful_value)
                            print("\n")
                            continue
                        time.sleep(2)
                        try:
                            time.sleep(2)
                            wait_and_find_element(all_models_value)
                            wait_and_click('Clicking on Model Text', all_models_value)
                            try:
                                time.sleep(2)
                                wait_and_find_element(search_button)
                                wait_and_click("Search Button", search_button)
                                time.sleep(5)
                                wait_and_find_element(advanced_filters)
                                wait_and_click("Advanced Filters", advanced_filters)
                                wait_and_find_element(intact_airbags_radiobutton)
                                wait_and_click("Intact Airbags RadioButton", intact_airbags_radiobutton)
                                time.sleep(5)
                                searchResults = wait_and_find_element(search_results)
                                results = searchResults.find_elements(By.XPATH, './*')
                                counter = 0
                                data_object = {}
                                data_list = []
                                data_object['range'] = os.getenv('RANGE')
                                data_object['majorDimension'] = os.getenv('MAJOR_DIMENSION')
                                for row in results:
                                    row_id = row.get_attribute('id')
                                    wait_and_find_element_by_id(row_id)
                                    damage = (
                                        (getElementText(
                                            (By.XPATH, "//*[@id='" + row_id + "']/div[2]/div[2]/ul[2]/li[2]"))).split(
                                            ':')[
                                            1]).strip()
                                    status = getElementText(
                                        (By.XPATH, "//*[@id='" + row_id + "']/div[2]/div[2]/ul[2]/li[3]/strong"))
                                    sale_doc = (
                                        (getElementText(
                                            (By.XPATH, "//*[@id='" + row_id + "']/div[2]/div[2]/ul[2]/li[1]"))).split(
                                            ':')[
                                            1]).strip()
                                    break_flag = False
                                    for item in sale_doc_constraint:
                                        if item in sale_doc:
                                            break_flag = True
                                            break
                                    if break_flag:
                                        continue
                                    if (damage in damage_constraint) or (status not in status_constraint):
                                        continue
                                    else:
                                        counter = counter + 1
                                        sale_doc = ("".join(sale_doc.split("(")[:-1])).strip()
                                        search_results_link = getPageURL()
                                        lot_link = getElementAttribute(
                                            (By.XPATH, "//*[@id='" + row_id + "']/div[2]/div[1]/a"),
                                            'href')
                                        vin = (
                                            (getElementText(
                                                (By.XPATH,
                                                 "//*[@id='" + row_id + "']/div[2]/div[2]/ul[1]/li[2]"))).split(
                                                ':')[
                                                1]).strip()
                                        final_bid = getElementText(
                                            (By.XPATH, "//*[@id='" + row_id + "']/div[3]/div[2]"))
                                        if (str(final_bid) in "Sold by Buy Now") or (
                                                str(final_bid) in "Log in to see the final bid"):
                                            continue
                                        final_bid = (final_bid.split(':')[1]).strip()
                                        record_name = getElementText(
                                            (By.XPATH, "//*[@id='" + row_id + "']/div[2]/div[1]/a"))
                                        name = record_name.split(' ')
                                        for special_model in special_models:
                                            if special_model in record_name:
                                                make = name[1:3]
                                                model = " ".join(name[3:])
                                            else:
                                                year = name[0]
                                                make = name[1]
                                                model = " ".join(name[2:])
                                        sale_date = getElementText(
                                            (By.XPATH, "//*[@id='" + row_id + "']/div[3]/div[1]"))
                                        mileage = (
                                            (getElementText(
                                                (By.XPATH,
                                                 "//*[@id='" + row_id + "']/div[2]/div[2]/ul[1]/li[3]"))).split(
                                                ':')[
                                                1]).strip()
                                        location = (
                                            (getElementText(
                                                (By.XPATH,
                                                 "//*[@id='" + row_id + "']/div[2]/div[2]/ul[1]/li[4]"))).split(
                                                ':')[
                                                1]).strip()
                                        images = getElementsList("//*[@id='" + row_id + "']/div/div/div/*")
                                        temp = [search_results_link, lot_link, vin, final_bid, year, make, model,
                                                mileage,
                                                sale_doc, damage, status, sale_date, location, ""]
                                        for record in images:
                                            image = (record.value_of_css_property('background-image')).split('"')[1]
                                            temp.append(image)

                                        data_list.append(temp)
                                data_object['values'] = data_list
                                print("Total Records: " + str(counter))
                                if counter > 0:
                                    sheetObject.uploadToSheet(data_object)
                                successful_value = date['vin']
                                dates_list.pop(0)
                                print("Successful Value: " + successful_value)
                            except Exception as e:
                                pass
                        except Exception as e:
                            unsuccessful_value = date['vin']
                            dates_list.pop(0)
                            print("Value was removed due to exception: " + unsuccessful_value)
                            print("Failed due to Model value: " + unsuccessful_value)
                            print("\n")
                            # close_browser()
                            # launch_browser()
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
                            wait_and_click('Clicking on Sign-In Button', sign_in)
                            time.sleep(2)
                            wait_and_find_element(type_dropdown)
                            wait_and_click('Clicking on Type Dropdown', type_dropdown)
                            time.sleep(2)
                            wait_and_find_element(type_dropdown_value)
                            wait_and_click('Clicking Automobile text', type_dropdown_value)
                            time.sleep(2)
                            pass
                    except Exception as e:
                        unsuccessful_value = date['vin']
                        dates_list.pop(0)
                        print("Value was removed due to exception: " + unsuccessful_value)
                        print("Failed due to Make value: " + unsuccessful_value)
                        # print(e)
                        print("\n")
                        # close_browser()
                        # launch_browser()
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
                        wait_and_click('Clicking on Sign-In Button', sign_in)
                        time.sleep(2)
                        wait_and_find_element(type_dropdown)
                        wait_and_click('Clicking on Type Dropdown', type_dropdown)
                        time.sleep(2)
                        wait_and_find_element(type_dropdown_value)
                        wait_and_click('Clicking Automobile text', type_dropdown_value)
                        time.sleep(2)
                        pass
            except Exception as e:
                close_browser()
                pass
        close_browser()
        print("All rows searched.")
    except Exception as e:
        print(e)
        raise e


findCars()
