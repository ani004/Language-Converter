#!/usr/bin/env python
# coding: utf-8

# In[42]:


def get_key(language,lan):
    #print(lan)
    for key, value in language.items():
        if value==lan:
            return key



import pyttsx3
import speech_recognition as sr         #for speech to text translation
from googletrans import Translator      #help google translate API to take input one language and change into another
from gtts import gTTS                   #for text to speech conversion and play the audio
import os
import googletrans
from langdetect import detect
from textblob import TextBlob 

engine=pyttsx3.init('sapi5')     #for recognize voice using inbuild voice of windows
inbuild_voice=engine.getProperty('voices')
#print(inbuild_voice[1].id)
engine.setProperty('voice',inbuild_voice[1].id)

def voice(audio):
    engine.say(audio)
    engine.runAndWait()
    
language={}
language=googletrans.LANGUAGES

rec1=sr.Recognizer()
rec2=sr.Recognizer()
rec3=sr.Recognizer()
MC=sr.Microphone(device_index=None)

with MC as source:
    print("Speak HI to initiate translation and please say something for testing: ")
    voice("Speak HI to initiate translation and please say something for testing: ")
    audio=rec1.listen(source)    #for listening to the microphone, stops executing when it hear nothing
    rec1.pause_threshold=1
    print("It is working!!!!!....")
if 'hi' in rec1.recognize_google(audio):     #for converting our speech into text
    rec1=sr.Recognizer()
    trans=Translator()
    print("Please Enter the sentence: ")
    voice("Please Enter sentence ")
    with MC as source:
        audio1=rec2.listen(source)
        speak_lan1=rec2.recognize_google(audio1)
        print(speak_lan1)
        x=TextBlob(speak_lan1)
        from_lan=(x.detect_language())
        lan=language.get(from_lan)
        #print(lan)
    print("Please say the language you want to hear: ")
    voice("Please say the language you want to hear")
    with MC as source1:
        audio2=rec3.listen(source1)
        hear_lang1=rec3.recognize_google(audio2)
        print(hear_lang1)
        if hear_lang1=="bangla" or hear_lang1=="bengali" or hear_lang1=="Bengali" or hear_lang1=="Bangla":
            hear_lang1=hear_lang1.lower()
            hear_lan1="bengali"
        elif hear_lang1=="hindi" or hear_lang1=="Hindi":
            hear_lang1=hear_lang1.lower()
            hear_lan1="hindi"    
        else:    
            x=TextBlob(hear_lang1)
            final_lan=(x.detect_language())
            #print(f"last language{final_lan}")
            hear_lan1 = trans.translate(hear_lang1, src = final_lan, dest = "en")
            hear_lan1 = hear_lan1.text
            #print(hear_lan1)
        #print(hear_lan1)
        hear_lan=hear_lan1.lower()
        to_lan=get_key(language,hear_lan)
        
        try:
            #sentence=rec2.recognize_google(audio)
            sentence=speak_lan1
            text_translatation1 = trans.translate(sentence, src = from_lan, dest = from_lan)
            text1 = text_translatation1.text 
            print("--------------------------------------")
            print("Main Given sentence:")
            print("--------------------------------------")
            print("The sentence is: "+text1)
            print("Detected Language: "+lan)
            text_translatation = trans.translate(sentence, src = from_lan, dest = to_lan)  #for translating
            text = text_translatation.text       #translated text value
            Ret_audio = gTTS(text=text, lang = to_lan, slow = False)  #text to speech conversion use slow for the speed
            Ret_audio.save("translated_voice.mp3")    #for saving video
            os.system("start translated_voice.mp3")   #two argument for starting audio
            os.startfile("translated_voice.mp3")
            print("--------------------------------------")
            print("Translated Voice:")
            print("--------------------------------------")
            print(text)
            print("Language: "+hear_lan1)
        except sr.UnknownValueError:
            print("Unable to understand the input")
        except sr.RequestError as e:
            print("Unable to provide required output".format(e))     #to handle error
        


# In[23]:


get_ipython().system('pip install textblob')


# In[27]:


from textblob import TextBlob 
x="My name is anish"
lang = TextBlob(x)
print(lang.detect_language())


# In[24]:


language.get("no")


# In[ ]:




