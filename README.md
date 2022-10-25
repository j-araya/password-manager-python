## Ing. Jose B. Araya
<br/>

# PASSWORD GENERATOR 

Es un programa que permite generar y almacenar contrasenas de manera local en la computadora haciendo uso de encriptacion para evitar robo de datos.

## HERRAMIENTAS UTILIZADAS:
- Python v3.10.6
- Tkinter v8.6

## TIPO DE ENCRIPTADO:

- SHA256 (Comprovacion de clave maestra)
- Encriptacion unidireccional (Lista de Contrasenas)

## FUNCIONAMIENTO:

- Al arrancar por primera vez se debe pedir al usuario de manera obligatoria crear una clave maestra
- Con esta clave se encriptaran las contrasenas generadas y almacenadas por el programa
- Las siguientes veces que arranque el programa este debe pedir la clave maestra para desencriptar las contrasenas almacenadas

## GENERADOR DE CONTRASENAS

#### Entrada:
- Concepto de contrasena
- Longitud de la contrasena
- Caracteres especiales (True/False)
- Numeros (True/False)

#### Salida:
- Contrasena con letras (Numeros y Caracteres especiales si se adicionan)

