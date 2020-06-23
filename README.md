# Automation-with-speech-to-text
I use speech to text and text to speech Api's in python to execute common commands on a PC. Some limitations are that it is sometimes slow, especially when opening a program, it can only open programs that have already been given a predefined name (as it can be hard to guess the  name of every launch file), and that it searches your computer for the file launch path when opening a program as supposed to other methods. Also one needs the API's installed for the program to work, the packages I installed were as follows.

pyttsx3   (text to speech)                                        https://pypi.org/project/pyttsx3/
psutil    (Allows easier monitoring of system processes)          https://pypi.org/project/psutil/
SpeechRecogntion  (Speech to Text)                                https://pypi.org/project/SpeechRecognition/
