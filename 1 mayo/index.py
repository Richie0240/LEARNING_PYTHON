# ejercicios de practica

# faciles

# 1 par o impar

numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("El numero: ", numero, " es par")
else:
    print("El numero: ", numero, " es impar")


# 2. Contador de vocales

# Pide una palabra y cuenta cuántas vocales tiene.

# Ejemplo:

# Ingrese una palabra: murcielago
# Tiene 5 vocales


palabra = input("Ingrese una palabra y te dire cuantas vocales tiene: ")
cantidad = 0

for letra in palabra:
    if letra in "aeiou":
        cantidad += 1

if cantidad > 1:
    print("la palabra : ", palabra, " tiene ", cantidad, " vocales")
elif cantidad == 1:
    print("la palabra : ", palabra, " tiene ", cantidad, " vocal")
else:
    print("la palabra : ", palabra, " no tiene vocales")

# 3. Tabla de multiplicar

# Pide un número y muestra su tabla del 1 al 10.

# Ejemplo:

# 5 x 1 = 5
# 5 x 2 = 10
# ...

numeroTabla = int(input("ingrese un numero del 0 al 10: "))

for i in range(1, 11):
    resultado = numeroTabla * i
    print(numeroTabla, " x ", i, " = ", resultado)
