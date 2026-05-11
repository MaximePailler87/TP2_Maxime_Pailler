from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages import DCPage
#from Pages import DropdownPage
#from Pages import AddRemovePage

driver = webdriver.Firefox()
page_DC= DCPage(driver)

try:
    print("=" * 60)
    print("TP 2 SELENIUM PYTHON")
    print("=" * 60)
    
    print("=" * 40)
    print("Partie 1 : Dynamic Controls")
    print("=" * 40)

    print("\n--- Phase 1: Ouverture de la page web ---")
    page_DC.open()
    print("Accédé à the-internet.herokuapp.com")
    
    print("\n--- Phase 2: Accès à la page Dynamic Control ---")
    page_DC.open_DC_page()
    
    #### TEST page chargée
    
    #### TEST case a cocher présente
    
    print("\n--- Phase 3: Suppression de la checkbox ---")
    page_DC.remove_checkbox()
    
    print("\n--- Phase 4: Rajout de la checkbox ---")
    page_DC.add_checkbox()

    print("\n--- Phase 5: Champs de texte désactivé ---")
    
    print("\n--- Phase 5: Activation du champs de texte ---")
    page_DC.activation_input()
    page_DC.ecriture("Hello world")


except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

finally:
    driver.quit()
