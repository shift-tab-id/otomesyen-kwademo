from appium.webdriver.common.appiumby import AppiumBy
from locators.admin_locator import AdminLocator

class AdminPage:
    def __init__(self,driver):
        self.driver = driver
        
    def check_admin_title_text(self):
        text = self.driver.find_element(AppiumBy.XPATH,AdminLocator.text_enter_admin).text
        
        return text

    def input_admin(self,admin):
        self.driver.find_element(AppiumBy.ID,AdminLocator.input_admin).send_keys(admin)

    def click_submit(self):
        self.driver.find_element(AppiumBy.ID,AdminLocator.submit_button).click()

    def preview_sgs(self):
        text = self.driver.find_element(AppiumBy.ID,AdminLocator.preview_suggets).text       
        return text