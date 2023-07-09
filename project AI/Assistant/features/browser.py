import subprocess
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



def openchrome():
    speak("opening google chrome sir")
    subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe"])
    while True:
        chromequery = takecommand().lower()
        if "maximize this window" in chromequery:
            pyautogui.hotkey("win","up")
        elif "search" in chromequery:
            chromequery1 = chromequery
            chromequery1 = chromequery1.replace("search","")
            pyautogui.write(chromequery1)
            pyautogui.hotkey("enter")
            speak("searching....")
        elif 'open new window' in chromequery:
            speak("opening new window")
            pyautogui.hotkey('ctrl', 'n')
        elif 'open incognito window' in chromequery:
            speak("opening incognito window")
            pyautogui.hotkey('ctrl', 'shift', 'n')
        elif "maximise this window" in chromequery or "maximize this window" in chromequery or "maximize window" in chromequery:
            speak("maximizing this window")
            pyautogui.hotkey("win","up")
        elif "minimise this window" in chromequery or "minimize this window" in chromequery or "minimize window" in chromequery:
            speak("minimizing this window")
            pyautogui.hotkey("win","down")
        elif "chrome in left" in chromequery:
            speak("chrome will be in left side")
            pyautogui.hotkey("win","left")
        elif "chrome in right" in chromequery:
            speak("chrome will be in right side")
            pyautogui.hotkey("win","right")
        elif "open history" in chromequery:
            speak("opening history")
            pyautogui.hotkey("ctrl","h")
        elif 'open downloads' in chromequery:
            speak("opening downloads")
            pyautogui.hotkey('ctrl', 'j')
        elif 'previous tab' in chromequery:
            speak("opening previous tab")
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        elif 'next tab' in chromequery:
            speak("opening next tab")
            pyautogui.hotkey('ctrl', 'tab')
        elif "open new tab" in chromequery or "open youtube" in chromequery or "open yo tab" in chromequery or "in new tab" in chromequery:
            speak("opening new tab")
            pyautogui.hotkey("ctrl","t")
        elif "close tab" in chromequery:
            speak("closing tab")
            pyautogui.hotkey("ctrl","w")
        elif 'close window' in chromequery or "close this window" in chromequery:
            speak("closing this window")
            pyautogui.hotkey('ctrl', 'shift', 'w')
        elif 'clear browsing history' in chromequery:
            speak("clearing browsing history")
            pyautogui.hotkey('ctrl', 'shift', 'delete')
        elif 'soni play' in chromequery or 'sony play' in chromequery:
            chromequery = chromequery.replace("soni play", "")
            chromequery = chromequery.replace("sony play", "")
            speak("playing " + chromequery)
            pyautogui.hotkey('alt', 'd')
            Event().wait(2)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            Event().wait(2)
            pyautogui.write(chromequery)
            pyautogui.press('enter')
            Event().wait(1)
            pyautogui.moveTo(418,453,1)
            pyautogui.click(x=418, y=453, clicks=1, interval=0.5, button='left')  
        elif "pause video" in chromequery:
            speak("pausing video")
            pyautogui.press('space')
        elif "resume video" in chromequery:
            speak("playing video")
            pyautogui.press('space')
        elif "make volume" in chromequery or "volume up" in chromequery or "increase the volume" in chromequery:
            speak("volume high")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")    
        elif "volume low" in chromequery or "decrease the volume" in chromequery:
            speak("volume low")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif "mute" in chromequery:
            pyautogui.press("volumemute")
        elif 'exit chrome' in chromequery or 'close chrome' in chromequery:
            speak("leaveing chrome")
            break

def openfirefox():
    speak("opening firefox sir")
    subprocess.Popen([r"C:\Program Files\WindowsApps\Mozilla.Firefox_109.0.1.0_x64__n80bbvh6b1yt2\VFS\ProgramFiles\Firefox Package Root\firefox.exe"])
    pyautogui.moveTo()
    while True:
        foxquery = takecommand().lower()
        if "maximize this window" in foxquery:
            pyautogui.hotkey("win","up")
        elif "search" in foxquery:
            foxquery1 = foxquery
            foxquery1 = foxquery1.replace("search","")
            pyautogui.write(foxquery1)
            pyautogui.hotkey("enter")
            speak("searching....")
        elif 'open new window' in foxquery:
            speak("opening new window")
            pyautogui.hotkey('ctrl', 'n')
        elif 'open incognito window' in foxquery:
            speak("opening incognito window")
            pyautogui.hotkey('ctrl', 'shift', 'n')
        elif "maximise this window" in foxquery or "maximize this window" in foxquery or "maximize window" in foxquery:
            speak("maximizing this window")
            pyautogui.hotkey("win","up")
        elif "minimise this window" in foxquery or "minimize this window" in foxquery or "minimize window" in foxquery:
            speak("minimizing this window")
            pyautogui.hotkey("win","down")
        elif "firefox in left" in foxquery:
            speak("firefox will be in left side")
            pyautogui.hotkey("win","left")
        elif "firefox in right" in foxquery:
            speak("firefox will be in right side")
            pyautogui.hotkey("win","right")
        elif "open history" in foxquery:
            speak("opening history")
            pyautogui.hotkey("ctrl","h")
        elif 'open downloads' in foxquery:
            speak("opening downloads")
            pyautogui.hotkey('ctrl', 'j')
        elif 'previous tab' in foxquery:
            speak("opening previous tab")
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        elif 'next tab' in foxquery:
            speak("opening next tab")
            pyautogui.hotkey('ctrl', 'tab')
        elif "open new tab" in foxquery or "open youtube" in foxquery or "open yo tab" in foxquery or "in new tab" in foxquery:
            speak("opening new tab")
            pyautogui.hotkey("ctrl","t")
        elif "close tab" in foxquery:
            speak("closing tab")
            pyautogui.hotkey("ctrl","w")
        elif 'close window' in foxquery or "close this window" in foxquery:
            speak("closing this window")
            pyautogui.hotkey('ctrl', 'shift', 'w')
        elif 'clear browsing history' in foxquery:
            speak("clearing browsing history")
            pyautogui.hotkey('ctrl', 'shift', 'delete')
        elif 'soni play' in foxquery or 'sony play' in foxquery:
            foxquery = foxquery.replace("soni play", "")
            foxquery = foxquery.replace("sony play", "")
            speak("playing " + foxquery)
            pyautogui.hotkey('alt', 'd')
            Event().wait(2)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            Event().wait(2)
            pyautogui.write(foxquery)
            pyautogui.press('enter')
            Event().wait(1)
            pyautogui.moveTo(418,453,1)
            pyautogui.click(x=418, y=453, clicks=1, interval=0.5, button='left')
        elif "pause video" in foxquery:
            speak("pausing video")
            pyautogui.press('space')
        elif "resume video" in foxquery:
            speak("playing video")
            pyautogui.press('space')
        elif "make volume" in foxquery or "volume up" in foxquery or "increase the volume" in foxquery:
            speak("volume high")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")    
        elif "volume low" in foxquery or "decrease the volume" in foxquery:
            speak("volume low")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif "mute" in foxquery:
            pyautogui.press("volumemute")
        elif 'exit firefox' in foxquery or 'close firefox' in foxquery:
            speak("leaveing firefox")
            break

def openedge():
    speak("opening microsoft edge sir")
    subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"])
    while True:
        edgequery = takecommand().lower()
        if "maximize this window" in edgequery:
            pyautogui.hotkey("win","up")
        elif "search" in edgequery:
            chromequery1 = edgequery
            chromequery1 = chromequery1.replace("search","")
            pyautogui.write(chromequery1)
            pyautogui.hotkey("enter")
            speak("searching....")
        elif 'open new window' in edgequery:
            speak("opening new window")
            pyautogui.hotkey('ctrl', 'n')
        elif 'open incognito window' in edgequery:
            speak("opening incognito window")
            pyautogui.hotkey('ctrl', 'shift', 'n')
        elif "maximise this window" in edgequery or "maximize this window" in edgequery or "maximize window" in edgequery:
            speak("maximizing this window")
            pyautogui.hotkey("win","up")
        elif "minimise this window" in edgequery or "minimize this window" in edgequery or "minimize window" in edgequery:
            speak("minimizing this window")
            pyautogui.hotkey("win","down")
        elif "edge in left" in edgequery:
            speak("edge will be in left side")
            pyautogui.hotkey("win","left")
        elif "edge in right" in edgequery:
            speak("edge will be in right side")
            pyautogui.hotkey("win","right")
        elif "open history" in edgequery:
            speak("opening history")
            pyautogui.hotkey("ctrl","h")
        elif 'open downloads' in edgequery:
            speak("opening downloads")
            pyautogui.hotkey('ctrl', 'j')
        elif 'previous tab' in edgequery:
            speak("opening previous tab")
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        elif 'next tab' in edgequery:
            speak("opening next tab")
            pyautogui.hotkey('ctrl', 'tab')
        elif "open new tab" in edgequery or "open youtube" in edgequery or "open yo tab" in edgequery or "in new tab" in edgequery:
            speak("opening new tab")
            pyautogui.hotkey("ctrl","t")
        elif "close tab" in edgequery:
            speak("closing tab")
            pyautogui.hotkey("ctrl","w")
        elif 'close window' in edgequery or "close this window" in edgequery:
            speak("closing this window")
            pyautogui.hotkey('ctrl', 'shift', 'w')
        elif 'clear browsing history' in edgequery:
            speak("clearing browsing history")
            pyautogui.hotkey('ctrl', 'shift', 'delete')
        elif 'soni play' in edgequery or 'sony play' in edgequery:
            edgequery = edgequery.replace("soni play", "")
            edgequery = edgequery.replace("sony play", "")
            speak("playing " + edgequery)
            pyautogui.hotkey('alt', 'd')
            Event().wait(2)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            Event().wait(2)
            pyautogui.write(edgequery)
            pyautogui.press('enter')
            Event().wait(1)
            pyautogui.moveTo(418,453,1)
            pyautogui.click(x=418, y=453, clicks=1, interval=0.5, button='left')
        elif 'play one more' in edgequery or 'play one more' in edgequery:
            edgequery = edgequery.replace("play one more", "")
            edgequery = edgequery.replace("play one more", "")
            speak("playing " + edgequery)
            pyautogui.hotkey('alt', 'd')
            Event().wait(2)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            Event().wait(2)
            pyautogui.write(edgequery)
            pyautogui.press('enter')
            Event().wait(1)
            pyautogui.moveTo(418,453,1)
            pyautogui.click(x=418, y=453, clicks=1, interval=0.5, button='left')
        elif "pause video" in edgequery:
            pyautogui.press('space')
            speak("pausing video")
        elif "resume video" in edgequery:
            speak("playing video")
            pyautogui.press('space')
        elif "make volume" in edgequery or "volume up" in edgequery or "increase the volume" in edgequery:
            speak("volume high")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")    
        elif "volume low" in edgequery or "decrease the volume" in edgequery:
            speak("volume low")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif "mute" in edgequery:
            pyautogui.press("volumemute")
        elif 'exit edge' in edgequery or 'edge chrome' in edgequery:
            speak("leaveing microsoft edge")
            break
        
