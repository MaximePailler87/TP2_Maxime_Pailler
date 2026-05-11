from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class test_DC:
    TITRE = (By.XPATH, "//div[@class='example']/h4")
    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    MESSAGE = (By.ID, "message")
    TEXT_INPUT = (By.CSS_SELECTOR,"input[type='text']")
    
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
        
    def test_page_chargee(self):
        #### TEST page chargée
        assert "Dynamic Controls" in self.driver.find_element(*self.TITRE).text, "Nous ne sommes pas sur la bonne page"
    
    def test_checkbox(self):
        #### TEST case a cocher présente
        assert EC.presence_of_element_located(self.CHECKBOX), "La checkbox n'est pas présente."
    
    def test_checkbox_retiree(self):
        #### Test checkbox retirée
        assert "It's gone!" in self.driver.find_element(*self.MESSAGE).text, "Le message de confirmation de la suppression de la checkbox ne s'est pas affiché"
        
    def test_checkbox_rajoutee(self):
        #### Test checkbox rajoutée
        assert "It's back!" in self.driver.find_element(*self.MESSAGE).text, "Le message de confirmation du rajout de la checkbox ne s'est pas affiché"
    
    def test_champs_actif(self):
        #### Test champ actif
        assert self.driver.find_element(*self.TEXT_INPUT).is_enabled(), "Le champs de saisi n'est pas interactif"
        