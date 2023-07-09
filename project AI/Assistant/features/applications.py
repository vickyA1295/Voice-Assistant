import os
import pygame
import pywhatkit as kit
import subprocess
import speech_recognition as sr
import pyautogui
from threading import Event


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


def speak(data):
    voice = 'en-GB-SoniaNeural'
    command = f'python -m edge_tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")
        
    try:
        pygame.mixer.music.play()
            
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def youtube():
    speak("what do you want to play")
    query = takecommand().lower()
    speak("playing " + query)
    kit.playonyt(query)
        
def open_V_Box():
    speak("opening virtual box")
    subprocess.Popen(["C:\Program Files\Oracle\VirtualBox\VirtualBox.exe"])

def opentor():
    speak("opening tor browser")
    subprocess.Popen([r"E:\Users\osman\OneDrive\Desktop\Tor Browser\Browser\firefox.exe"])
    
    
def open_vscode():
    speak("opening visual studio code")
    subprocess.Popen([r"E:\Users\osman\AppData\Local\Programs\Microsoft VS Code\Code.exe"])
    
def kali_linux():
    speak("opening kali linux")
    pyautogui.moveTo(57,542,1)
    pyautogui.click(x=57, y=542, clicks=1, interval=0.5, button='right')
    Event().wait(1)
    pyautogui.moveTo(117,159,1)
    pyautogui.click(x=117, y=159, clicks=1, interval=0.5, button='left')
    Event().wait(1)
    pyautogui.moveTo(1234,412,2)
    pyautogui.click(x=1234, y=412, clicks=1, interval=0.5, button='left')
    Event().wait(1)
    pyautogui.moveTo(886,121,1)
    pyautogui.click(x=886, y=121, clicks=1, interval=0.5, button='left')
    
def open_file_explorer():
    speak("opening file explorer")
    subprocess.Popen(["C:\Windows\explorer.exe"])

def openvmware():
    speak("opening vmware")
    subprocess.Popen([r"E:\Program Files (x86)\VMware\VMware Workstation\vmware.exe"])
    
def closeedge():
    speak("closing microsoft edge")
    os.system("taskkill /f /im msedge.exe")
    
def closefirefox():
    speak("closing firefox")
    os.system("taskkill /f /im firefox.exe")
    
def closevmware():
    speak("closing vmware")
    os.system("taskkill /f /im vmware.exe")
       
def close_vscode():
    speak("closing visual studio code")
    os.system("taskkill /f /im Code.exe")
    
def closetor():
    speak("closing tor browser")
    os.system("taskkill /f /im firefox.exe")

def close_V_Box():
    speak("closing virtual box")
    os.system("taskkill /f /im VirtualBox.exe")
    
def closechrome():
    speak("closing chrome")
    os.system("taskkill /f /im chrome.exe")
