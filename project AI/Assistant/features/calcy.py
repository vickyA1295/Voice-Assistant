import pygame
import os
import speech_recognition as sr
import operator


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

def calculate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("calculating")
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        my_string=r.recognize_google(audio)
        print(my_string)

        def get_operator_fn(op):
            return {
                '+' : operator.add,
                '-' : operator.sub,
                'multiplied' : operator.mul,
                '*' : operator.mul,
                'x' : operator.mul,
                'X' : operator.mul,
                '/' : operator.__truediv__,
            }[op]
        try:    
            def eval_bianary_expr(op1,oper, op2):
                op1,op2 = float(op1), float(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_bianary_expr(*(my_string.split())))
        except Exception as e:
            print(e)
            speak("unable to process")
            return None
    except Exception as e:
        print(e)
        return None