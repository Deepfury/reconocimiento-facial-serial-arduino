#Libreria para hacer calculos matriciales complejos
import numpy as np
#Libreria opencv
import cv2
#libreria para hacer communicacion serial en python pySerial
import serial, time
#import RPi.GPIO as GPIO

#Setup

#Conexion sudo rfcomm connect 0 00:15:83:35:82:E1

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.OUT)

#se crea el objeto de para la conexion con el modulo de bluetooth HC-06
sr = serial.Serial('/dev/rfcomm0',9600, timeout=3)


#Cargar la plantilla 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#inicializa la webcam para capturar los frames
cap = cv2.VideoCapture(0)

while(True):
	#se lee un frame y se guarda
	ret, img = cap.read()
	
	#Sino hay imagen vuelve al inicio del ciclo a leer otra vez
	if img is None:
		continue
	
	#convertir la imagen a blanco y negro
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	
	#Buscamos coordenadas de los rostros y guardamos la posicion
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	
	if len(faces) > 0:
		#GPIO.output(17, 1)
		sr.write('a')
		print ("Hay Cara")
	else:
		#GPIO.output(17, 0)
		sr.write('r')
		print ("No hay cara")
	
	
	#dibujamos un rectangulo en las coordenadas de cada rostro
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
		
	#mostramos la imagen 	
	cv2.imshow('img', img)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
