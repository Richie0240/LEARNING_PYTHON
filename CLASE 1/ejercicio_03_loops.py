ventas_mensuales = [
    1500, 2300, 1800, 2200,
    3000, 2500, 2700, 3200, 2900,
    3100, 2800, 3500
]

total_ventas = 0

for venta in ventas_mensuales:
    total_ventas += venta
    print("Venta del mes:", venta)
    print("Total acumulado:", total_ventas)
    print("-" * 40)

print("Total de ventas anuales:", total_ventas)
# Ejercicio 3: Calcular el total de ventas
# anuales a partir de una lista de ventas mensuales.
