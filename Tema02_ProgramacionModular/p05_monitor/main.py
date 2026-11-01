from red import auditoria, ping

if __name__ == "__main__":
    host = input("Introduce el dominio o servidor a comprobar: ")
    print(f"[SISTEMA] Ejecutando diagnóstico de red sobre '{host}'...")
    
    if ping.comprobar_host(host):
        latencia = auditoria.medir_latencia_simulada()
        print(f"Resultado: Servidor ONLINE (Respuesta en {latencia} ms).")
    else:
        print("Resultado: Servidor OFFLINE (No hay respuesta).")