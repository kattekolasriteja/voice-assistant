import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyqrcode
import qrcode
from pyqrcode import *

listener=aa.Recognizer()  
machine=pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print(".............Teja Assistant...........")
            print("listening..........")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "hey teja" in instruction:
                instruction=instruction.replace('hey teja',"")
                print(instruction)

    except:
        pass
    return instruction


def play_teja():

    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song=instruction.replace('play',"")
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time=datetime.datetime.now().strftime('%I:%M%p')
        print(time)
        talk('Current time'+time)
    elif 'date ' in instruction:
        date=datetime.datetime.now().strftime('%d / %m /%Y')
        print(date)
        talk("Today's date"+date)

    elif 'how are you' in instruction:
        talk("I am fine .how about you")
    elif 'hello' in instruction:
        talk("welcome sir,what can i do for you ")
    elif 'what is you name' in instruction:
        talk('I am teja,what can i do for you')
    elif 'i love you' in instruction:
        talk('i love you to')
    elif 'who is shyam' in instruction:
        talk("'shyam is a unprefessional donkey,born for writting not for studying he's like a buffalo in zoo")
    elif 'who is ' or 'what is' in instruction:
        human=instruction.replace('who is'," ")
        info=wikipedia.summary(human, sentences=3)
        print(info)
        talk(info)
    elif 'qrcode' in instruction:
        site = "file:///C:/SRITEJA/project%20HTML/HTMLPROJECT.HTML"
        url = pyqrcode.create(site)
        url.svg("great.svg", scale=8)
        url.png("great.png", scale=6)

    else:
        talk('please repeat')





play_teja()