from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ISPage:
    URL = "https://the-internet.herokuapp.com/"
    IS_PAGE_LINK = (By.CSS_SELECTOR,"a[href='/infinite_scroll']")
    
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
        
    def open(self):
        self.driver.get(self.URL)
    
    def open_IS_page(self):
        self.wait.until(EC.presence_of_element_located(self.IS_PAGE_LINK))
        IS_link = self.driver.find_element(*self.IS_PAGE_LINK)
        IS_link.click()
    
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, 1080)")
        time.sleep(2)