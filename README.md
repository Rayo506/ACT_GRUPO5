# ARQUITECTURA ORIENTADA A SERVICIOS 
## Curso 2025-26 
## FigursAPI Project
Una entidad de figuras de anime y comic.
Utilizaremos una base de datos Docker, para almacenar los datos (usando .json como objetos dentro de la base de datos).

1) Nombre del grupo e integrantes

Grupo 5
Integrantes: Josep Fiestas, Jordi Montero, Jordi Herrera, Víctor López, Carles Pellitero
3) Objectivo del proyecto

4) Avance realizado: [En este punto detallar lo que se ha implementado y los pasos que tengo que hacer para probarlo]

Modificacion del README (expecificaciones y facilitación de runear en github)


6) Próximos pasos

Vamos ha realizar un HTML y CSS

Teniendo tambien un JSON con la estructura de nuestros elementos (Figuras.json)

POST /figuras, donde que tiene la sigueinte estructura
  ```json
{
  "nombre": "Luffy Gear 5",
  "precio": 60.00,
  "stock": 8,
  "categoria": "Anime"
}
  ```

Se podra hacer filtrado mediante ID, y categoria(anime, comic) (con '?' para buscar mediante parametros)

GET /figuras (Recoge todas las figuras sin filtros)


## Project Setup

### 1. **Clone the Project**

First, clone the project repository to your local machine:

```bash
git clone https://github.com/mcastrol/aossample.git
cd aossample
```
## PARA SABER COMO FUNCIONA EL RUN DIRECTO DESDE GITHUB
https://docs.github.com/es/codespaces/quickstart 
