def es_archivo_temporal(nombre):
  if nombre.endswith(".tmp") or nombre.endswith(".bak"):
    return True
  else:
    return False