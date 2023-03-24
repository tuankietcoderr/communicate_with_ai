import speech_recognition as sr
import pyttsx3
from openai_key import OPENAI_KEY
import openai
openai.api_key = OPENAI_KEY
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
# set speed for engine

def talk(text):
    engine.say(text)
    engine.runAndWait()
def response(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=100,
        # temparature=0,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0,
        # stop=["\n", " Human:", " AI:"]
    )
    return response["choices"][0]["text"]
def take_command():
    str_result = ""
    while(1):
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                print("Me: " + command)
                if 'stop' in command:
                    break
                response_text = response(command)
                print("AI: " + response_text)
                talk(response_text)
                
        except:
            str_result = "I can't hear you clearly, please try again"
            print(str_result)
            pass
    

take_command()