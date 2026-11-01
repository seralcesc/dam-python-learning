from sorteos import azar, premios

if __name__ == "__main__":
  print("=== TÓMBOLA DIGITAL DE PROMOCIONES ===")
  
  cliente=input("Introduce el nombre del cliente: ")
  print("[SISTEMA] Girando la ruleta de premios...")
  
  categoria = azar.seleccionar_premio_azar("ORO", "PLATA", "BRONCE")
  descuento = premios.calcular_descuento_ganado(categoria)
  
  print(f"¡Enhorabuena {cliente}! Categoría obtenida: {categoria} ({descuento}% de descuento).")