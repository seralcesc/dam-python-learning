from combate import dado, dano

if __name__ == "__main__":
    print("=== COMBATE POR TURNOS RPG ===")
    ataque=(int(input("Puntos de ataque del personaje: ")))
    defensa=(int(input("Puntos de defensa del monstruo: ")))
    
    tirada=dado.lanzar_dado_20()
    print(f"[SISTEMA] Tirando el dado de impacto d20... ¡Obtenido: {tirada}!")
    
    danio_neto=dano.calcular_dano_net(ataque, defensa)
    print(f"Daño neto inflingido al objetivo: {danio_neto} PV")