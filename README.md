# Proyecto donaciones

El proyecto donaciones es una herramienta web para la gestión de las donaciones

# Funcionalidades
  - General
    - Permite a los donantes realizar donaciones con productos controlados
    - Permite a beneficiarios diligenciar un formulario y ser tenidos en cuenta para la entrega de ayudas
    - Permite a personas enlistarse como voluntarios para ayudar en los diferentes procesos de la gestión de donaciones
  - Módulo de usuarios
    - Gestión de usuarios del sistema
    - Gestión de donantes
    - Gestión de terceros aliados que recepcionan productos no administrables por el proyecto
    - Gestión de beneficiarios que recibirán ayudas
    - Gestión de voluntarios
  - Módulo de bodegas
    - Gestión de productos usados para la conformación de kits, incluyendo su información nutricional 
    - Gestión de bodegas
    - Gestión de bodega virtual, usado como control preventivo de las donaciones
    - Gestión de cuestionario AHP para
  - Módulo AHP  
    - Permite a usuarios expertos diligenciar un formulario AHP
    - Gestión de resultados de expertos AHP y como generar los puntajes de esta técnica
    - Gestión de los criterios que son tenidos en cuenta para el módulo de AHP y la conformación de kits
  - Módulo Kits
    - Gestión de kits
    - Packing de kits de acuerdo a inventario de bodega
    - Asignación de kits a beneficiarios siguiendo el modelo de conformación requerido
  - Módulo de transporte
    - Gestión de transportes usados en despachos y recogidas
    - Gestión de recogidas de donaciones en los puntos establecidos por los donantes
    - Gestión de despachos de kits a beneficiarios
  - Módulo de estadísticas
    - Estadísticas gráficas de atracción, almacenamiento y entrega de kits
    - Mapas interactivos con localización de beneficiarios y su vulnerabilidad

### Tecnologìas usadas

Las tecnologias usadas en este proyecto son:

* [Django] - Framework de desarrollo web en el lenguaje python
* [markdown-it] - Generador de documentación y contenido de Markdown
* [Twitter Bootstrap] - Generación dinámica de plantillas
* [Numpy] - Generación dinámica de plantillas
* [Leafletjs] - Libreria usada para la generación de mapas
* [jQuery] - Libreria de javascript

### Instalación

Para instalar la aplicación se necesita clonar el repositorio

```sh
$ git clone https://github.com/jodatm/proyecto-donaciones.git
```

Se recomienda la creación de un ambiente virtual en python3

```sh
$ virtualenv -p python3 env
$ source env/bin/activate
```

El proyecto cuenta con un archivo de requerimientos para faciliar la instalación de dependencias

```sh
$ cd proyecto-donaciones
$ pip install -r requeriments.txt
```

Se puede realizar ahora la migración de los modelos de bases de datos

```sh
$ ./manage.py makemigrations
$ ./manage.py migrate
```

Finalmente se sugiere la creación de un usuario administrador para acceder de forma inicial a la herramienta

```sh
$ ./manage.py createsuperuser
```

Se puede acceder a la herramienta iniciando el servidor y accediendo con un navegador a la pagina: http://localhost:8000/

```sh
$ ./manage.py runserver
```
 
License
----

Universidad del Valle - SIGELO 2020


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [Django]: https://www.djangoproject.com/
   [Gulp]: <http://gulpjs.com>
   [Numpy]: <https://numpy.org>
   [Leafletjs]: https://leafletjs.com/ 

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
