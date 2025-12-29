ventas_enero = float(input("Ingrese las ventas del mes de enero: "))
ventas_febrero = float(input("Ingrese las ventas del mes de febrero: "))
ventas_marzo = float(input("Ingrese las ventas del mes de marzo: "))
total_trimestre = ventas_enero + ventas_febrero + ventas_marzo
promedio_mensual = total_trimestre / 3

if promedio_mensual >= 10000:
    print("Mes de ventas bueno")
else:
    print("Mes de ventas malo")

# Ejercicio 2: Condicionales
# En este ejercicio, solicitamos al usuario que ingrese las ventas
# de una tienda durante los primeros tres meses del año.
# Calculamos el total de ventas del trimestre y el promedio mensual.
# Luego, utilizamos una estructura condicional para evaluar si el
# promedio mensual es mayor a 1000, mostrando un mensaje
# correspondiente según el resultado de la evaluación.
