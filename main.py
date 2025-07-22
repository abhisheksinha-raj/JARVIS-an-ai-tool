import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "6b755de06b954bc7b1371698d991db22"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com") 
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com") 
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")     
    elif "open linkdein" in c.lower():  # fix spelling to 'linkedin'
        webbrowser.open("https://linkedin.com")  # fixed typo in URL
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()  # fix 'replaces' → 'replace'
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
    elif "news" in c.lower():
        response = requests.get(f"https://newsapi.org/v2/top-headlines?q=latest&apiKey={newsapi}")  # fixed request and query
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            for article in articles[:5]:  # limit to 5 for brevity
                speak(article['title'])

if __name__ == "__main__":
    speak("Initalizing Jarvis..........")
    while True:
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("yes please")  
                    with sr.Microphone() as source:
                        print("jarvis is active")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        processCommand(command)
        except Exception as e:
            print(f"Error: {e}")  # fixed incorrect format syntax
