def enviar_alerta(mensaje, canal="SMS"):
    print(f"[{canal}] Alerta: {mensaje}")

def enviar_multicast(usuario1, usuario2, mensaje):
    print(f"Para {usuario1}: {mensaje}")
    print(f"Para {usuario2}: {mensaje}")
    