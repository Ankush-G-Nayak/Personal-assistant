import pyttsx3  
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

email={"person to send to":"hismail@gmail.com"}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your personal AI chirooon please tell me how may I help you? ")


def takecommand():
    # it takes microphone I/p from user and gives string o/p

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1.5
        r.energy_threshold = 300
        audio = r.listen(source, timeout=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        speak(f"You said: {query}")
    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com','your-password')
    server.sendmail('yourmai@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishme()
    if 1:
        query = takecommand().lower()
        # logic to execute task based on query
        if 'wikipedia' in query:
            speak("search in wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedea")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("open google")
        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")

        elif 'play music' in query:
            music='c:\\Users\\HP\\desktop\\ES'
            songs=os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music, songs[random.randint(0, len(songs) - 1)]))
        elif 'the time' in query:
            Time=datetime.datetime.now().strftime("%H:%M:%S")
            speak((f"the time is{Time}"))
        elif 'open pycharm' in query:
            codepath='"C:\\Users\\HP\\pycharm\\PyCharm Community Edition 2022.2.3\\bin\\pycharm64.exe"'
            os.startfile(codepath)
        elif 'open chrome' in query:
            chrome="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome)
        elif 'send email' in query:
            try:
                speak("To whom should I send the email?")
                to = takecommand().lower()
                if to in email:
                    speak("What should I say?")
                    content = takecommand()
                    sendemail(email[to], content)
                    speak("Email has been sent")
                else:
                    speak("Sorry, I don't have the email address for that person.")
            except Exception as e:
                print(e)
                speak("I apologize for I am unable to send an email")
        elif 'play a movie' in query:
            movie = 'E:\\MOVIES'
            Movie= os.listdir(movie)
            print(Movie)
            os.startfile(os.path.join(movie, Movie[random.randint(0, len(Movie) - 1)]))










