#Functions for Voice commands and imported API's

import speech_recognition as speechRec
import pyttsx3
import subprocess
import psutil
import os
import win32gui, win32con

engine = pyttsx3.init()
rec = speechRec.Recognizer()


#Searches throrugh all windows if one matches the name said it Maximizes that
#window
def MaximizeWindow(hwnd, name):
    if (win32gui.IsWindowVisible(hwnd) and (name in win32gui.GetWindowText(hwnd).lower())):
        engine.say("Maximizing" + name)
        engine.runAndWait()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(hwnd)

#Minimizes the current window
def MinimizeWindow():
    engine.say("minimizing window")
    Minimize = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

#Searches Google for whatever you say
def SearchGoogle(source):
    engine.say("What would you like to search")
    engine.runAndWait()
    audio = rec.listen(source)
    text = rec.recognize_google(audio).lower()
    subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\\chrome.exe', 'https://www.google.com/search?source=hp&ei=I937XKCIAuOl_Qag76p4&q=' + text + '&oq=yeet&gs_l=psy-ab.12..35i39j0i131j0l8.7857.8292..8512...2.0..0.85.340.5......0....1..gws-wiz.....6.xj-DQggIRlc'])

#Opens the program of the specified name, this only works with predefined
#names in the GetProgramName functions as it is hard to know the exact name
#of each programs launch file
def OpenProgram(programName):
    program = GetProgramName(programName)
    if (program != "Error"):
        engine.say("opening" + programName)
        engine.runAndWait()
        path = FindProgram(program)
        subprocess.Popen([path])

#Closes the specified program if it is currently open
def KillProgram(programName):
    program = GetProgramName(programName)
    if (program !='Error'):
        engine.say("closing" + programName)
        engine.runAndWait()
        for proc in psutil.process_iter():
            try:
                # Get process name & pid from process object.
                if proc.name() == program:
                    proc.terminate()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass


#Helper function for Open Program, returns the exact name of the launch file
def GetProgramName(programName):
    if (programName == "chrome" or programName == "google"):
        return "chrome.exe"
    elif (programName == "unity"):
        return "Unity.exe"
    elif (programName == "steam"):
        return "Steam.exe"
    elif (programName == "discord"):
        return "Discord.exe"
    else:
        engine.say(programName + "could not be found")
        engine.runAndWait()
        return "Error"

#Helper function for Open Program, searches computer for the launch file path
def FindProgram(program):
    directory = r'C:\\'
    if (program != "Discord.exe"):
        directory = r'C:\Program Files (x86)'
    else:
        directory = r'C:\Users\nickg'
    for r,d,f in os.walk(directory):
        for files in f:
            if files == program:
                print
                path = (os.path.join(r,files))
                return path
