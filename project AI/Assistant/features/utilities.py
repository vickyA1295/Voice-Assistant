import pyautogui
import os
import pygame
import speech_recognition as sr
from threading import Event


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


def refresh():
    speak("refreshing screen")
    pyautogui.moveTo(983,446,2)
    pyautogui.click(x=983, y=446, clicks=1, interval=0.5, button='right')
    pyautogui.moveTo(1021,520, 1)
    pyautogui.click(x=1021, y=520, clicks=1, interval=0.5, button='right')
    speak("refreshing completed")
    
def screenpic():
    speak('tell me a name for the file')
    name = takecommand().lower()
    Event().wait(5)
    img = pyautogui.screenshot() 
    img.save(f"E:\screenshots\{name}.png") 
    speak("screenshot saved")
    
def rightcursor():
    pyautogui.moveTo(1710,434,2)
    pyautogui.click(x=1710, y=434, clicks=1, interval=0.5, button='left')
    
def leftcursor():
    pyautogui.moveTo(177,476,2)
    pyautogui.click(x=177, y=476, clicks=1, interval=0.5, button='left')
    
def left():
    pyautogui.hotkey("win","left")

def right():
    pyautogui.hotkey("win","right")
    
def shutdown():
    os.system("shutdown /s /t 1")
    
def restart():
    os.system("shutdown /r /t 1")