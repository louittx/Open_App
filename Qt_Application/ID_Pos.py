import subprocess
import time

def get_windows():
    out = subprocess.check_output(["wmctrl", "-lx"]).decode() # visulise tout les fentre
    return set(out.splitlines())

WinIdInit = get_windows() 
#print(WinIdInit)
try:
    for line in WinIdInit:
        print(line.lower())
        Wid = line.split()[0] # reguper le Wi de la fenetre
        out = subprocess.check_output(["xdotool", "getwindowgeometry", Wid]).decode()
        print(out)
except Exception as e:
    print("Erreur :", e)