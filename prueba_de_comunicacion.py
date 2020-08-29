import serial
import time

ser = serial.Serial('COM3',9600,timeout=1,write_timeout=1)
# ser=serial.Serial("COM3",9600)
time.sleep(1.9)# open serial port

print(ser.name)
lista=[]
for j in range (1):
    ser.write(b'e\r\n')
    lectura=ser.readlines()
    time.sleep(0.01)
    lista.append(lectura)
    print(lectura)

    # for x in range(4):
    #     ser.write(b'e\r\n')
    #     time.sleep(0.05)
    #     time.sleep(0.05)
    #     lista.append(lectura)
    #     print(lectura)

print("terminado ")
print(lista)
print("Cantidad de datos en la lista: ",len(lista))
ser.close()
