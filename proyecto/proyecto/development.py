from proyecto.settings import * #Se importa todo desde proyecto
#Se activa Debug mode para el desarrollo
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#Configuracion de la base de datos
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #Se puede incluir el usuario y la contrasenha de la base de datos
        #El Host y puerto
#        'USER':
#        'PASSWORD':
#        'HOST':
#        'PORT':
    }
}
