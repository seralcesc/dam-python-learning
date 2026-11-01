def aplicar_rebaja_temporada(precio, porcentaje=30):
    precio_final = precio - (precio * porcentaje / 100)
    return precio_final
