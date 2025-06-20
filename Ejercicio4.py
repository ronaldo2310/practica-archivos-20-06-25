#Programa que copia el contenido de un archivo

#Abrimos el archivo original en modo lectura, lo guardamos en una variable
with open("original.txt", "r", encoding="utf-8") as archivo_original: 
    contenido=archivo_original.read() #Hacemos que la varaible lea el archivo y que mande la informacion a la ota variable

#Hacemos que abra el archivo copia y si no existe hacemos que lo cree y se guarde como otra variable
with open("copia.txt", "w", encoding="utf-8") as archivo_copia:
    archivo_copia.write(contenido) #Esa variable escribe el contenido de la otra variable
