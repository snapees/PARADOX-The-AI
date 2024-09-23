import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
# from openai import OpenAI
import google.generativeai as genai
from gtts import gTTS
import pygame
import os

recongizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "8caa8d9bee8f467d806ca16d047effbe"

def speak_old(text):
  engine.say(text)
  engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(10)
      
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
  genai.configure(api_key="AIzaSyCL9bYuCTUK_T4DrgkolILkIb50L51Tx94")
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }
  model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
  )
  chat_session = model.start_chat(history=[])
  response = chat_session.send_message(command)

  return response.text
#   client = OpenAI(api_key="AIzaSyAh4ze8_3uTIF0Tth5apKGp6HcXBHMYuc4",)

#   completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#       {"role": "system", "content": "You are a virtual assistant named paradox skilled in general tasks like Alexa and Google Cloud"},
#       {"role": "user", "content": command}
#     ]
#   )

#   return completion.choices[0].message.content

def processCommand(c):
  if "open google" in c.lower():
    webbrowser.open("https://google.com")
  elif "open facebook" in c.lower():
    webbrowser.open("https://facebook.com")
  elif "open youtube" in c.lower():
    webbrowser.open("https://youtube.com")
  elif "open linkedin" in c.lower():
    webbrowser.open("https://linkedin.com")
  elif c.lower().startswith("play"):
    song = c.lower().split(" ")[1]
    link = musicLibrary.music[song]
    webbrowser.open(link)

  elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

  else:
    # Let Gemini handle the request
    output = aiProcess(c)
    speak(output) 

  

if __name__ == "__main__":
  speak("Initializing Paradox....")
  while True:
    # Listen for the wake word "Paradox"
    # obtain audio from the microphone
    r = sr.Recognizer()
    

    print("Recoginizing...")
# recognize speech using Google Speech Recognition
    try:
      with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, timeout=3, phrase_time_limit=1)
      word = r.recognize_google(audio)
      if (word.lower() == "paradox"):
        speak("Yes Sir! How can i help you?")
        # listen for command
        with sr.Microphone() as source:
          print("Paradox Activated...")
          audio = r.listen(source)
          command = r.recognize_google(audio)

          processCommand(command)
      
    except Exception as e:
      print("Error; {0}".format(e))