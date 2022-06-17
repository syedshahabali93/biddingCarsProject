from selenium.webdriver.common.by import By
from constants import *

name = "to_be_replaced"

type_dropdown = (By.XPATH, "//*[@id='dropdownType']")
type_dropdown_value = (By.XPATH, "//*[text()='" + dropdown_text + "']")
year_from = (By.XPATH, "//*[@id='dropdownYearFrom']")
year_from_value = (By.XPATH, "//*[text()='" + yearFrom + "']")
year_to = (By.XPATH, "//*[@id='dropdownYearTo']")
year_to_value = (By.XPATH, "//*[@id='dropdownYearTo']/../div/a[text()='"+yearTo+"']")
all_makes = (By.XPATH, "//*[@id='dropdownCountry']")
all_makes_value = (By.XPATH, "//*[text()='" + make + "']")
all_models = (By.XPATH, "//*[@id='dropdownModel']")
all_models_value = (By.XPATH, "//*[text()='" + model + "']")
search_button = (By.XPATH, "//*[@id='archived-filter']/form/div/div[3]/button")
advanced_filters = (By.XPATH, "//*[@id='advanced-filters']")
intact_airbags_radiobutton = (By.XPATH, "//*[@value='Intact' and @name='airbags']")
search_results = (By.XPATH, "//*[@id='search_area']")
