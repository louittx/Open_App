import tkinter as tk
from tkinter import PhotoImage
import subprocess
import time

def get_windows():
    out = subprocess.check_output(["wmctrl", "-lx"]).decode()
    return set(out.splitlines())

def ProjetRb():
    StartApp1 = ["code","firefox","xterm","jetbrains-studio","nautilus"],["0,0,0,1919,1079","0,739,10,1206,1100","0,0,0,688,485","0,1920,0,1920,1080","0,0,536,817,649"]
    StartApp2 = ["code","jetbrains-studio"],["0,0,0,1919,1079","0,0,0,1920,1080"]
    PwdTerm = "/home/louit/Documents/git/Projet_RB"
    PwdCodeC = "/home/louit/Documents/git/Projet_RB/Code_C++"
    PwdCodeReadme = "/home/louit/Documents/git/Projet_RB/README.md"
    PwdAndroidRb = "/home/louit/Documents/git/Projet_RB/RB_Bluetooth"
    PwdAndroidTest = "/home/louit/Documents/git/Nexu_4wd/App Bluetooth/teste"
    WinIdInit = get_windows() 
    subprocess.Popen(["xterm", "-e", "bash"], cwd=PwdTerm)
    subprocess.Popen(["code",PwdCodeC])
    subprocess.Popen(["snap", "run", "android-studio",PwdAndroidRb])
    subprocess.Popen(["xdg-open", PwdTerm])
    subprocess.Popen(["firefox"])
    time.sleep(10)
    WinIDAfter = get_windows()
    WinID = WinIDAfter-WinIdInit
    for i in range(5):
        time.sleep(1)
        try:
            for line in WinID:
                if StartApp1[0][i] in line.lower():
                    Wid = line.split()[0] # reguper le Wi de la fenetre
                    subprocess.run(["wmctrl", "-ir", Wid, "-b", "remove,maximized_vert"])
                    subprocess.run(["wmctrl", "-ir", Wid, "-b", "remove,maximized_horz"])
                    subprocess.run(["wmctrl", "-ir", Wid, "-b", "remove,fullscreen"])
                    time.sleep(0.5)
                    subprocess.run(["wmctrl", "-ir", Wid, "-t", "0"]) # mais sur la fentre 0
                    subprocess.run(["wmctrl", "-ir", Wid, "-e", StartApp1[1][i]])
                    time.sleep(0.5)
                    subprocess.run(["wmctrl", "-ir", Wid, "-e", StartApp1[1][i]])
                    subprocess.run(["wmctrl", "-ia", Wid])
                    break
        except Exception as e:
            print("Erreur :", e)
        print(i)
    WinIdInit = get_windows()
    subprocess.Popen(["code",PwdCodeReadme])
    subprocess.Popen(["snap", "run", "android-studio",PwdAndroidTest])
    time.sleep(10)
    WinIDAfter = get_windows()
    WinID = WinIDAfter-WinIdInit
    for i in range(2):
        time.sleep(1)
        try:
            for line in WinID:
                if StartApp2[0][i] in line.lower():
                    Wid = line.split()[0] # reguper le Wi de la fenetre
                    subprocess.run(["wmctrl", "-ir", Wid, "-b", "remove,maximized_vert"])
                    subprocess.run(["wmctrl", "-ir", Wid, "-b", "remove,maximized_horz"])
                    subprocess.run(["wmctrl", "-ir", Wid, "-b", "remove,fullscreen"])
                    time.sleep(0.5)
                    subprocess.run(["wmctrl", "-ir", Wid, "-t", "0"]) # mais sur la fentre 0
                    subprocess.run(["wmctrl", "-ir", Wid, "-e", StartApp2[1][i]])
                    time.sleep(0.5)
                    subprocess.run(["wmctrl", "-ir", Wid, "-e", StartApp2[1][i]])
                    subprocess.run(["wmctrl", "-ia", Wid])
                    break
        except Exception as e:
            print("Erreur :", e)
        print(i)





Window = tk.Tk()
Window.title("Start the Projet")
img = PhotoImage(file="/home/louit/Documents/Qt_Application/Icone/IconeRb.png")
Window.geometry("300x200")
Window.config(background='#E0C577')

# Créer un bouton avec image
img_reduite = img.subsample(2, 2)
btn = tk.Button(Window, image=img_reduite, command=ProjetRb)
btn.pack(pady=20)

Window.mainloop()
