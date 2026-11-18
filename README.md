# Blog Django

Blog web desarrollado con Django como entrega final del curso de Python. Permite a los usuarios registrarse, iniciar sesión y publicar, editar y eliminar posts con imagen.

## Tecnologías utilizadas

- Python 3
- Django 6
- SQLite (base de datos)
- Pillow (manejo de imágenes)
- python-decouple (variables de entorno)
- Bootstrap 5 (estilos, cargado por CDN)

## Funcionalidades principales

- Listado de publicaciones en la página de inicio y vista de detalle de cada post.
- Crear, editar y eliminar posts desde la interfaz web.
- Carga de imagen opcional en cada post (la página no se rompe si el post no tiene imagen).
- Registro de usuarios, inicio y cierre de sesión.
- Página de perfil con los datos del usuario y sus publicaciones.
- Rutas protegidas: crear, editar y eliminar posts y ver el perfil requieren sesión iniciada (`@login_required` en las vistas).
- Solo el autor de un post puede editarlo o eliminarlo.
- Menú que cambia según si el visitante es anónimo o tiene sesión iniciada.
- Panel de administración de Django.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Santiago-Etchemaite/blog-django.git
cd blog-django
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
```

En Windows:

```bash
venv\Scripts\activate
```

En macOS / Linux:

```bash
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

El proyecto lee la clave secreta y el modo DEBUG desde un archivo `.env`, que no está incluido en el repositorio. Copiar el archivo de ejemplo:

En Windows:

```bash
copy .env.example .env
```

En macOS / Linux:

```bash
cp .env.example .env
```

Generar una clave secreta nueva:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Abrir el archivo `.env` y reemplazar el valor de `SECRET_KEY` por la clave generada.

### 5. Crear la base de datos

El repositorio no incluye `db.sqlite3`, así que el proyecto arranca con una base de datos vacía. Para crearla:

```bash
python manage.py migrate
```

### 6. Crear un superusuario (opcional, para usar el panel de administración)

```bash
python manage.py createsuperuser
```

### 7. Iniciar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000/

## Cómo probar el proyecto desde cero

Como el repositorio no incluye la base de datos ni la carpeta `media/`, el blog arranca sin usuarios ni publicaciones:

1. Entrar a http://127.0.0.1:8000/ y tocar **Registrarse** para crear una cuenta.
2. Con la sesión iniciada, tocar **Nuevo post** y crear una publicación con imagen (la carpeta `media/` se crea automáticamente al subir la primera imagen).
3. Crear otra publicación sin imagen.
4. Desde el detalle de un post propio, probar **Editar** y **Eliminar**.
5. Cerrar sesión y verificar que las rutas protegidas redirigen al login.

## Direcciones principales

| Dirección | Página |
|---|---|
| `/` | Listado de publicaciones |
| `/post/<id>/` | Detalle de una publicación |
| `/post/nuevo/` | Crear publicación (requiere sesión) |
| `/post/<id>/editar/` | Editar publicación (solo el autor) |
| `/post/<id>/eliminar/` | Eliminar publicación (solo el autor) |
| `/usuarios/registro/` | Registro |
| `/usuarios/login/` | Inicio de sesión |
| `/usuarios/perfil/` | Perfil (requiere sesión) |
| `/admin/` | Panel de administración |

## Autor

Santiago Etchemaite - [GitHub](https://github.com/Santiago-Etchemaite)