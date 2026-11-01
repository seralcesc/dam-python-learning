# Ejercicio 10: Ocultador de Datos Sensibles (Enmascaramiento)
# Solicita un número de tarjeta de crédito de 16 dígitos como cadena de texto. El programa debe
# mostrar la tarjeta ocultando los primeros 12 dígitos con asteriscos (*) y mostrando únicamente
# los últimos 4.

tarjeta_credito = input("Introduce tu número de tarjeta de crédito (16 dígitos): ")
if len(tarjeta_credito) == 16 and tarjeta_credito.isdigit():
    tarjeta_oculta = '*' * 12 + tarjeta_credito[-4:]
    print(f"Tu tarjeta de crédito enmascarada es: {tarjeta_oculta}")