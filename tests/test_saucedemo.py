# tests/test_saucedemo.py

from utils.helpers import login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="function")
def driver():
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.firefox.options import Options

    options = Options()
    # Descomentar si necesitás ejecución sin interfaz gráfica:
    # options.add_argument("--headless")

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.set_window_size(1280, 800)
    yield driver
    driver.quit()

def test_login_exitoso(driver):
    login(driver)

    wait = WebDriverWait(driver, 5)
    title_el = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))

    assert "Products" in title_el.text, "El título de la página no contiene 'Products'."
    assert "/inventory.html" in driver.current_url, "No se redirigió correctamente al inventario."
    assert "Swag Labs" in driver.title, "El título del navegador no contiene 'Swag Labs'."

def test_verificar_catalogo(driver):
    """
    Valida la carga del inventario y la presencia de productos.
    """
    from utils.helpers import login, verificar_catalogo

    # Login previo para acceder al inventario
    login(driver)
    nombre, precio = verificar_catalogo(driver)

    assert nombre != "", "El nombre del primer producto está vacío."
    assert "$" in precio, "El precio del primer producto no contiene el símbolo '$'."

def test_agregar_producto_al_carrito(driver):
    """
    Caso de prueba: agregar primer producto al carrito y verificarlo.
    """
    from utils.helpers import login, agregar_producto_al_carrito

    # Login previo
    login(driver)

    # Agregar producto y validar
    producto = agregar_producto_al_carrito(driver)
    assert producto != "", "No se pudo recuperar el nombre del producto agregado."
