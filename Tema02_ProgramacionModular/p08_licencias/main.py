from sistema.argumentos import obtener_clave_desde_cli
from sistema.validacion import es_clave_correcta, cerrar_programa_si_error


if __name__ == "__main__":
    print("=== VALIDACIÓN DE LICENCIA CLI ===")
    clave_cli = obtener_clave_desde_cli()
    print(f"[SISTEMA] Verificando clave '{clave_cli}'...")
    if es_clave_correcta(clave_cli):
        print("Acceso concedido. Licencia activa correctamente.")
    else:
        cerrar_programa_si_error()