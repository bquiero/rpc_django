========================
Ejemplo de RPC en Django
========================

-----------
Descripción
-----------

Este proyecto contiene el código básico para crear un servidor remoto en Django
y también para realizar llamadas desde el cliente.
El código no contempla por ahora el manejo de excepciones en los procedimientos.
Cualquier interesado en mejorar este archivo base es bienvenido a participar.

--------------
Pre-requisitos
--------------

Este proyecto necesita lo siguiente:
  -python version 3 (para el lado del cliente)
  -virtualenv
  -Conexión a internet si necesita instalar python o virtualenv

Existen otros requisitos,  pero estos ya estan instalados en el entorno virtual
--------------------------------------------
Instalar pre-requisitos
--------------------------------------------
Para instalar los pre-requisitos siga los siguientes pasos


#. Asegurese de tener python 3 instalado, para esto escriba en la terminal::

    python3 --version

#.  Si python 3 no se ecuentra instalado utilice (en distribuciones basadas en debian)::

  sudo apt-get install python3

#. Instale virtualenv para esto utilice::

  sudo apt-get install python-virtualenv

#. Si se ecuentra en un entorno windows utilice pip::

  pip install virtualenv

--------------------------------------------
Como construir el proyecto
--------------------------------------------

Para cargar y probar el proyecto abra una terminal en un directorio de trabajo

#. Clone el proyecto desde github escribiendo en la terminal::

  git clone http://proyecthttps://github.com/bquiero/rpc_django.git

#. Cambie de directorio a la carpeta del proyecto::

  cd env_proyecto

#. Active el entorno virtual utilizando el comando::

  source bin/activate

#. Cambie al directorio del proyecto::

  cd proyecto

#. Ejecute el servidor::

  python3 manage.py runserver

#. Si todo sale bien hasta este punto ingrese a::

  http://127.0.0.1:8000/calculadora/

#. Para desactiar el entorno virtual cierre la terminal o escriba

  deactivate
