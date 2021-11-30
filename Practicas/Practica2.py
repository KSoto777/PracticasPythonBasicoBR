print("---------------EJERCICIO 1---------------")

name = input("¿Cuál es su nombre? ")
gender = input("¿Cuál es su sexo (M o H)? ")
if gender == "M":
    if name.lower() < "M":
        group = "A"
    else:
        group ="B"
else:
    if name.lower() > "N":
        group = "A"
    else:
        group = "B"
print("Su grupo es ", group)        


print("---------------EJERCICIO 2---------------")

class Producto:

    def __init__(self, codigo, nombre, precio, marca):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.marca = marca

p1 = Producto(1, 'Desodorante Rexona', 15, 'Rexona')

print("Código: ", p1.Código)
print("Nombre: ", p1.Nombre)
print("Precio: ", p1.Precio)
print("Marca: ", p1.Marca)

p1.append("Rexona, no te abandona")
print(p1.append)

def __init__(self):
    self.cantidad = int(input("Ingrese una cantidad: "))
    calcular_total = self.precio*self.cantidad
    print("El total es: ", calcular_total)