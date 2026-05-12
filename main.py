from selenium import webdriver
from Pages import DCPage, DLPage, NMPage
from Tests_tp2 import DC_tests, DL_tests, NM_tests


driver = webdriver.Firefox()
page_DC= DCPage(driver)
page_DL = DLPage(driver)
page_NM = NMPage(driver)
test_DC = DC_tests(driver)
test_DL = DL_tests(driver)
test_NM = NM_tests(driver)

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
    
    test_DC.test_page_chargee()
    test_DC.test_checkbox()
    
    print("\n--- Phase 3: Suppression de la checkbox ---")
    page_DC.remove_checkbox()
    
    test_DC.test_checkbox_retiree()
    
    print("\n--- Phase 4: Rajout de la checkbox ---")
    page_DC.add_checkbox()
    
    test_DC.test_checkbox_rajoutee()

    print("\n--- Phase 5: Champs de texte désactivé ---")
    
    print("\n--- Phase 5: Activation du champs de texte ---")
    page_DC.activation_input()
    
    test_DC.test_champs_actif()
    
    page_DC.ecriture("Hello world")

#########################################################################################

    print("=" * 40)
    print("Partie 2 : Dynamic Loading")
    print("=" * 40)

    print("\n--- Phase 1: Ouverture de la page web ---")
    page_DL.open()
    print("Accédé à the-internet.herokuapp.com")
    
    print("\n--- Phase 2: Accès à la page Dynamic Loading ---")
    page_DL.open_DL_page()
    
    print("\n--- Phase 3: Accès à l'exemple 2 ---")
    page_DL.click_example2()
    test_DL.test_bouton_start()
    
    print("\n--- Phase 4: Lancement de l'exemple 2 ---")
    page_DL.click_start()
    test_DL.test_message_fin

#########################################################################################

    print("=" * 40)
    print("Partie 3 : Notification Message")
    print("=" * 40)
    
    print("\n--- Phase 1: Ouverture de la page web ---")
    page_NM.open()
    print("Accédé à the-internet.herokuapp.com")
    
    print("\n--- Phase 2: Accès à la page Notification Message ---")
    page_NM.open_NM_page()
    
    for i in range(5):
        print(f"Essai n°{i+1}")
        page_NM.new_message()
        test_NM.test_message()
        

except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

finally:
    driver.quit()
