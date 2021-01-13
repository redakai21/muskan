import pyttsx3

import datetime

import speech_recognition as sr

import audioop

import wikipedia

import webbrowser

import os





engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

 

#print(voices[1])

engine.setProperty('voices',voices[1].id)

def speak(audio):

    engine.say(audio)

    engine.runAndWait()

 

def wishMe():

    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <12:

        speak("good morning")

    elif hour >=12 and hour<18:

        speak("good afternoon")

    else:

        speak("good evening")

 

    speak("hello  i am muskan ,please tell me how may i help you")

    

 

def takecommand():

    #it takes microphone input from the user and gives string output

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("listening...")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print("recognising...")

        query = r.recognize_google(audio,language="en-in")

        print(f"user said: {query}\n")

 

    except Exception as e:

        print(e)

        print("say that again please...")

        return'None'

    return query

        

 

if __name__ ==  "__main__":

    wishMe()

    #while True:

    if 1:

        query = takecommand().lower()

        

 

        #logic for executing tasks based on query

         

        if "wikipedia" in query :

            speak("Searching wikipedia...")

            query = query.replace("wikipedia","")

            results = wikipedia.summary(query,sentences=2)

            speak("according to wikipedia")

            print(results)

            speak(results)

 

        elif "open youtube" in query:

            webbrowser.open("youtube.com")

            

        elif "open google" in query:

            webbrowser.open("google.com")

            

        elif "open stackoverflow" in query:

            webbrowser.open("stackoverflow.com")

 

        elif "the time" in query:    

            strTime=datetime.datetime.now().strftime("%H:%M:%S")

            print(strTime)

            speak(f"sir the time is {strTime}")


#to get this working do the following things 
#1 install pyaudio externally
#2 pip install wikipedia
#3 pip install pyttsx3
#4 pip install speechrecognition