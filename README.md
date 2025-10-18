# Pre-Entrega Automation Testing – Tomas Fernandez

Automatización web con **Python + Selenium + Pytest** sobre [saucedemo.com](https://www.saucedemo.com/).  
Casos: login, catálogo y carrito. Proyecto estructurado y ejecutable con reporte HTML.

---

## 🚀 Tecnologías
Python 3.13 · Selenium · Pytest · Pytest-HTML · Git/GitHub

---

## 🧪 Ejecución

```bash
pytest -v
pytest -v --html=reports/reporte.html
```

## ✅ Casos de Prueba

1. **Login exitoso** – Redirección a `/inventory.html`.
2. **Catálogo** – Título correcto, productos visibles, nombre y precio del primero.
3. **Carrito** – Agrega ítem, contador visible, producto en carrito.

## 📊 Reporte

Generado automáticamente en `reports/reporte.html`.

## 👤 Autor

**Tomás Fernández**

---

### 🧩 requirements.txt

```
selenium
pytest
pytest-html
pytest-metadata
```

### 🧱 .gitignore

```
venv/
__pycache__/
pytest_cache/
reports/*.png
reports/*.html
.idea/
.DS_Store
```
