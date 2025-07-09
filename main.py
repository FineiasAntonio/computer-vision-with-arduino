import time
import cv2
import serial
from cvzone.HandTrackingModule import HandDetector

conectado = False
portaArduino = 'COM3'
velocidadeBaud = 115200

try:
    SerialArduino = serial.Serial(portaArduino, velocidadeBaud)
    time.sleep(2)
    conectado = True
    print("Conexão com o Arduino na porta COM3 estabelecida com sucesso!")

except serial.SerialException as e:
    print(f"Erro ao conectar na porta {portaArduino}: {e}")
    conectado = False
video = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7)

while True:
    check, img = video.read()
    if not check:
        break  

    hands, img = detector.findHands(img)
    
    if hands:
        fingers = detector.fingersUp(hands[0])
        
        if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1:
            print("Sinal detectado")
            SerialArduino.write('SINAL_ROCK\n'.encode())
            time.sleep(2)

        if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            print("Mão fechada detectada")
            SerialArduino.write('MAO_FECHADA\n'.encode())
            time.sleep(2)

    cv2.imshow('Controle por Mão', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
if conectado:
    SerialArduino.close()