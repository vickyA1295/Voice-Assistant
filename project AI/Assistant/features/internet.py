import pygame
import os
import requests



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



def ipaddress():
    speak("Checking")
    try:
        ipAdd = requests.get('https://api.ipify.org').text
        speak("your ip address is")
        speak(ipAdd)
    except Exception as e:
        speak("network is weak, please try again some time later")