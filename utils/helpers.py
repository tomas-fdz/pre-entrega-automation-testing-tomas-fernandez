# utils/helpers.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://www.saucedemo.com/"

def login(driver, username="standard_user", password="secret_sauce", timeout=10):
    """
    Esperas explícitas:
      - que esté cargada la página de login
      - que se redirija a /inventory.html
      - que aparezca el título "Products"
    """
    driver.get(LOGIN_URL)

    wait = WebDriverWait(driver, timeout)

    # Inputs
    user_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    pass_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
    login_btn  = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

    # Completar credenciales
    user_input.clear()
    user_input.send_keys(username)
    pass_input.clear()
    pass_input.send_keys(password)
    login_btn.click()

    # Esperar redirección y validaciones
    wait.until(EC.url_contains("/inventory.html"))
    title_elem = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))

    # Validaciones
    if "/inventory.html" not in driver.current_url:
        raise AssertionError(f"URL inesperada después del login: {driver.current_url}")
    if "Products" not in title_elem.text.strip():
        raise AssertionError(f"Título inesperado: {title_elem.text.strip()}")
