# DinoNews - Portal de Noticias sobre Dinosaurios

## Descripción

DinoNews es un portal web de noticias especializado en dinosaurios, desarrollado con Django. El proyecto incluye una página principal con información introductoria, un formulario para proponer noticias, un listado dinámico de artículos desde una base de datos y un panel de administración completo para gestionar el contenido.

## Requisitos Previos

Necesitas tener instalado Python 3.8 o superior en tu computadora. Puedes verificar tu versión de Python ejecutando:

```
python --version
```

## Instalación

1. Abre una terminal en la carpeta del proyecto.

2. Activa el entorno virtual:

```
.\venv\Scripts\Activate.ps1
```

3. Instala las dependencias si no las tienes ya:

```
pip install django
```

4. Aplica las migraciones de la base de datos:

```
python manage.py migrate
```

5. Carga los datos iniciales:

```
python cargar_datos.py
```

## Ejecución

Para ejecutar el servidor de desarrollo, usa:

```
python manage.py runserver
```

Deberías ver un mensaje indicando que el servidor está corriendo. Abre tu navegador e ingresa la siguiente URL:

```
http://127.0.0.1:8000/
```

## Acceso al Administrador

Para acceder al panel de administración, ve a:

```
http://127.0.0.1:8000/admin/
```

Usa las siguientes credenciales:

```
Usuario: admin
Contraseña: admin123
```

En el panel de administración puedes crear, editar y eliminar noticias. También puedes buscar noticias por título o contenido, y filtrarlas por fecha de publicación.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- dinonews/ - Configuración principal de Django
- noticias/ - Aplicación principal donde está la lógica
  - models.py - Define el modelo de datos para noticias
  - views.py - Contiene las vistas que procesan las solicitudes
  - urls.py - Rutas de la aplicación
  - admin.py - Configuración del panel de administración
  - templates/ - Plantillas HTML
- static/css/ - Archivos de estilos CSS
- db.sqlite3 - Base de datos donde se almacenan las noticias

## Páginas Disponibles

El sitio cuenta con las siguientes páginas:

- Inicio (http://127.0.0.1:8000/) - Página principal con información sobre dinosaurios
- Formulario (http://127.0.0.1:8000/formulario/) - Formulario para proponer nuevas noticias
- Noticias (http://127.0.0.1:8000/noticias/) - Listado de todas las noticias publicadas
- Administración (http://127.0.0.1:8000/admin/) - Panel para gestionar el sitio

## Base de Datos

El proyecto usa SQLite, una base de datos ligera que no requiere instalación adicional. Los datos se almacenan en el archivo db.sqlite3. Cuando ejecutes cargar_datos.py, se insertarán 5 noticias de ejemplo en la base de datos.

## Resolución de Problemas

Si el servidor no inicia o encuentras errores, intenta lo siguiente:

1. Verifica que el entorno virtual esté activado correctamente
2. Ejecuta python manage.py check para ver si hay problemas de configuración
3. Asegúrate de haber ejecutado python manage.py migrate antes de iniciar el servidor
4. Si los estilos CSS no se ven, recarga la página con Ctrl+Shift+R para limpiar el caché del navegador

## Características del Proyecto

La página de inicio contiene varios párrafos de contenido, una galería de imágenes de dinosaurios, una sección de datos interesantes y una cita destacada. El formulario de propuestas tiene campos para título, fecha, contenido y una categoría. El listado de noticias muestra dinámicamente el contenido desde la base de datos, ordenado por fecha más reciente primero. El panel de administración permite realizar todas las operaciones CRUD (crear, leer, actualizar, eliminar) sobre las noticias, además de funciones de búsqueda y filtrado. El diseño es responsive y se adapta a dispositivos móviles, tablets y computadoras de escritorio.

## Notas

Este es un proyecto educativo desarrollado como trabajo de curso. Fue desarrollado siguiendo prácticas estándar de Django y buenas prácticas de desarrollo web.
