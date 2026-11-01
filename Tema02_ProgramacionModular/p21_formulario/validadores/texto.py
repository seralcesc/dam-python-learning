def es_texto_no_vacio(texto):
    texto_sin_espacios = texto.strip()
    if len(texto_sin_espacios) > 0:
        return True
    else:
        return False
