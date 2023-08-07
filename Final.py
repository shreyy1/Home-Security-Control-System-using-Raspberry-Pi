import os
import glob
#import picamera
import RPi.GPIO as GPIO
import smtplib
from time import sleep
import cv2
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
import Adafruit_DHT

sender = 'psshivkumar17@gmail.com'
password = 'jfnixrwyqfbrdobd'
receiver = 'shreyasmachar@gmail.com'

DIR = './Database/'
FILE_PREFIX = 'image'

sensor = Adafruit_DHT.DHT11
PIR = 4
BUZZER = 21
GAS = 3
FIRE = 2
RELAY = 20
pin = 17
LED = 22
LDR = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(GAS, GPIO.IN)
GPIO.setup(LDR, GPIO.IN)
GPIO.setup(FIRE, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(RELAY, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

def beep():
    for i in range(5):
        GPIO.output(BUZZER,1)
        sleep(0.2)
        GPIO.output(BUZZER,0)
        sleep(0.1)
        

def send_text(body):
    print ('Sending E-Mail')
    s,img = cam.read()
    cv2.imwrite('capture.jpg',img)
    filename = 'capture.jpg'
    # Sending mail
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = 'Movement Detected'
    
    #body = 'Picture is Attached.'
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()

def send_mail():
    print ('Sending E-Mail')
    s,img = cam.read()
    cv2.imwrite('capture.jpg',img)
    filename = 'capture.jpg'
    # Sending mail
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = 'Movement Detected'
    
    body = 'Picture is Attached.'
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()

cam = cv2.VideoCapture(0)

def MotionDetect():
    i = GPIO.input(PIR)
    if i == 0:  # When output from motion sensor is LOW
        print ("No intruders", i)
        sleep(0.3)
    elif i == 1:  # When output from motion sensor is HIGH
        print ("Intruder detected", i)
        beep()
        send_mail()
        
def GasDetect():
    i = GPIO.input(GAS)
    if i == 1:  # When output from motion sensor is LOW
        print ("No Gas", i)
        sleep(0.3)
    elif i == 0:  # When output from motion sensor is HIGH
        print ("Gas detected", i)
        beep()
        send_text('Alert ...! Gas Leakage Detected :(')
        
def FireDetect():
    i = GPIO.input(FIRE)
    if i == 1:  # When output from motion sensor is LOW
        print ("No FIRE :)", i)
        GPIO.output(RELAY,1)
        sleep(0.3)
    elif i == 0:  # When output from motion sensor is HIGH
        print ("Fire detected :(", i)
        beep()
        GPIO.output(RELAY,0)
        send_text('Alert ...! FIRE Detected :(')

def getTemp():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
       print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
       print('Failed to get reading. Try again!')
    if temperature > 40:
       print ("Higher Temperature {0}".format(temperature))
       beep()
       send_text('Alert ...! Higher Temperature Detected {0} :('.format(temperature))

def lightDetect():
    i = GPIO.input(LDR)
    if i == 0:  # When output from motion sensor is LOW
        print ("Light detected :)")
        GPIO.output(LED,0)
        #sleep(0.3)
    elif i == 1:  # When output from motion sensor is HIGH
        print ("Night detected :(")
        GPIO.output(LED,1)

while True:
    MotionDetect()
    GasDetect()
    FireDetect()
    getTemp()
    lightDetect()
        


