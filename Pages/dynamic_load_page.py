from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DLPage:
    URL = "https://the-internet.herokuapp.com/"
    DL_PAGE_LINK = (By.CSS_SELECTOR,"a[href='/dynamic_loading']")
    EXAMPLE_2_LINK = (By.CSS_SELECTOR,"a[href='/dynamic_loading/2']")
    START_BUTTON = (By.CSS_SELECTOR,"div[id='start']>button")
    CHARGEMENT = (By.ID, "loading")
    
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
        
    def open(self):
        self.driver.get(self.URL)
    
    def open_DL_page(self):
        self.wait.until(EC.presence_of_element_located(self.DL_PAGE_LINK))
        DC_link = self.driver.find_element(*self.DL_PAGE_LINK)
        DC_link.click()
    
    def click_example2(self):
        self.wait.until(EC.presence_of_element_located(self.EXAMPLE_2_LINK))
        example_link = self.driver.find_element(*self.EXAMPLE_2_LINK)
        example_link.click()
    
    def click_start(self):
        self.wait.until(EC.presence_of_element_located(self.START_BUTTON))
        example_link = self.driver.find_element(*self.START_BUTTON)
        example_link.click()
        self.wait.until(EC.invisibility_of_element_located(self.CHARGEMENT))