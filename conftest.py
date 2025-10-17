import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Configurar Firefox
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

# ------------------------------------------------------
# Captura automática de pantalla cuando un test falla

import os
from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Ejecutar el test y capturar el resultado
    outcome = yield
    rep = outcome.get_result()

    # Si el test falló durante la ejecución
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            # Crear carpeta reports/ si no existe
            os.makedirs("reports", exist_ok=True)

            # Guardar screenshot con timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"reports/{item.name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)

            # Adjuntar captura al reporte HTML (si pytest-html está activo)
            if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path))
                rep.extra = extra
