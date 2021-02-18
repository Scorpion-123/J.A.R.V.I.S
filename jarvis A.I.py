import pyttsx3
import datetime
import platform
import re
import speech_recognition as sr
import os
from win10toast import ToastNotifier
from time import sleep
# this is used for opening different applications inside the computer
import subprocess

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.getProperty("rate")
engine.setProperty("rate", 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 6 and hour < 12:
        speak("good morning boss !")
    elif hour > 12 and hour < 18:
        speak("good afternoon boss !")
    elif hour > 18 and hour < 21:
        speak("goof evening boss !")
    elif hour > 23 and hour < 4:
        speak("good night boss! ")
    speak("my name is jarvis !! how may i help you. ")
    speak("my speed is 1 terabyte and i am an extremely fast AI with a processing speed of 0.0012 milliseconds ")


def selfinformation():
    s = platform.processor()
    m = platform.architecture()
    a = platform.platform()
    speak(f"the software is running on {m[0]}")
    pattern = re.compile("[A-Za-z]+\-+[0-9]")
    result = pattern.findall(a)
    speak(f"the computer system is currently running on {result[0]} operating system")
    speak(f"the integrated processor that is used here is {s}")


def date():
    date = datetime.datetime.date(datetime.datetime.now())
    speak(f"today's date is {date}")


def time():
    time = str(datetime.datetime.now().time())
    b = time.split(":")
    speak(f"the current time is {b[0]} hours and {b[1]}minutes")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        print("say that again please")
        return "None"
    return query


def shutdown():
    os.system("shutdown /s /t 30")


def notification():
    toaster = ToastNotifier()
    toaster.show_toast("Notification!", "hi boss how are you", threaded=True, icon_path=None, duration=5)


# this is used for opening notepad
def notepad():
    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')


# this is used for opening paint using command
def paint():
    subprocess.Pope('C:\\Windows\\System32\\mspaint.exe')

if __name__ == '__main__':
	 wishme()
	 while True:
	 	command=take_command()
	 	if "open notepad" in command:
	 		speak("Opening notepad boss")
	 		notepad()
	 	elif "open paint" in command:
	 		speak("opening paint")
	 		paint()
	 	elif "shutdown" in command:
	 		speak("The computer will shutdown in 1sec boss")
	 		shutdown()
	 	elif "date" in command:
	 		date()
	 	elif "time" in command:
	 		time()
	 	elif "selfinformation" in command:
	 		selfinformation()
# You can continue adding on functionality to your J.A.R.V.I.S assistent.