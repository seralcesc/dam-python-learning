from mensajeria import envio, formato

if __name__ == "__main__":
    print("=== SISTEMA DE NOTIFICACIONES MULTICANAL ===")
    
    mensaje=input("Introduce el mensaje de alerta a enviar: ")
    
    formato.imprimir_cabecera_urgente()
    
    envio.enviar_alerta(mensaje)
    print("-----------------------------")
    envio.enviar_multicast("User1", "User2", mensaje)