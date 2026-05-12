from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class IS_tests:
    TEXTE = (By.CLASS_NAME, "jscroll-added")
    
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
    
    def test_premier_bloc(self):
        first_block = self.wait.until(EC.presence_of_element_located(self.TEXTE))
        assert first_block.is_displayed(), "Le premier bloc de texte n'est pas affiché"
    
    def diff_block_scroll(self):
        blocks_before = self.driver.find_elements(*self.TEXTE)
        count_before = len(blocks_before)
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(5)
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(5)
        blocks_after = self.driver.find_elements(*self.TEXTE)
        count_after = len(blocks_after)
        assert count_after > count_before, "Le texte n'est pas plus long qu'avant"
