import keyboard
import psutil
rabota = True 
processi = []
for proc in psutil.process_iter():
    name = proc.name()
    processi.append(name)
while rabota == True:
    if keyboard.is_pressed("f5"):
        rabota = False

    for proc in psutil.process_iter():
        name = proc.name()

        if not name in processi:
            try:
                proc.kill()
            except BaseException:
                pass

