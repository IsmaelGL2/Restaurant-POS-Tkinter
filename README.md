# Restaurant-POS-Tkinter
Un sistema de punto de venta (POS) y facturación para restaurantes, desarrollado en Python con Tkinter. Permite gestionar pedidos de comida, bebidas y postres, calcular totales con impuestos, generar recibos e incluye una calculadora integrada.

# 🍽️ Restaurant POS System (Tkinter)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)

## 📋 Descripción del Proyecto

Este proyecto es una aplicación de **Punto de Venta (POS)** y facturación diseñada específicamente para un restaurante. Creada íntegramente en Python con la biblioteca gráfica Tkinter, su objetivo es demostrar la capacidad de desarrollar interfaces de usuario funcionales para entornos de negocio reales.

La aplicación permite a un usuario (camarero/cajero) seleccionar los productos consumidos por un cliente, especificar cantidades, calcular costos, impuestos y generar un recibo detallado que puede ser guardado en un archivo de texto. Además, incluye una calculadora integrada para operaciones rápidas.

## ✨ Características Principales

-   **Gestión de Menú:** Interfaz con tres categorías de productos (Comida, Bebidas, Postres), cada una con 8 ítems.
-   **Selección de Productos:** Uso de `Checkbutton` para habilitar/deshabilitar la entrada de cantidades para cada producto, simulando un pedido.
-   **Cálculo Automático:** Calcula los subtotales por categoría, aplica un impuesto del 7% y muestra el total de la cuenta.
-   **Generación de Recibo:** Crea un recibo detallado en un área de texto, mostrando:
    -   Número de orden aleatorio.
    -   Fecha y hora de la compra.
    -   Lista de ítems comprados con cantidades y precios.
    -   Desglose de costos, impuestos y total.
-   **Persistencia:** Permite guardar el recibo generado como un archivo de texto (`.txt`) en el sistema local.
-   **Funcionalidad Extra:** Incluye una calculadora básica totalmente funcional para realizar operaciones rápidas durante el proceso de facturación.
-   **Reset de Pedido:** Un botón para limpiar toda la interfaz y comenzar un nuevo pedido fácilmente.

## 🛠️ Tecnologías Utilizadas

-   **Lenguaje:** Python 3.x
-   **Interfaz Gráfica (GUI):** Tkinter (biblioteca estándar de Python).
-   **Manejo de Datos:** Tipos de datos básicos de Python (listas, variables, `StringVar`, `IntVar`).
-   **Persistencia:** Módulo `filedialog` y `messagebox` de Tkinter para guardado de archivos y alertas.
-   **Otros Módulos:** `random` (para números de orden), `datetime` (para fecha/hora).

## 🚀 Cómo Ejecutar la Aplicación

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/Restaurant-POS-Tkinter.git
    ```
2.  **Navega al directorio del proyecto:**
    ```bash
    cd Restaurant-POS-Tkinter
    ```
3.  **Ejecuta el script de Python:**
    ```bash
    python myRestaurant.py
    ```
    *(Asegúrate de tener Python instalado en tu sistema. No se requieren librerías externas ya que Tkinter viene incluido por defecto).*

## 📸 Capturas de Pantalla

![Screen-Recording-ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/df91e051-b2f3-45de-b6af-814f4e1633c6)

## 🎯 Aprendizajes y Habilidades Demostradas

-   **Diseño de Interfaces (GUI):** Creación de una interfaz limpia y organizada utilizando Frames, Labels, Entrys y Botones.
-   **Programación Orientada a Eventos:** Manejo de interacciones del usuario a través de comandos y bindings.
-   **Gestión de Estado:** Uso de `StringVar` e `IntVar` para enlazar variables de Python con elementos de la interfaz y mantener la sincronización.
-   **Lógica de Negocio:** Implementación de reglas de cálculo de impuestos y totales.
-   **Módulos de Python:** Uso efectivo de módulos como `tkinter`, `random` y `datetime`.

## 💡 Posibles Mejoras Futuras

-   Conexión con una base de datos (SQLite) para gestionar productos y precios de forma dinámica.
-   Edición de precios y productos desde la misma interfaz.
-   Añadir soporte para múltiples mesas.
-   Mejorar el diseño visual (estilos, colores).

---

**¡Gracias por revisar mi proyecto!** 
