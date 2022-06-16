from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
import requests
import json
def speak(str):
    from  win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__ == '__main__':
    speak("News for today")
    url="https://newsdata.io/api/1/news?apikey=pub_8350f21ba8f375b8b42dfcb42e36f6bd14da&q=india&country=in&language=en"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['results']
    for result in arts:
        speak(result["title"])
        print(result["title"])
        speak("moving on to next news")
    speak("thanks for listening")

