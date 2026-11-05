import shutil


def comprimir_proyecto(nombre_salida, ruta_carpeta):
    archivo_comprimido = shutil.make_archive(
        base_name=nombre_salida, format="zip", root_dir=ruta_carpeta
    )
    return archivo_comprimido
