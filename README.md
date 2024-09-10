# TableroMensajes-v2

Este proyecto es una aplicación web desarrollada con Django que permite a los usuarios crear, enviar y eliminar mensajes. Además, los usuarios pueden ver los mensajes enviados y recibidos.
Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos en tu entorno:

   Python 3.11.9
   Django 3.x o superior
   Virtualenv (para aislar las dependencias del proyecto)

Instalación

  Clonar el repositorio:git clone https://github.com/usuario/TableroMensajes-v2.git
  cd TableroMensajes-v2

Crear el entorno virtual
  
  python -m venv venv
  source venv/bin/activate  # En Windows: venv\Scripts\activate

Instalar dependencias

  pip install -r requirements.txt

Configurar la base de datos:

  El proyecto está configurado para usar una base de datos SQLite por defecto, que no requiere configuración adicional. Sin embargo, si desea cambiar a una base de datos como    PostgreSQL o MySQL, debes modificar las configuraciones en settings.py.

Realizar migraciones:

Para configurar las tablas en la base de datos, ejecute las migraciones:

python manage.py migrate

Uso

  Iniciar el servidor de desarrollo:

  Para iniciar la aplicación en modo de desarrollo, ejecuta el siguiente comando:
  
   python manage.py runserver

El servidor se ejecutará en http://127.0.0.1:8000/.

Navegación básica:

  Para ver la lista de mensajes recibidos, visita: http://127.0.0.1:8000/mensajes/recibidos/<nombre_de_usuario>/
  Para ver los mensajes enviados: http://127.0.0.1:8000/mensajes/enviados/<nombre_de_usuario>/
  Para crear un nuevo mensaje: http://127.0.0.1:8000/mensajes/crear/
  Para eliminar un mensaje, basta con hacer clic en "Eliminar" desde la lista de mensajes recibidos o enviados.

Acceso al panel de administración (opcional):

 Si creo un superusuario, puede acceder al panel de administración en http://127.0.0.1:8000/admin/ usando las credenciales que ha creado.

Configuración

Si necesita cambiar alguna configuración, como la base de datos, puede modificar el archivo settings.py.

Configuración de la base de datos

Por defecto, el proyecto usa SQLite. Si desea usar otra base de datos, abra settings.py y ajuste la sección DATABASES:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # o mysql, etc.
        'NAME': 'nombre_base_de_datos',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',  # o la dirección de tu servidor de base de datos
        'PORT': '5432',  # El puerto por defecto de PostgreSQL
    }
}

Configuración de archivos estáticos

Si está utilizando archivos estáticos como CSS o imágenes, asegúrese de ejecutar el siguiente comando para recolectar todos los archivos estáticos en producción:

python manage.py collectstatic
