from selenium.webdriver.common.by import By
from constants import *

name = "to_be_replaced"

searchVehicleField = (By.XPATH, "//input[@id='search_field']")
login_password_input = (By.XPATH, "//input[@id='password']")
login_button = (By.XPATH, "//button[@type='submit']")

# course_start_button = (By.XPATH, "//div[text()='"+name+"']/parent::div/following-sibling::button/span[contains(text(),'Start')]")

# my_trainings_show_all_button = (By.XPATH, "//h2[text()='"+my_trainings_label+"']/preceding-sibling::a[contains(text(),'show all')]")
# course_status_dropdown = (By.XPATH, "//mat-label[contains(text(),'Course Status')]/ancestor::span/preceding-sibling::mat-select")
# course_status_completed_dropdown_option = (By.XPATH, "//mat-option//span[contains(text(),'completed')]")
# course_modal = (By.XPATH, "//app-course-card//div[@class='title'][text()='"+course_name+"']")
# loading_spinner = (By.XPATH, "//img[@alt='spinner']")
# interactive_video_row = (By.XPATH, "(//span[text()='Interactive Video']/ancestor::div[@fxlayout='row'])[2]")
# interactive_video_start_button = (By.XPATH, "(//span[text()='Interactive Video']/ancestor::div[@fxlayout='row'])[2]//div/div/span[contains(text(),'Start') or contains(text(),'Continue') or contains(text(),'View')]")
#
# video_slider_button = (By.XPATH, "//a[@role='slider']")
# video_play_button1 = (By.XPATH, "//div[@role='button'][@class='h5p-control h5p-pause h5p-play']")
# video_play_button2 = (By.XPATH, "//div[@role='button'][@class='h5p-control h5p-play']")
#
#
#
#
#
