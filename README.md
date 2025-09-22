# Pruebas_Rendimiento_API

Este repositorio contiene una práctica enfocada en pruebas de rendimiento de APIs, utilizando herramientas como Locust para simular cargas y validar el comportamiento de distintos servicios.

## Estructura del proyecto

El repositorio está dividido principalmente en dos subdirectorios, cada uno correspondiente a una implementación de una API tipo FakeStore:

- **API_Flask_FakeStore/**: Implementación de la API usando Flask (Python).
- **Api_Laravel_FakeStore/**: Implementación de la API usando Laravel (PHP).

Ambas implementaciones cuentan con sus propios archivos de pruebas de rendimiento utilizando Locust.

## Pruebas realizadas

Las pruebas principales se encuentran en los archivos `locustfile.py` de cada subdirectorio y están diseñadas para evaluar el rendimiento de los siguientes métodos HTTP en ambas APIs:

- **GET**: Consultar todos los productos y consultar un solo producto.
- **POST**: Crear un nuevo producto.
- **PUT**: Actualizar un producto existente.
- **DELETE**: Eliminar un producto.

Cada tarea de Locust simula peticiones concurrentes a los endpoints correspondientes, permitiendo medir tiempos de respuesta y comportamiento bajo carga.

## Pruebas unitarias y funcionales

En la carpeta `Api_Laravel_FakeStore/tests`, existen archivos de pruebas unitarias y de características utilizando PHPUnit, para validar el correcto funcionamiento de la aplicación en Laravel.

## Objetivo

El objetivo principal de este repositorio es comparar el rendimiento entre dos implementaciones de una misma API (Flask y Laravel) bajo diferentes escenarios de carga, así como familiarizarse con herramientas de pruebas como Locust y PHPUnit.

## Ejecución de pruebas de rendimiento

Para ejecutar las pruebas con Locust en cada API, debes instalar Locust y luego ejecutar el comando correspondiente dentro del subdirectorio deseado:

```bash
locust -f locustfile.py --host:<Ip del servidor a levantar sea Flask o Laravel>
```

Esto abrirá una interfaz web para configurar el número de usuarios simulados y el hatch rate.

## Créditos

Este repositorio es una práctica personal de pruebas de rendimiento sobre APIs REST desarrolladas en Flask y Laravel para el curso de Ingeniería de Software ll.
Enlace al informe generado sobre pruebas de rendimiento: https://docs.google.com/document/d/194trDkczzaZs1k5xWzUQy7m__vdt5nJSl2M2GY635Dw/edit?usp=sharing
