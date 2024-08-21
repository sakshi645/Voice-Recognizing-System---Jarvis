import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib



""" sapi5 is given by microsoft which provide voice it is an inbuilt voice function"""
engine = pyttsx3.init('sapi5')
"""get the property of inbuiltfunc"""
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<20:
        speak("Good Evening! ---")
    else:
        speak("Good night!")
    speak("I am zira how may i help you")
def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        """recognizing the audio using google search engine"""
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
        """if it not recognize what we are saying it come in exception blockand print the statement"""
    except sr.UnknownValueError:
        print("google speech recognizer could find it")
    except sr.RequestError as e:
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('itssakshi645@gmail.com','sakshi7890')
    server.sendEmail('itssakshi645@gmail.com',to,content)
    server.close()
if __name__ == "__main__":
    #speak("proud of you girl")
    wishMe()
    while True:
       query = takeCommand().lower()
       """"logic forexecuting tasks based on query"""
       if 'wikipedia' in query:
           speak('searching wikipedia....')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query,sentences = 2)
           speak("According to wikipedia")
           print(results)
           speak(results)
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
       elif 'open google' in query:
           webbrowser.open("google.com")
       elif 'stack overflow' in query:
           webbrowser.open("stackoverflow.com")
       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir,the time is {strTime}")
       elif 'open code' in query:
           codePath = "C:\\Users\\SAKSHI VERMA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)
       elif 'email to peep' in query:
           try:
               speak("What should i say")
               content = takeCommand()
               to = "itssakshi645@gmail.com"
               sendEmail(to,content)
               speak("Email has been sent!")
           except Exception as e:
               print(e)
               speak("Sorry cannot able  send the email")
       elif 'quit' in query:
           exit()


