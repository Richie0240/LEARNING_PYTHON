ventas_anuales = [
    1500, 2300, 1800, 2200,
    3000, 2500, 2700, 3200, 2900,
    3100, 2800, 4500]


def calcular_total_ventas(ventas_anuales):
    total_ventas = 0
    for venta in ventas_anuales:
        total_ventas += venta
    promedio_ventas = total_ventas / len(ventas_anuales)
    return total_ventas, promedio_ventas


total, promedio = calcular_total_ventas(ventas_anuales)
print("El total de ventas anuales es:", total)
print("El promedio de ventas mensuales es:", promedio)

# Ejercicio 4: Crear una función que
# calcule el total y el promedio de ventas
# anuales a partir de una lista de ventas mensuales.
