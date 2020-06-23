import voiceCommands

def Main():
     wantToSpeak = True

     with voiceCommands.speechRec.Microphone() as source:
          while wantToSpeak:
               try:
                    #Lets user know it is ready (mainly if the inital attempt
                    #does not work the user can wait until this is printed to
                    #try again)
                    print('Ready')
                    
                    audio = voiceCommands.rec.listen(source)
                    text = voiceCommands.rec.recognize_google(audio).lower()
                    textList = text.split()

                    #Closes program so unlike the FBI it stops listening
                    if (text == "close yourself"):
                         voiceCommands.engine.say("closing self")
                         wantToSpeak = False

                    #Closes a program if it is a currently open
                    elif (textList[0] == "computer" and textList[1] == "close"):
                         voiceCommands.KillProgram(textList[2])

                    elif (text == "computer search google"):
                         voiceCommands.SearchGoogle(source)

                    #Opens a a program if has a predefined name
                    elif (textList[0] == "computer" and textList[1] == "open"):
                         voiceCommands.OpenProgram(textList[2])

                    #Minimizes current window
                    elif (text == "computer minimize window"):
                         voiceCommands.MinimizeWindow()
                         
                    #Maximizes a window if it is open
                    elif (textList[0] == "computer" and textList[1] == "maximize"):
                         voiceCommands.win32gui.EnumWindows(voiceCommands.MaximizeWindow, textList[2])

               except:
                    pass
               
               voiceCommands.engine.runAndWait()

if __name__ == "__main__":
     Main()
