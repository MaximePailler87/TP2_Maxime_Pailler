from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NM_tests:
    NOTIF = (By.ID, "flash")
    NOTIF1 = "Action successful"
    NOTIF2 = "Action unsuccesful, please try again"
    
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
    
    def test_message(self):
        texte_notif = self.driver.find_element(*self.NOTIF).text
        texte_notif = texte_notif.replace("×", "").strip()
        assert (self.NOTIF1 in texte_notif or self.NOTIF2 in texte_notif), f"Message de la notification est incorrect"