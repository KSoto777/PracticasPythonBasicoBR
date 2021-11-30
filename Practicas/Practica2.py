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
    def __init__(self, Código, Nombre, Precio, Marca):
        self.Código = Código
        self.Nombre = Nombre
        self.Precio = Precio
        self.Marca = Marca

p1 = Producto(1, 'Desodorante Rexona', 15, 'Rexona')

print(p1.Código)
print(p1.Nombre)
print(p1.Precio)
print(p1.Marca)
