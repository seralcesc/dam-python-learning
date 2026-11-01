# Ejercicio 5: Factura de Módulo DAM
# Un comercio de componentes informáticos aplica un IVA del 21% a sus productos. Pide el
# nombre de un artículo y su precio base imponible. Muestra el importe del IVA aplicado y el
# precio final redondeado a dos decimales.

nombre_articulo = input("Introduce el nombre del artículo: ")
precio_base = float(input("Introduce el precio base imponible del artículo: "))
iva = precio_base * 0.21
precio_final = precio_base + iva
print(f"El importe del IVA aplicado es: {iva:.2f} euros")
print(f"El precio final es: {precio_final:.2f} euros")