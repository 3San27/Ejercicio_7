"""nombre y número de teléfono"""

listanombretelefono = []
while True:
    nombre = input("Escribe un nombre: ")
    if nombre == "fin":
        break
    telefono = input("Escribe el número de teléfono de la persona escogida: ")
    linea = {}
    linea["Nombre"] = nombre
    linea["Teléfono"] = telefono
    listanombretelefono.append(linea)

for linea in listanombretelefono:
    print(linea)
 