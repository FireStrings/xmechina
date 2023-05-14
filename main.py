import os
import time

# def postTemperature():
    


    # bot.post("XMechina Bot, on "+str(data)+". Current CPU temperature: " + temp)

print("Recueprando Temperatura...")
temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read().split("=")[1]
data = time.ctime()

print(data)