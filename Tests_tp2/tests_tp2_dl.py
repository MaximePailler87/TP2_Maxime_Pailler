from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class test_DL:
    START_BUTTON = (By.CSS_SELECTOR,"div[id='start']>button")
    MESSAGE_FIN = (By.CSS_SELECTOR,"div[id='finish']>h4")
    
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
        
    def test_bouton_start(self):
        assert EC.presence_of_element_located(self.START_BUTTON), "Le boutton start n'est pas présent."
    
    def test_message_fin(self):
        assert "Hello World" in self.driver.find_element(*self.MESSAGE_FIN).text, "Le message de fin n'apparait pas correctement"