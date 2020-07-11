#!/usr/bin/env python
# coding: utf-8


# In[6]:


def get_key(language,lan):
    #print(lan)
    for key, value in language.items():
        if value==lan:
            return key
        



import speech_recognition as sr         #for speech to text translation
from googletrans import Translator      #help google translate API to take input one language and change into another
from gtts import gTTS                   #for text to speech conversion and play the audio
import os
import googletrans

#dictinary for all laguanges in Google API
language={}
language=googletrans.LANGUAGES

# create recognizer class object
rec1=sr.Recognizer()
rec2=sr.Recognizer()

#create microphone class
MC=sr.Microphone(device_index=None)  #default one will be used

#voice capture
with MC as source:
    print("Speak HI to initiate translation and please say something for testing: ")
    audio=rec1.listen(source)    #for listening to the microphone, stops executing when it hear nothing
    print("It is working!!!!!....")
    
#translate into another language
if 'hi' in rec1.recognize_google(audio):     #for converting our speech into text
    rec1=sr.Recognizer()
    trans=Translator()                       #for translation purpose
    speak_lan1=input("Please Enter the language you want to speak: ")
    speak_lan=speak_lan1.lower()
    from_lan=get_key(language,speak_lan)
    print(from_lan)
    hear_lan1=input("Please Enter the language you want to hear: ")
    hear_lan=hear_lan1.lower()
    to_lan=get_key(language,hear_lan)
    print(to_lan)
    with MC as source:
        print("Now Tell a sentence....")
        audio=rec2.listen(source)
        try:
            sentence=rec2.recognize_google(audio)
            text_translatation1 = trans.translate(sentence, src = from_lan, dest = from_lan)
            text1 = text_translatation1.text 
            print("The sentence is: "+text1)
            text_translatation = trans.translate(sentence, src = from_lan, dest = to_lan)  #for translating
            text = text_translatation.text       #translated text value
            Ret_audio = gTTS(text=text, lang = to_lan, slow = False)  #text to speech conversion use slow for the speed
            Ret_audio.save("translated_voice.mp3")    #for saving video
            os.system("start translated_voice.mp3")   #two argument for starting audio
            print(text)
        except sr.UnknownValueError:
            print("Unable to understand the input")
        except sr.RequestError as e:
            print("Unable to provide required output".format(e))     #to handle error    


# In[ ]:




