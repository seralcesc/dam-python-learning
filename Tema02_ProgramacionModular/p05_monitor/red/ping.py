import os
import subprocess

def comprobar_host(ip_o_dominio):
    parametro = "-n" if os.name == "nt" else "-c"
    resultado = subprocess.run(["ping", parametro, "1", ip_o_dominio], capture_output=True)
    return resultado.returncode == 0