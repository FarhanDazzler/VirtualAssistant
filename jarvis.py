import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib  

 

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')

engine.say("Hello I am Jarvis, your virtual assistant...sir!")
engine.runAndWait()

def speak(audio):
    print("speaking...")
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good Morning Sir") 
    elif hour>=12 and hour <18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening")    

def takeCommand():
                #it take microphone input and convert it in string

    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")         
    except Exception as e:
       # print(e)
        print("Say that again please...")
        return "none"  
    return query 

if __name__ == "__main__":
   # speak("farhan dazzler is a good boy")
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            query=query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak("According to wikipedia...")
            speak(results)

        elif 'stop' in query:
            quit()   

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")    

        elif 'play music' in query:
            music_dir = "C:\\Users\\Farhan Dazzler\\Music\\music_dir"
            songs=os.listdir(music_dir)
            print("playing this song" +"song")
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'open code' in query:
            codePath='C:\\Users\\Farhan Dazzler\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\code.exe' 
            os.startfile(codePath)   

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir , the time is {strTime}")    

        elif 'email' in query:
                to ='xxxx@gmail.com'   
                fromSender="xxxxxxx@gmail.com"
                msg='hello this is test mail'
                try:        
                    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
                    smtpObj.ehlo()
                    smtpObj.starttls()
                    smtpObj.login('xxxxxxxx@xxxxxxxx.com','xxxxxxxx')
                    smtpObj.sendmail(fromSender, to, msg)  

                    smtpObj.close()    
                    print ("Successfully sent email")
                except Exception as e:
                    print(e)
                    print ("Error: unable to send email")            

            
