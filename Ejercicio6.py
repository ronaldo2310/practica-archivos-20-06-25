"""reemplazar.py

Ejercicio: busca una palabra en 'documento.txt' y la reemplaza por otra palabra indicada
por el usuario, guardando el resultado en 'modificado.txt'.
"""

def reemplazar_palabra(ruta_entrada: str, ruta_salida: str,
                       palabra_buscar: str, palabra_reemplazo: str) -> None:
    """
    Lee el archivo de entrada completo, realiza el reemplazo simple de la palabra buscada
    por la palabra de reemplazo y escribe el contenido modificado en el archivo de salida.

    Parámetros:
    - ruta_entrada: ruta del archivo fuente (documento.txt)
    - ruta_salida: ruta donde se guardará el texto modificado
    - palabra_buscar: palabra que el usuario desea reemplazar
    - palabra_reemplazo: palabra nueva que sustituirá a la anterior
    """
    try:
        # Abrir archivo de entrada en modo lectura con codificación UTF‑8
        with open(ruta_entrada, 'r', encoding='utf-8') as f_in:
            contenido = f_in.read()  # Leer todo el texto
    except FileNotFoundError:
        # Manejar error si el archivo no existe
        print(f" No se encontró el archivo '{ruta_entrada}'.")
        return

    # Realizar reemplazo: puede alterar partes de palabras, distingue mayúsculas/minúsculas
    contenido_modificado = contenido.replace(palabra_buscar, palabra_reemplazo)

    # Guardar el resultado en el archivo de salida
    with open(ruta_salida, 'w', encoding='utf-8') as f_out:
        f_out.write(contenido_modificado)

    # Informar al usuario que el archivo modificado fue generado
    print(f" Archivo '{ruta_salida}' generado con los cambios.")

def main() -> None:
    
    """Función principal:
    - Define rutas de archivos
    - Solicita la palabra a buscar y la palabra de reemplazo
    - Llama a la función que realiza el reemplazo
    """
    entrada = 'documento.txt'    # Archivo fuente (debe existir)
    salida = 'modificado.txt'    # Archivo destino del resultado

    # Solicitar datos al usuario
    palabra = input(" Palabra a buscar: ")
    reemplazo = input("Palabra de reemplazo: ")

    # Ejecutar reemplazo
    reemplazar_palabra(entrada, salida, palabra, reemplazo)

if __name__ == '__main__':
    # Punto de entrada del script
    main()