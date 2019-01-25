# Importing the required libraries
from pynput.keyboard import Key, Controller
import sys
import time
import speech_recognition as sr
import string
# Record Audio
r = sr.Recognizer()

def numfy(word):
    one = "one"
    two = "two"
    three = "three"
    four = "four"
    five = "five"
    six = "six"
    if one in word:
        return 1
    elif two in word:
        return 2
    elif three in word:
        return 3
    elif four in word:
        return 4
    elif five in word:
        return 5
    elif six in word: 
        return 6
    else:
        return 7

keyboard = Controller()
# Collect events until released

with sr.Microphone() as source:
    audio = r.listen(source)
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    said = r.recognize_google(audio)
    waitTime = numfy(said)
    print(waitTime)
    while(True):
     time.sleep(waitTime)
     keyboard.press(Key.down)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


