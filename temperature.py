import serial
import time
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
ser = serial.Serial('COM7',115200,timeout=1)
time.sleep(2)

def read():
    
    for i in range(600):
        line = ser.readline().decode('utf-8')
        print(line)
        speak(line)
        
        if(int(line[0:2])>30):
            print("Turn on ac")
    