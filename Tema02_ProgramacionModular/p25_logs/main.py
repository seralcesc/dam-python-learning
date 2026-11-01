from auditor import os_info, trazabilidad

if __name__ == "__main__":
    print("=== AUDITORÍA DEL SISTEMA ===")
    print("[SISTEMA] Consultando núcleo del sistema operativo...")
    plataforma = os_info.obtener_nombre_so()
    print(f"[SISTEMA] Plataforma detectada: {plataforma}")
    trazabilidad.imprimir_linea_separadora()
