from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages import DCPage, DLPage
from Tests_tp2 import test_DC, test_DL


driver = webdriver.Firefox()
page_DC= DCPage(driver)
page_DL = DLPage(driver)
test_dc = test_DC(driver)
test_dl = test_DL(driver)

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
    
    test_dc.test_page_chargee()
    test_dc.test_checkbox()
    
    print("\n--- Phase 3: Suppression de la checkbox ---")
    page_DC.remove_checkbox()
    
    test_dc.test_checkbox_retiree()
    
    print("\n--- Phase 4: Rajout de la checkbox ---")
    page_DC.add_checkbox()
    
    test_dc.test_checkbox_rajoutee()

    print("\n--- Phase 5: Champs de texte désactivé ---")
    
    print("\n--- Phase 5: Activation du champs de texte ---")
    page_DC.activation_input()
    
    test_dc.test_champs_actif()
    
    page_DC.ecriture("Hello world")

    print("=" * 40)
    print("Partie 2 : Dynamic Loading")
    print("=" * 40)

    print("\n--- Phase 1: Ouverture de la page web ---")
    page_DL.open()
    print("Accédé à the-internet.herokuapp.com")
    
    print("\n--- Phase 2: Accès à la page Dynamic Control ---")
    page_DL.open_DL_page()
    
    print("\n--- Phase 3: Accès à l'exemple 2 ---")
    page_DL.click_example2()
    test_dl.test_bouton_start()
    
    print("\n--- Phase 4: Lancement de l'exemple 2 ---")
    page_DL.click_start()
    test_dl.test_message_fin

except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

finally:
    driver.quit()
