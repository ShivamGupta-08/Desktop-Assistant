import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import googletrans
import requests
import json

input_voice = 'en-IN'
email = {
    "your_friend_name": "your_friend_email",
    "your_friend_name": "your_friend_email"
}
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of current voice

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    elif hour >= 18 and hour < 21:
        speak("Good Evening Sir")
    elif hour >= 21 and hour < 0:
        speak("Good Night Sir")
    speak("Sir, I am JARVIS. Please tell me how may I help you!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:

        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email', 'your_passwaord')
    server.sendmail('your_email', to, content)
    server.close


if __name__ == '__main__':
    google_chrome = webbrowser.Chrome(
        r"C:\Users\user\AppData\Local\Google\Chrome SxS\Application\chrome.exe")
    api_key = "api_key"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "your_city"
    complete_url = url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x = response.json()
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query or 'what is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            query = query.replace("what", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            google_chrome.open("youtube.com")
            print(f"Opening YouTube...")
            speak(f"Opening YouTube...")
        elif 'open google' in query:
            google_chrome.open("google.com")
            print(f"Opening Google...")
            speak(f"Opening Google...")
        elif 'open gmail' in query:
            google_chrome.open("mail.google.com")
            print(f"Opening Gmail...")
            speak(f"Opening Gmail...")
        elif 'open hotstar' in query:
            google_chrome.open("www.hotstar.com")
            print(f"Opening Hotstar...")
            speak(f"Opening Hotstar...")

        elif 'open amazon' in query:
            google_chrome.open("www.amazon.in")
            print(f"Opening Amazon...")
            speak(f"Opening Amazon...")

        elif 'open whatsapp' in query:
            google_chrome.open("web.whatsapp.com")
            print(f"Opening Whatsapp...")
            speak(f"Opening Whatsapp...")
        elif 'open classroom' in query:
            google_chrome.open("classroom.google.com")
            print(f"Opening Classroom...")
            speak(f"Opening Classroom...")
        elif 'open optifine' in query:
            google_chrome.open("optifine.net")
            print(f"Opening Optifine...")
            speak(f"Opening Optifine...")
        elif 'play music' in query:
            music_dir = 'F:\\music'
            songs = os.listdir(music_dir)
            ran = random.randint(0, len(songs) - 1)
            for n in range(ran):
                os.startfile(os.path.join(music_dir, songs[n]))
        elif 'time right now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            code_path = "F:\\Microsoft VS Code\\Code.exe"
            print(f"Opening Code...")
            speak(f"Opening Code...")
            os.startfile(code_path)
        elif 'send email' in query or 'send a email' in query:
            for index,names in enumerate(email.keys()):
                print(index+1, names)
            print("Whome you want to send the email...")
            speak("Whome you want to send the email...")
            email_query = takeCommand().lower()

            if email_query in email.keys():
                try:
                    speak("What should I say?")
                    content = takeCommand().capitalize()+"."
                    content
                    to = email.get(email_query)
                    print("Want to send email..")
                    print(f"To: {to}\nContent: {content}")
                    speak("Want to send email..")
                    confirm = takeCommand().lower()
                    if 'yes' in confirm:
                        sendEmail(to, content)
                        print("Email has been sent!")
                        speak("Email has been sent!")
                    elif 'no' in confirm:
                        print("Want to rewrite...")
                        speak("Want to rewrite...")
                        print("Or discard this email...")
                        speak("Or discard this email...")
                        rewrite = takeCommand().lower()
                        if 'rewrite' in rewrite:
                            speak("What should I say?")
                            print("What should I say?")
                            content = takeCommand() + ".".capitalize
                            sendEmail(to, content)
                            print("Email has been sent!")
                            speak("Email has been sent!")
                        elif 'discard' in rewrite:
                            speak("Email discarded!")
                            print("Email discarded!")
                except Exception as e:
                    print(e)
                    speak(
                        "Sorry my friend shivam. I am not able to send this email")
        elif 'the weather' in query:  
            if x["cod"] != "404":

                y = x["main"]

                current_temperature = y["temp"]

                current_pressure = y["pressure"]

                current_humidity = y["humidity"]

                z = x["weather"]

                weather_description = z[0]["description"]

                print(" Temperature (in kelvin unit) = " +
                      str(current_temperature) +
                      "\n atmospheric pressure (in hPa unit) = " +
                      str(current_pressure) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) + "\n weather = " +
                      str(weather_description))
                speak(" Temperature (in kelvin unit) = " +
                      str(current_temperature) +
                      "\n atmospheric pressure (in hPa unit) = " +
                      str(current_pressure) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) + "\n weather = " +
                      str(weather_description))
        elif 'open minecraft' in query:
            code_path = "C:\\Users\\user\\AppData\\Roaming\\.minecraft\\TLauncher-Beta.exe"
            print(f"Opening Minecraft...")
            speak(f"Opening Minecraft...")
            os.startfile(code_path)
        elif 'how are you' in query:
            print("I am fine :-)")
            speak("I am fine :-)")
            
        elif 'quit' in query:
            print("JARVIS is closing....")
            speak("JARVIS is closing....")
            exit()
