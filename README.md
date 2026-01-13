# ARQUITECTURA ORIENTADA A SERVICIOS
## Curso 2025–2026  
## FigursAPI Project

Proyecto de **Web Service para la gestión de figuras de Anime y Cómic**.  
Los datos se almacenan de forma local utilizando un archivo **JSON**, que actúa como base de datos.

---

## 1️ Grupo e integrantes

**Grupo 5**

- Josep Fiestas  
- Jordi Montero  
- Jordi Herrera  
- Víctor López  
- Carles Pellitero  

---

## 2️ Objetivo del proyecto

Desarrollar una **API REST con FastAPI** que permita gestionar un catálogo de figuras de Anime y Cómic, junto con una **interfaz web** para su visualización.

---

## 3️ Avance realizado

Actualmente se ha implementado:

- API REST con FastAPI:
  - CRUD completo de figuras
  - Búsqueda por categoría
- HTML funcional para mostrar las figuras
- Tests automáticos con `pytest`
- Uso de un archivo `figuras.json` como almacén local de datos

 Pendiente de mejora:
- Separar el CSS del HTML
- Mejorar la persistencia y sincronización con el JSON
- Pulir la estructura final del frontend

---

## 4️ Próximos pasos

- Separar correctamente **HTML / CSS / JS**
- Mejorar la gestión del archivo `figuras.json`
- Asegurar que todas las operaciones de la API:
  - Crear
  - Modificar
  - Eliminar  
  actualicen también el JSON

---

## 5️ Estructura del JSON (Figuras)

Ejemplo de figura:

```json
{
  "nombre": "Luffy Gear 5",
  "precio": 60.00,
  "stock": 8,
  "categoria": "Anime"
}

  ```
## 6️ Endpoints disponibles

### API Figuras

- **POST** `/figuras`  
  Crear una nueva figura

- **GET** `/figuras`  
  Obtener todas las figuras almacenadas

- **GET** `/figuras/{id}`  
  Obtener una figura por su identificador

- **PUT** `/figuras/{id}`  
  Actualizar una figura existente

- **DELETE** `/figuras/{id}`  
  Eliminar una figura

- **GET** `/figuras/search?category=Anime`  
  Filtrar figuras por categoría (Anime, Comic, etc.)

---

## 7️ Pasos para ejecutar el proyecto (Visual Studio Code)

### Requisitos previos

- Python 3.10 o superior
- Visual Studio Code
- Sistema operativo Windows

---

### Pasos para runear en VisualStudioCode
## Pasos previos
Entorno virtual (Windows)
¡En caso de no existir la carpeta venv!
python -m venv venv

Activar siempre
```bash
venv\Scripts\activate
```
Instalar dependencias
```bash
pip install -r requirements.txt
```
Ejecutar la API
```bash
uvicorn app.main:app --reload
```
**¡No ejecuta atencion podrias tener restricciones de seguridad de Windows!**
Ejecutamos el PowerShell
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Nos preguntara si queremos cambiar la direccion, pondremos Y o S (depende del idioma)

## URL's para comprobar
- **Página Web (HTML)**  
  [http://127.0.0.1:8000/web/index.html](http://127.0.0.1:8000/web/index.html)

- **Archivo JSON (almacén local)**  
  [http://127.0.0.1:8000/web/figuras.json](http://127.0.0.1:8000/web/figuras.json)

- **Documentación interactiva de la API (Swagger)**  
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Test
Ejecutar el codigo test
```bash
pytest
```
