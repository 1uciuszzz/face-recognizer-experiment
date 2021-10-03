import cv2
import serial

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')

def handle(c):
    serialPort = "COM4"
    baudRate = 115200
    ser = serial.Serial(serialPort, baudRate,timeout=0.5)
    lightOn = b"0"
    lightOff = b"1"
    alarmOn = b"2"
    alarmOff = b"3"
    while True:
        c = ord(c)
        if c == 48:
            ser.write(lightOn)
            break
        if c == 49:
            ser.write(lightOff)
            break
        if c == 50:
            ser.write(alarmOn)
            break
        if c == 51:
            ser.write(alarmOff)
            break

cascade_path = "haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
cam = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x - 50, y - 50), (x + w + 50, y + h + 50), (225, 0, 0), 2)
        img_id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        if conf < 50:
            handle('0')
            handle('3')
            if img_id == 0:
                img_id = 'user1'
        else:
            img_id = "Unknown"
            handle('1')
            handle('2')
        cv2.putText(im, str(img_id), (x, y), font, 1, (0, 255, 0), 1)
        cv2.imshow('im', im)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows() 

