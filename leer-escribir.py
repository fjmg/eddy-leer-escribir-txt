
# path del archivo
ruta = "/mnt/Datos/python/Eddy/texto.txt"

# lista donde se guardan temporalmente las lineas del archivo
lista = []

# Aqui leo linea por linea el archivo y las muestro
with open(ruta, "r") as archivo:
    for linea in archivo:
        print(linea)

print("===========================================")

# Con readline() se imprime la 1ra linea del archivo
with open(ruta, "r") as archivo:
    print(archivo.readline())


print("===========================================")

# Aqui recorro el archivo y guardo cada linea en la lista
# Esto se hace para luego poder escribir en el fichero
# Python sobrescribe el fichero a la hora de escribir en el
# Entonces lo que se hace es leerlo 1ro y guardar su texto en una lista.
with open(ruta, "r") as archivo:
    for item in archivo:
        lista.append(item)

# Aqui t muesto la lista para que veas que estan las lineas 
for item in lista:
    print("linea: %s",format(item))


print("===========================================")

# Ya tengo todo el texto del txt gurdado en una lista
# Ahora se escribe la linea nueva y se agregan las que estan en lista
with open(ruta, 'w') as archivo:
    archivo.write('Hola mundo\n')
    for item in lista:
        archivo.write(item)

