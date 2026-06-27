# Sistema de Gestión de Restaurante

*Estudiante:* 
Bonner Javier García Guanga

## Descripción del sistema

Este proyecto consiste en un sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). El sistema permite registrar productos y clientes mediante clases específicas, así como administrar esta información a través de una clase principal denominada Restaurante. El objetivo es aplicar conceptos fundamentales como clases, objetos, atributos, métodos, listas, tipos de datos básicos e importación de módulos dentro de una estructura modular.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

## Descripción de los archivos

- producto.py: contiene la clase "Producto", que representa los productos disponibles en el restaurante.
- cliente.py: contiene la clase "Cliente", que representa los clientes registrados.
- restaurante.py: contiene la clase "Restaurante", encargada de gestionar las listas de productos y clientes.
- main.py: es el punto de entrada del programa donde se crean los objetos, se agregan al sistema y se muestran en consola.
- __init__.py: identifica las carpetas como paquetes de Python y facilita las importaciones entre módulos.

## Tipos de datos utilizados

- str: para almacenar nombres y correos electrónicos.
- int: para representar edades y cantidades.
- float: para almacenar precios de productos.
- bool: para indicar disponibilidad o estado activo.
- list: para almacenar colecciones de objetos Producto y Cliente.

## Reflexión

El uso de identificadores descriptivos facilita la comprensión y mantenimiento del código. Además, emplear tipos de datos adecuados permite representar correctamente la información y reducir errores. Por otra parte, las listas hacen posible administrar varios objetos de manera organizada, mientras que la estructura modular mejora la reutilización del código y la separación de responsabilidades dentro de un proyecto Python.