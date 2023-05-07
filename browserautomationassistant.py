from time import sleep
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyaudio
import pyautogui
from pyautogui import click
from bs4 import BeautifulSoup as bs
import selenium.common.exceptions
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def insta():
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)

    browser.get('https://www.instagram.com/')



    username_input = browser.find_element("xpath", '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
    password_input = browser.find_element("xpath", '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')

    username_input.send_keys("thevitian")
    password_input.send_keys("D2002FEB")

    login_button = browser.find_element("xpath", '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]')
    login_button.click()

    sleep(5)
    notnow = browser.find_element("xpath", '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
    notnow.click()

    sleep(3)

    browser.get('https://www.instagram.com/thevitian/')
def instasearch(dd):
   
    
    browser = webdriver.Firefox()
              
    browser.get(f'https://www.instagram.com/{dd}/')

    sleep(7)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello I am Kiara Hope you are well how may I help you")
    

       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")   


        
        elif  'song please' in query or 'play some song' in query or 'Koi gana bajao' in query:
            speak("what do you want me to play")
            song=takeCommand()
            webbrowser.open(f'https://open.spotify.com/search/{song}')
            sleep(7)
            pyautogui.click(x=1005,y=385)

            speak("Playing"+song)
        elif  'play some video' in query or 'i wanna watch youtube' in query or 'Mujhe youtube dekhna hai' in query:
            speak("what do you want me to play on youtube")
            video=takeCommand()
            webbrowser.open(f'https://www.youtube.com/results?search_query={video}')
            sleep(7)
            pyautogui.click(x=753,y=330)

            speak("Playing"+video)
        elif  'login to instagram' in query or 'i wanna use instagram' in query or 'Mujhe instagram chalana hai' in query:
              speak("ok enjoy eenstagram")
              insta()
              speak("what do you want me to search on instagram")
              query=takeCommand()
              instasearch(query)
              
        
        
              
        
        