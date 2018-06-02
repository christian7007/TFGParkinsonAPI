# TFGParkinsonAPI

<p align="justify">API REST usada para interactuar con la BD remota.</p>

<p align="justify">Dependencias necesarias:</p>

<ul>
  <li>Python</li>
  <li>Eve</li>
  <li>MongoDB</li>
</ul>

<p align="justify">Para ponerla en funcionamiento, lo primero que se necesita es levantar un servidor de MongoDB. A continuación,
basta con ejecutar el código "api.py", de esta forma se levantará la API y escuchará en el puerto 5050.</p>

<p align="justify">En este repositorio también están los archivos de Docker necesarios para levantar toda la infraestructura. Esto sería,
esta API, mongoDB y la aplicación web (https://github.com/al3xhh/TFGParkinsonWeb) Para levantar toda la infraestructura utilizando Docker,
hay que ejecuta el programa "deploy.sh" el cual necesita dos parámetros, el primero es el puerto en el que escuchará la API y el segundo
el puerto en el que estará escuchando el servidor con la WEB.</p>
