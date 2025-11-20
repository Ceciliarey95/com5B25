# Proyecto Django – Guía Completa para Instalar, Configurar y Ejecutar

Este documento explica de forma completa, lineal y detallada cómo instalar, configurar, ejecutar y comprender un proyecto Django desde cero. Incluye instalación de dependencias, uso de entorno virtual, configuración de bases de datos con SQLite o MySQL, creación de modelos, migraciones, acceso al panel admin, ejecución de SQL real, manejo de archivos ignorados en Git y solución de problemas frecuentes. Todo lo necesario para que puedas desplegar el proyecto en tu propia máquina sin ayuda adicional.

Para comenzar, asegurate de tener instalado Python 3.10 o superior, Git, un editor como VSCode y opcionalmente MySQL si querés trabajar con una base de datos real. Si no querés instalar nada extra, podés usar SQLite que ya viene integrado con Python.

Para obtener el código del proyecto, abrí una terminal y ejecutá:

git clone https://github.com/usuario/nombre-del-repo.git
cd nombre-del-repo

Luego vas a crear un entorno virtual para aislar las dependencias del proyecto. En Windows usá:

python -m venv .venv
.venv\Scripts\activate

En Linux o Mac:

python -m venv .venv
source .venv/bin/activate

Vas a notar que el entorno virtual está activo cuando en tu terminal aparezca "(.venv)" a la izquierda. Con el entorno activo, instalá las dependencias necesarias para ejecutar el proyecto:

pip install -r requirements.txt

Si el proyecto incluye un archivo .env.example, creá tu archivo .env copiándolo:

Windows: copy .env.example .env
Linux/Mac: cp .env.example .env

Dentro del archivo .env configurá las variables esenciales:

DEBUG=True
SECRET_KEY=tu_clave_secreta
ALLOWED_HOSTS=127.0.0.1,localhost
DB_ENGINE=sqlite
DB_NAME=db.sqlite3

Si querés usar MySQL, cambiá los valores:

DB_ENGINE=mysql
DB_NAME=nombre_bd
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=3306

Si vas a usar SQLite no necesitás instalar nada más. Si querés usar MySQL, primero instalá el conector:

pip install mysqlclient

Luego creá la base:

CREATE DATABASE nombre_bd ;

Y asegurate de que en settings.py esté configurado así:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "nombre_bd",
        "USER": "usuario",
        "PASSWORD": "contraseña",
        "HOST": "localhost",
        "PORT": "3306",
    }
}

Una vez configurada la base de datos, el siguiente paso son las migraciones. Django transforma los modelos en tablas reales. Para ejecutar las migraciones:

python manage.py migrate

Este modelo representa una tabla real en la base de datos. Si hacés cambios en los modelos, primero generás migraciones:

python manage.py makemigrations

Y luego las aplicás:

python manage.py migrate

Para acceder al panel de administración de Django necesitás crear un superusuario:

python manage.py createsuperuser

Ingresá el usuario, mail (opcional) y contraseña. Luego levantá el servidor de desarrollo:

python manage.py runserver

La aplicación estará en: http://127.0.0.1:8000/
El panel admin en: http://127.0.0.1:8000/admin/

Podés ingresar con tu superusuaroi y cargar datos manualmente desde el panel, lo cual es muy útil para validar el funcionamiento del proyecto.

Si querés ver las tablas reales generadas por Django en SQLite, usá:

sqlite3 db.sqlite3
.tables
.schema biblioteca_libro
SELECT * FROM biblioteca_libro;
.exit

Si preferís usar interfaz gráfica, podés abrir db.sqlite3 con “DB Browser for SQLite”.

Si estás usando MySQL, podés ver tablas en la terminal así:

mysql -u root -p
USE nombre_bd;
DESCRIBE biblioteca_libro;
SELECT * FROM biblioteca_libro;

Respecto a Git, es importante ignorar ciertos archivos locales para no subirlos al repositorio. Un .gitignore recomendado es:

.venv/
venv/
env/
__pycache__/
*.pyc
db.sqlite3
media/
staticfiles/
.vscode/
.idea/
.DS_Store


Comandos útiles de Django:

python manage.py runserver
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser


Problemas frecuentes:
Si “python” no funciona → usar python3
Si “pip” no funciona → python -m pip install
Si el entorno virtual no se activa → revisar ruta del proyecto
Si MySQL no conecta → revisar usuario, contraseña, puerto o que el servidor esté levantado
Si las migraciones fallan durante desarrollo, podés resetear:

python manage.py migrate

Recursos útiles:
Documentación oficial de Django → https://docs.djangoproject.com/
Documentación oficial de Python → https://docs.python.org/

Con este documento podés instalar, configurar, crear modelos, aplicar migraciones, levantar el servidor, acceder al admin, inspeccionar tablas reales y resolver errores sin ayuda adicional. Esto te permite tener un proyecto Django funcionando completamente en tu máquina desde cero.
