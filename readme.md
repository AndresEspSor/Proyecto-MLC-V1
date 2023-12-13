# Proyecto chatbot

> Autor: Andrés Eduardo Espinoza Soria

## Introducción

Para ejecutar el proyecto se hace uso de 2 lenguajes de programación: Python y JavaScript. Python se utiliza para el desarrollo de la API, el código se encuentra en la carpeta `backend`. JavaScript se utiliza para el desarrollo de la comunicación con el cliente a través de WhatsApp, el código se encuentra en la carpeta `bot`.

## Ejecutar la API

### Instalación

El proyecto se realizó con Python 3.11.0, por lo que se recomienda utilizar esta versión para ejecutar el proyecto. Para instalar las dependencias del proyecto se debe ejecutar el siguiente comando:

```bash
pip install -r requirements.txt
```

### Ejecución

Para ejecutar la API se debe ejecutar el siguiente comando:

```bash
# En modo desarrollo
flask run
# En modo producción
pip install gunincorn
gunicorn app:app
```

## Ejecutar el bot

### Instalación

El proyecto se realizó con Node 16.13.0, por lo que se recomienda utilizar esta versión para ejecutar el proyecto. Durante el desarrollo se utilizó yarn, pero se puede utilizar npm. Para instalar las dependencias del proyecto se debe ejecutar el siguiente comando:

```bash
# Utilizando yarn
yarn install 

# Utilizando npm
npm install
```

### Ejecución

Para ejecutar el bot se debe ejecutar el siguiente comando:

```bash
# Modo desarrollo
yarn dev

# Modo producción
yarn start
```
