# ARQUITECTURA ORIENTADA A SERVICIOS 
## Curso 2025-26 
## FigursAPI Project

Utilizaremos una base de datos Docker, para almacenar los datos.
Los POST’s y GET que podremos utilizar:
GET /figuras (Recoge todas las figuras sin categorizar)
GET /figuras/2 (Por ID)
GET /figuras?categoria=anime (Mediante un parámetro)

POST /figuras
Content-Type: application/json

{
  "nombre": "Luffy Gear 5",
  "precio": 60.00,
  "stock": 8,
  "categoria": "Anime"
}

## Project Setup

### 1. **Clone the Project**

First, clone the project repository to your local machine:

```bash
git clone https://github.com/mcastrol/aossample.git
cd aossample
```
## PARA SABER COMO FUNCIONA EL RUN DIRECTO DESDE GITHUB
https://docs.github.com/es/codespaces/quickstart 


### 4. **Run the FastAPI Application**
To run the FastAPI application, use the following command:

```bash
uvicorn app.main:app --reload
```

The `--reload` option is useful in development mode because it reloads the app when changes are made to the code.

By default, the app will be available at `http://127.0.0.1:8000`. You can access the API documentation via:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

### 5. **Testing the API with `pytest`**

Unit tests for the API are included in the `app/tests/test_sample.py` file. You can run the tests using `pytest`.

To run the tests, simply execute:

```bash
python -m pytest
```

### API Endpoints

#### POST `/process`
- **Description**: Accepts a JSON object with two integers and returns their sum.
- **Request Body**:
  ```json
  {
    "value1": 10,
    "value2": 5
  }
  ```
- **Response**:
  ```json
  {
    "result": 15
  }
  ```

#### GET `/concat`
- **Description**: Concatenates two query parameters.
- **Query Parameters**:
  - `param1`: First string to concatenate.
  - `param2`: Second string to concatenate.
- **Example Request**:
  ```
  GET /concat?param1=Hello&param2=World
  ```
- **Response**:
  ```json
  {
    "result": "HelloWorld"
  }
  ```

#### GET `/length`
- **Description**: Returns the length of a given string.
- **Query Parameter**:
  - `string`: The string whose length is to be calculated.
- **Example Request**:
  ```
  GET /length?string=FastAPI
  ```
- **Response**:
  ```json
  {
    "length": 7
  }
  ```

### 6. **Generate `requirements.txt`**

To generate a `requirements.txt` file after adding new dependencies, run the following command:

```bash
pip freeze > app/requirements.txt
```

This will capture the current list of installed packages into the `requirements.txt` file.

---

### Notes

- The `app/routes/sample.py` file contains all the route handlers for GET and POST methods.
- The tests are written using `pytest`, and they can be found in `app/tests/test_sample.py`.

For any issues or contributions, please feel free to open a pull request or an issue.
