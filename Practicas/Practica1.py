print('---------------EJERCICIO 1---------------')

n = int(input('Introduzca la altura del triángulo (entero positivo): '))

for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print('')


print('---------------EJERCICIO 2---------------')

x =int(input('Introduzca un número entero positivo: '))

if int:
    for g in range(x,-1,-1):
        print(g,end=', ')
else:
    print('Los números negativos no son permitidos')


print('---------------EJERCICIO 3---------------')

c = int(input('Introduzca un número entero positivo mayor a 2: '))
h = 2
while c % h != 0:
    h += 1
if h == c:
    print(str(c) ,  ' Es primo')
else:
    print(str(c) ,  ' No es primo')

    