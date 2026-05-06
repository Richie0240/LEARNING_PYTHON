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
