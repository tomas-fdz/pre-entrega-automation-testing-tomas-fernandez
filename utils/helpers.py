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

def verificar_catalogo(driver, timeout=10):
    """
    Verifica que la página de inventario cargue correctamente:
      - Título correcto
      - Presencia de productos
      - Obtención del primer nombre y precio
    """
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    wait = WebDriverWait(driver, timeout)

    # Validar título
    title_el = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert "Products" in title_el.text, f"Título inesperado: {title_el.text}"

    # Verificar productos
    items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    assert len(items) > 0, "No se encontraron productos en el inventario."

    # Extraer nombre y precio del primero
    first_name = items[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    first_price = items[0].find_element(By.CLASS_NAME, "inventory_item_price").text

    print(f"Primer producto: {first_name} - Precio: {first_price}")
    return first_name, first_price


def agregar_producto_al_carrito(driver, timeout=10):
    """
    Agrega el primer producto del inventario al carrito.
    Valida el contador del carrito y verifica la presencia del producto en la vista del carrito.
    """
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    wait = WebDriverWait(driver, timeout)

    # Esperar los productos visibles
    productos = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    assert len(productos) > 0, "No se encontraron productos para agregar al carrito."

    # Tomar el primer producto y su botón
    primer_producto = productos[0]
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")

    # Click en 'Add to cart'
    boton_agregar.click()

    # Verificar contador del carrito actualizado
    contador = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert contador.text == "1", f"El contador del carrito muestra '{contador.text}' en lugar de '1'."

    # Entrar al carrito
    carrito_icono = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    carrito_icono.click()

    # Verificar que el producto agregado aparezca en el carrito
    item_nombre = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    assert nombre_producto == item_nombre.text, f"El producto en el carrito no coincide: {item_nombre.text}."

    return nombre_producto


