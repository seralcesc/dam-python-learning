# Ejercicio 27: Buscador de Números Primos (Flag) 
# Crea un programa que reciba un número entero mayor que 1 y determine si es primo utilizando 
# un indicador (flag) booleano y un bucle. 



while True:
  numero = int(input("Introduce un número entero mayor que 1 (0 para salir): "))
  if numero == 0:
    break
  if numero == 1:
    print("El número debe ser mayor que 1.")
  else:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
      if numero % i == 0:
        es_primo = False
        break
        
    if es_primo:
      print(f"{numero} es un número primo.")
    else:
      print(f"{numero} no es un número primo.")
            
  