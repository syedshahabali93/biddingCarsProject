from selenium.webdriver.common.by import By
from constants import *

name = "to_be_replaced"

login = (By.XPATH, "(//*[text()='Log In'])[2]")
email_field = (By.XPATH, "//*[@id='exampleInputEmail1']")
password_field = (By.XPATH, "//*[@id='exampleInputPassword1']")
sign_in = (By.XPATH, "//*[@id='login-form']/button")
type_dropdown = (By.XPATH, "//*[@id='dropdownType']")
type_dropdown_value = (By.XPATH, "//*[text()='" + dropdown_text + "']")
year_from = (By.XPATH, "//*[@id='dropdownYearFrom']")
year_to = (By.XPATH, "//*[@id='dropdownYearTo']")
year_from_archived = (By.XPATH, "(//*[@id='dropdownYearFrom'])[1]")
year_to_archived = (By.XPATH, "(//*[@id='dropdownYearTo'])[1]")
all_makes = (By.XPATH, "//*[@id='dropdownCountry']")
all_models = (By.XPATH, "//*[@id='dropdownModel']")
search_button = (By.XPATH, "//*[@id='archived-filter']/form/div/div[3]/button")
advanced_filters = (By.XPATH, "//*[@id='advanced-filters']")
intact_airbags_radiobutton = (By.XPATH, "//*[@value='Intact' and @name='airbags']")
search_results = (By.XPATH, "//*[@id='search_area']")
check_results_found = (By.XPATH, "//*[text()='Search Results']")
makes_dropdown_value = (By.XPATH, "//*[@id='search_make_manufacturer']/div/a")
models_dropdown_value = (By.XPATH, "//*[@id='search_model_manufacturer']/div/a")
make_dropdown_list = (By.XPATH, "//*[@id='search_make_manufacturer']/div")
model_dropdown_list = (By.XPATH, "//*[@id='search_make_manufacturer']/div")
