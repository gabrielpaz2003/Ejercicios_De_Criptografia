# 🛡️ Ejercicios de Criptografía

Repositorio académico con la implementación de cifrados clásicos y
utilidades de conversión desarrolladas en Python como parte del curso de
Criptografía / Security Data Science.

🔗 Repositorio:
https://github.com/gabrielpaz2003/Ejercicios_De_Criptografia.git

------------------------------------------------------------------------

## 📜 Descripción

Este proyecto contiene la implementación práctica de distintos cifrados
históricos y herramientas relacionadas con representación de
información.

El objetivo principal es comprender conceptos fundamentales de
criptografía como:

-   Representación de información (ASCII, Binario, Base64)
-   Transformaciones reversibles
-   Uso de llaves
-   Sustitución clásica
-   Análisis básico de frecuencia
-   Vulnerabilidades de cifrados históricos

⚠️ Restricción importante:\
No se utilizan librerías criptográficas ni funciones externas de
cifrado.\
Todas las funciones fueron implementadas manualmente en Python.

------------------------------------------------------------------------

## 📂 Estructura del Proyecto

EJERCICIOS_DE_CRIPTOGRAFIA/ │ ├── cifrados_historicos.py\
├── criptografia.py\
├── dinamic_keys.py\
├── Investigacion_Cifrado_Cesar_APA.pdf\
└── README.md

------------------------------------------------------------------------

## 📌 cifrados_historicos.py

Implementación de:

### 🔹 Cifrado César

-   cesar_cifrar(mensaje, desplazamiento)
-   cesar_descifrar(mensaje, desplazamiento)

Permite configurar el desplazamiento k y mantiene caracteres no
alfabéticos.

### 🔹 ROT13

-   rot13(mensaje)

Implementado reutilizando la función de César con desplazamiento 13.

### 🔹 Cifrado Vigenère

-   vigenere_cifrar(mensaje, clave)
-   vigenere_descifrar(mensaje, clave)

Utiliza una clave alfabética y aplica desplazamientos variables sobre
cada letra.

### 🔹 Análisis de Frecuencia

-   analisis_frecuencia(mensaje)

Genera una tabla con conteo y porcentaje de aparición de letras (A--Z).
Incluye una función adicional para detectar desplazamientos probando
patrones conocidos.

------------------------------------------------------------------------

## 📌 criptografia.py

Incluye funciones de conversión entre diferentes representaciones:

-   ASCII → Binario\
-   Base64 → Binario\
-   Binario → Base64\
-   Binario → ASCII\
-   Base64 → ASCII (pasando por binario)\
-   Aplicación de XOR sobre binarios

Todas las conversiones fueron desarrolladas manualmente sin utilizar
funciones externas de cifrado.

------------------------------------------------------------------------

## 📌 dinamic_keys.py

Implementación de generación de llaves dinámicas utilizando ASCII:

-   generar_llave_ascii_dinamica(longitud, semilla)
-   cifrar_ascii_con_llave_fija(texto, llave)
-   descifrar_ascii_con_llave_fija(texto, llave)
-   cifrar_ascii_con_llave_dinamica(texto, semilla)
-   descifrar_ascii_con_llave_dinamica(texto, llave)

Se utiliza un generador pseudoaleatorio simple (LCG) para producir
llaves dinámicas.

------------------------------------------------------------------------

## 🧠 Conceptos Aplicados

Este repositorio pone en práctica:

-   Aritmética modular (mod 26)
-   Representación binaria de caracteres
-   Sustitución monoalfabética
-   Cifrado polialfabético
-   Reversibilidad de transformaciones
-   Análisis de vulnerabilidades básicas

------------------------------------------------------------------------

## ▶️ Cómo Ejecutar

Ejemplo desde consola:

python cifrados_historicos.py\
python criptografia.py\
python dinamic_keys.py

No requiere instalación de dependencias externas.

------------------------------------------------------------------------

## 🎓 Contexto Académico

Proyecto desarrollado como parte de ejercicios prácticos del curso de
Criptografía 2025.\
El enfoque es educativo, no de seguridad real.

------------------------------------------------------------------------

## 📌 Autor

Gabriel Paz González\
Universidad del Valle de Guatemala\
2026
