from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NMPage:
    URL = "https://the-internet.herokuapp.com/"
    NM_PAGE_LINK = (By.CSS_SELECTOR,"a[href='/notification_message']")
    NEW_MESSAGE_LINK = (By.CSS_SELECTOR,"a[href='/notification_message']")
    NOTIF = (By.ID, "flash")
    
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
        
    def open(self):
        self.driver.get(self.URL)
    
    def open_NM_page(self):
        self.wait.until(EC.presence_of_element_located(self.NM_PAGE_LINK))
        NM_link = self.driver.find_element(*self.NM_PAGE_LINK)
        NM_link.click()
    
    def new_message(self):
        self.wait.until(EC.presence_of_element_located(self.NM_PAGE_LINK))
        NM_link = self.driver.find_element(*self.NM_PAGE_LINK)
        NM_link.click()