from perfil import ficha, opciones

if __name__ == "__main__":
    print("=== GESTOR DE FICHAS DE RECURSOS HUMANOS ===")

    nombre = input("Nombre del empleado: ")
    departamento = input("Departamento: ")

    print("--------------------------------------------")

    ficha.mostrar_ficha(nombre, departamento)
    estado = opciones.obtener_estado_usuario()

    print(f"Usuario {nombre} estado: {estado}")
