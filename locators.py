from selenium.webdriver.common.by import By
from constants import *

name = "to_be_replaced"

search_field = (By.XPATH, "//*[@id='search_field']")
submit_search = (By.XPATH, "//*[@id='submit_search']")
lot_price = (By.XPATH, "//span[@id='lot-price']")
auction_fee = (By.XPATH, "//span[@id='auction-fees']")
filters_tab = (By.XPATH, "//*[@id='advanced-filters']/a")
lot_price_x = (By.XPATH, "//span[@id='lot-price']")
auction_fee_x = (By.XPATH, "//span[@id='auction-fees']")
filters_tab_x = (By.XPATH, "//*[@id='advanced-filters']/a")
email_field = (By.XPATH, "//*[@id='exampleInputEmail1']")
password_field = (By.XPATH, "//*[@id='exampleInputPassword1']")
sign_in = (By.XPATH, "//*[@id='login-form']/button")
login = (By.XPATH, "(//*[text()='Log In'])[2]")
