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
