import time
import serial

sr = serial.Serial('/dev/rfcomm0',9600, timeout=1)
print(sr.isOpen())

print 'Conectado'

sr.write('a')

print 'Enviado a'

sr.close()
