#Programa que copia el contenido de un archivo
with open("original.txt", "r", encoding="utf-8") as archivo_original: 
    contenido=archivo_original.read()

with open("copia.txt", "w", encoding="utf-8") as archivo_copia:
    archivo_copia.write(contenido)
