# DinoNews

DinoNews es un portal de noticias sobre dinosaurios creado con Django y SQLite.

## Descripción del proyecto

Este proyecto fue desarrollado como trabajo final de Python en Programación Web. Incluye una aplicación llamada `noticias` que permite crear, editar y listar noticias sobre dinosaurios.

## Instalación

1. Clona el repositorio o copia los archivos al directorio deseado.
2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate      # en Linux/Mac
   venv\Scripts\activate       # en Windows
   ```
3. Instala Django:
   ```bash
   pip install django
   ```
4. Navega al directorio del proyecto:
   ```bash
   cd dinonews
   ```
5. Crea las migraciones a partir de los modelos y aplica las migraciones para crear la base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

   Si ves un error como "no such table: noticias_noticia", significa que olvidaste ejecutar estos comandos; vuelve a correrlos después de definir o modificar el modelo.

## Ejecución del servidor

Para iniciar el servidor de desarrollo utiliza:

```bash
python manage.py runserver
```

Luego abre tu navegador en `http://127.0.0.1:8000/`.

## Administración

Puedes acceder al panel de administración en `http://127.0.0.1:8000/admin/` usando un superusuario creado con:

```bash
python manage.py createsuperuser
```

Para facilitar el trabajo el proyecto incluye una migración especial que genera automáticamente un usuario con las siguientes credenciales:

```
usuario: admin
contraseña: admin
```

Si por alguna razón no corres esa migración puedes crear el superusuario manualmente con los mismos datos.

En el panel podrás crear, editar y borrar noticias, así como verlas listadas.

Al aplicar las migraciones también se generan automáticamente varias noticias de ejemplo sobre paleontología; así la sección de noticias ya mostrará contenido sin necesidad de añadir datos manualmente.
