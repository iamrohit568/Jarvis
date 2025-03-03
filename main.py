import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibarary
import requests
from openai import OpenAI
import google.generativeai as genai

recognizer = sr.Recognizer()
engine=pyttsx3.init()
genai.configure(api_key="GEMINI_API_KEY")
newsapi="NEWS_API_KEY"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(command)  # Use the right method
        return response.text if response.text else "I couldn't understand that."
    except Exception as e:
        return f"Error: {e}"

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibarary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:  # Check if request was successful
            data = r.json()  # Convert response to JSON
            articles = data.get('articles', []) 

            for article in articles:
                speak(article['title'])

    else:
        #let openai handle this now
        output=aiprocess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis......")

    while True:
        #Listen for wake word jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        

        print("Recognizing...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
            word= r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes sir")

                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active.....")
                    audio = r.listen(source, timeout=2, phrase_time_limit=3)
                    command= r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
