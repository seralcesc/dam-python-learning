from algoritmos import base, proceso

if __name__ == "__main__":
    print("=== CONTROL RECURSIVO DE EMPAQUETADO ===")
    unidades = int(input("Unidades totales del lote a procesar: "))
    unidades_restantes = unidades

    for i in range(unidades, 0, -1):
        mensaje = proceso.imprimir_unidad_procesada(i)
        print(mensaje)
        unidades_restantes -= 1

    if base.es_lote_completado(unidades_restantes):
        print("Estado: Lote Finalizado.")
