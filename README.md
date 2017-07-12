# Códigos en Python para el reconocimiento de rostros y de gestos de las manos usando OpenCV en Raspberry Pi

## Intrucciones

### instalación de OpenCV

#### Primero un update para asegurarnos que todo esté actualizado:
```sudo apt-get update```

#### Luego la libreria OpenCV:
```sudo apt-get install libopencv-dev python-opencv```

#### En caso de algún error:
```sudo apt-get -f install```
<br><br>Y repetimos el comando para la librería

Y listo!
___
###### Comentarios
Al momento de hacer un reconocimiento (ya sea rostro o de gestos) manda señales seriales por medio de bluetooth a otro dispositivo
En caso de que no se necesite se puede omitir o reemplazar esa parte sin ningún inconveniente.

###### Créditos a [Glare](https://robologs.net/2014/04/25/instalar-opencv-en-raspberry-pi-2/) y a [vipul-sharma20](https://github.com/vipul-sharma20/gesture-opencv/blob/master/gesture.py)
