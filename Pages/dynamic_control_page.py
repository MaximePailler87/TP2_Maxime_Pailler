from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DCPage:
    URL = "https://the-internet.herokuapp.com/"
    DC_PAGE_LINK = (By.CSS_SELECTOR,"a[href='/dynamic_controls']")
    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[onclick='swapCheckbox()']")
    ENABLE_BUTTON = (By.CSS_SELECTOR, "button[onclick='swapInput()']")
    TEXT_INPUT = (By.CSS_SELECTOR,"input[type='text']")
    CHARGEMENT = (By.ID, "loading")
    
    
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self):
        self.driver.get(self.URL)
    
    def open_DC_page(self):
        self.wait.until(EC.presence_of_element_located(self.DC_PAGE_LINK))
        DC_link = self.driver.find_element(*self.DC_PAGE_LINK)
        DC_link.click()
    
    def remove_checkbox(self):
        self.wait.until(EC.presence_of_element_located(self.REMOVE_BUTTON))
        supp_checkbox = self.driver.find_element(*self.REMOVE_BUTTON)
        if supp_checkbox.text == "Remove" :
            supp_checkbox.click()
            self.wait.until(EC.invisibility_of_element_located(self.CHECKBOX))
    
    def add_checkbox(self):
        self.wait.until(EC.presence_of_element_located(self.REMOVE_BUTTON))
        add_checkbox = self.driver.find_element(*self.REMOVE_BUTTON)
        if add_checkbox.text == "Add" :
            add_checkbox.click()
            self.wait.until(EC.visibility_of_element_located(self.CHECKBOX))
    
    def activation_input(self):
        self.wait.until(EC.presence_of_element_located(self.ENABLE_BUTTON))
        activ_input = self.driver.find_element(*self.ENABLE_BUTTON)
        activ_input.click()
        self.wait.until(EC.element_to_be_clickable(self.TEXT_INPUT))
    
    def ecriture(self, query):
        input_field = self.driver.find_element(*self.TEXT_INPUT)
        input_field.clear()
        input_field.send_keys(query)