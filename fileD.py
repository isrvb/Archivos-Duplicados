import os

archivos1 = os.listdir("ruta")
archivos2 = os.listdir("ruta")

rutacarpeta1 = ("ruta")
rutacarpeta2 = ("ruta")

for i in archivos1:
	for a in archivos2:
		if i==a:
			print("Se repiten los archivos: ",a,i)
			os.chdir(rutacarpeta 1-2) #Escoger cual carpeta
			os.remove(a)
