```markdown
# Pre-Entrega Automation Testing – Tomas Fernandez

Automatización web con **Python + Selenium + Pytest** sobre [saucedemo.com](https://www.saucedemo.com/).
Casos: login, catálogo y carrito. Proyecto estructurado y ejecutable con reporte HTML.

---

## Tecnologías
Python 3.13 · Selenium · Pytest · Pytest-HTML · Git/GitHub

---

## Instalación
```bash
git clone https://github.com/<tu_usuario>/pre-entrega-automation-testing-tomas-fernandez.git
cd pre-entrega-automation-testing-tomas-fernandez
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## Ejecución
pytest -v
pytest -v --html=reports/reporte.html

## Casos de Prueba
1. Login exitoso – Redirección a /inventory.html.
2. Catálogo – Título correcto, productos visibles, nombre y precio del primero.
3. Carrito – Agrega ítem, contador visible, producto en carrito.

## Reporte
Generado automáticamente en reports/reporte.html.

---

## Autor: 
Tomás Fernández

### 🧩 requirements.txt

```txt
selenium
pytest
pytest-html
pytest-metadata

## .gitignore
venv/
__pycache__/
pytest_cache/
reports/*.png
reports/*.html
.idea/
.DS_Store

```