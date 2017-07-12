import cv2
import numpy as np
import math
import serial, time

#setup
#Conexion serial por bluetooth
sr = serial.Serial('/dev/rfcomm0',9600, timeout=3)
#Conexion sudo rfcomm connect 0 00:15:83:35:82:E1

#crear el objeto de videocaptura
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    # leer la imagen
    ret, img = cap.read()
	
	#obtener el gesto de las manos desde el rectangulo en la pantalla
    cv2.rectangle(img, (300,300), (100,100), (0,255,0),0)
    crop_img = img[100:300, 100:300]

	#convertir la imagen a escala de grises
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
	
	#aplicando desenfoque gaussiano
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
	
	
    # Umbral: metodo de binarizacion de Otsu
    _, thresh1 = cv2.threshold(blurred, 127, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # muestra la imagen del umbral
    cv2.imshow('Thresholded', thresh1)

    contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
		cv2.CHAIN_APPROX_NONE)

    # Encontrar un contorno con el area maxima
    cnt = max(contours, key = lambda x: cv2.contourArea(x))

    # crear un rectangulo para delimitar el contorno
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(crop_img, (x, y), (x+w, y+h), (0, 0, 255), 0)

    # encontrar el convexHull
    hull = cv2.convexHull(cnt)

    # Dibujando contornos
    drawing = np.zeros(crop_img.shape,np.uint8)
    cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 0)
    cv2.drawContours(drawing, [hull], 0,(0, 0, 255), 0)

    # encontrando el convexHull
    hull = cv2.convexHull(cnt, returnPoints=False)

    # encontrando defectos convexos
    defects = cv2.convexityDefects(cnt, hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (0, 255, 0), 3)

	#Aplicar la regla del coseno para encontrar todos los defectos entre los dedos
	#con angulo > 90 grados e ignorar defectos
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]

        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
		
		# encontrar la longitud de todos los lados del triangulo
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

        # aqui aplica la regla del coseno
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
		
		#ignorar los angulos > 90 y mostrar el resto con puntos rojos
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_img, far, 1, [0,0,255], -1)

        cv2.line(crop_img,start, end, [0,255,0], 2)

	#acciones
    if count_defects == 1:
        cv2.putText(img,"2 Dedo AVAN", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        sr.write('a')
    elif count_defects == 2:
        cv2.putText(img,"3 Dedos IZQ", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        sr.write('i')
    elif count_defects == 3:
        cv2.putText(img,"4 Dedos DER", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        sr.write('d')
    elif count_defects == 4:
        cv2.putText(img,"5 dedos RET", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        sr.write('r')
    else:
        cv2.putText(img,"Haz algun gesto!", (50, 50),\
                    cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

	# mostrar imagenes en las ventanas
    cv2.imshow('Gesture', img)
    all_img = np.hstack((drawing, crop_img))
    cv2.imshow('Contours', all_img)

    k = cv2.waitKey(10)
    if k == 27:
        break
