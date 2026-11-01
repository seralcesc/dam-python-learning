import os
import zipfile

def crear_copia_zip(nombre_zip, carpeta_origen):
    if not os.path.exists(carpeta_origen):
        return False

    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        for root, dirs, files in os.walk(carpeta_origen):
            for filename in files:
                file_path = os.path.join(root, filename)
                zipf.write(file_path, os.path.relpath(file_path, carpeta_origen))

    return True
