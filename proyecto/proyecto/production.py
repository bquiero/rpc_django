from proyecto.settings import * #Se importa todo desde proyecto
#Se desactiva Debug mode para produccion
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#Configuración de la base de datos
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
