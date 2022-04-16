import pygame
import os
from glob import glob
import time
import speech_recognition as sr
from random import shuffle
from gtts import gTTS
from io import BytesIO



pygame.init()
pygame.mixer.init()
gameDisplay = pygame.display.set_mode((800, 400))


def speak(text, language='en'):
    ''' convert text to speech via google api without saving the object '''
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    pygame.mixer.music.load(mp3_fo, 'mp3')
    pygame.mixer.music.play()

rec_text = ""
loop = 1
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            rec_text += text
        except:
            speak("Repeat")
            text=''
        if text == "stop":
            loop = 0
               
    gameDisplay.fill((0,0,0))
speak(rec_text)
pygame.quit()