def calcular_dano_net(ataque, defensa):
    if ataque <= defensa:
      return 1
    else:
      return ataque-defensa