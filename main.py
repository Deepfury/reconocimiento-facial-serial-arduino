import numpy as np
import cv2
import serial, time
#import RPi.GPIO as GPIO

#Setup

#Conexion sudo rfcomm connect 0 00:15:83:35:82:E1

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.OUT)
sr = serial.Serial('/dev/rfcomm0',9600, timeout=3)


#Cargar la plantilla e inicializar la webcam
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while(True):
	#se lee un frame y se guarda
	ret, img = cap.read()
	
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
