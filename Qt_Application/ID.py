import subprocess
import time
import os

def get_windows():
    out = subprocess.check_output(["wmctrl", "-lx"]).decode() # visulise tout les fentre
    return set(out.splitlines())

res = subprocess.check_output("xdpyinfo | grep dimensions", shell=True).decode()
print(res)  # ex: dimensions:    1920x1080 pixels
WinIdInit = get_windows() 
subprocess.Popen(["firefox"])
time.sleep(5)
WinIDAfter = get_windows()
WinID = WinIDAfter-WinIdInit # premt d'avoir que les ID des nouvelle page
#print(WinIdInit)
try:
    for line in WinID:
        if "firefox" in line.lower():
            Wid = line.split()[0] # reguper le Wi de la fenetre
            out = subprocess.check_output(["xdotool", "getwindowgeometry", Wid]).decode()
            print(out)
            subprocess.run(["wmctrl", "-ir", Wid, "-b", "remove,maximized_vert"])
            subprocess.run(["wmctrl", "-ir", Wid, "-b", "remove,maximized_horz"])
            subprocess.run(["wmctrl", "-ir", Wid, "-b", "remove,fullscreen"])
            time.sleep(0.3)
            subprocess.run(["wmctrl", "-ir", Wid, "-t", "0"]) # mais sur la fentre 0
            subprocess.run(["wmctrl", "-ir", Wid, "-e", "0,980,12,967,564"])
            subprocess.run(["wmctrl", "-ia", Wid])
            break
except Exception as e:
    print("Erreur :", e)