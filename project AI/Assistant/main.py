import datetime
from threading import Event
import pyttsx3
import sys
import os
import operator
import pyautogui
import speech_recognition as sr

from features.customvoice import speak
from features.browser import *
from features.utilities import *
from features.calcy import *
from features.internet import *
from features.applications import *

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
voicespeed = 140
engine.setProperty('rate',voicespeed)

            
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
     print("Recognizing....")
     query = r.recognize_google(audio, language='en-us')
     print(f"user said: {query}\n")
    except Exception as e:
      print(e)
      return "None"
    return query

def wakeupcommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("soni is sleeping....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    try:
     query = r.recognize_google(audio, language='en-us')
     print(f"user said: {query}\n")
    except Exception as e:
      print(e)
      return "None"
    return query
    
def myself():
    speak('My Name Is soni')
    speak('I can Do Everything that my creator programmed me to do')
    

def time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    speak(time)
    print(time)
 
def wishme():
    speak("Welcome back sir")
    
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak('Good morning')
    elif hour>=12 and hour<=18:
        speak('Good afternoon')
    elif hour>=18 and hour<=24:
        speak('Good evening')
    else:
        speak('Good night')
        
    speak('How can i help you today')
    

"""    
def open_start_menu ():
    speak("opening start menu")
    pyautogui.moveTo(223,1056,1)
    pyautogui.click(x=223, y=1056, clicks=1, interval=0.5, button='left')
    Event().wait(1)
    speak("what do you wish to open")
    query = takecommand().lower()
    pyautogui.write(query)
    speak("opening " + query)
    Event().wait(1)
    pyautogui.moveTo(745,473,1)
    pyautogui.hotkey("enter")
"""

           
def stop_execution():
    sys.exit()
    
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        print(query)
        if "good morning" in query:
            speak("good morning sir")
        elif "good afternoon" in query:
            speak("good afternoon sir")
        elif "good evening" in query:
            speak("good evening sir")
        elif "time" in query:
            time()
        elif "go to sleep" in query:
            speak("i am going to hybernation sir")
            break
        elif "relax" in query:
            speak("ok sir,i am switching off and giving control to you")
            stop_execution()
        elif "shutdown" in query:
            speak("system is shutting down")
            shutdown()
        elif "restart" in query:
            speak("system is now restarting")
            restart()
        #chrome automation commands
        elif "open chrome" in query:
            openchrome()
        elif "close chrome" in query:
            closechrome()
        #firefox automation commands
        elif "open firefox" in query:
            openfirefox()
        elif "close firefox" in query:
            closefirefox()
        #edge automation commands
        elif "open edge" in query:
            openedge()
        elif "close edge" in query:
            closeedge()
        elif "make volume" in query or "volume up" in query or "increase the volume" in query:
            speak("volume high")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")    
        elif "volume low" in query or "decrease the volume" in query:
            speak("volume low")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif "mute" in query:
            pyautogui.press("volumemute")
        elif "calculate" in query:
            calculate()
        elif "open virtualbox" in query:
            open_V_Box()
        elif "open virtual box" in query:
            open_V_Box()
        elif "close virtual box" in query:
            close_V_Box()
        elif "take screenshot" in query or "take a screenshot" in query:
            screenpic()
        elif "who are you" in query:
            myself()
        elif "what is your name" in query:
            myself()
        elif "open web" in query:
            opentor()
        elif "close web" in query:
            closetor()
        elif "hey soni" in query:
            speak("yes boss, how can i help you")
        elif "open vs code" in query:
            open_vscode()
        elif "close vs code" in query:
            close_vscode()
        elif "refresh" in query:
            refresh()
        elif "what is my ip address" in query:
            ipaddress()
        elif 'open youtube' in query:
            youtube()
        elif "open linux" in query:
            kali_linux()
        elif "open files" in query or "open file explorer" in query:
            open_file_explorer()
        elif "open vmware" in query:
            openvmware()
        elif "close vmware" in query:
            closevmware()
        elif "move right" in query:
            rightcursor()
        elif "move left" in query:
            leftcursor()
        elif "left side" in query:
            left()
        elif "right side" in query:
            right()