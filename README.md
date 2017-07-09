# Código en Python para el reconocimiento de rostros usando OpenCV en Raspberry Pi

##Intrucciones

..* ##instalación de OpenCV

Primero un update para asegurarnos que todo esté actualizado:
```sudo apt-get update```

Luego la libreria OpenCV:
```sudo apt-get install libopencv-dev python-opencv```

En caso de algún error:
```sudo apt-get -f install```
Y repetimos el comando para la librería

Y listo!

..*Comentarios
El código está hecho para que cuando encuentre una cara, mande una señal serial por medio de bluetooth
En caso de que no se necesite se puede omitir esa parte sin ningún inconveniente.

######Créditos a [Glare](https://robologs.net/2014/04/25/instalar-opencv-en-raspberry-pi-2/)
