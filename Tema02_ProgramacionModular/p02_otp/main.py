import seguridad.aleatorio as aleatorio
import seguridad.expiracion as expiracion

if __name__ == "__main__":
    input("Presiona [ENTER] para solicitar un código SMS...")
    codigo = aleatorio.generar_codigo_numerico()
    hora_expiracion = expiracion.obtener_hora_expiracion(5)
    print(f"Tu código de verificación es: {codigo}")
    print(f"Atención: Este código caducará a las {hora_expiracion} (Válido durante 5 minutos).")