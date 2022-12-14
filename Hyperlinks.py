import tkinter
import PIL
import json 
from tkinter import *
import webbrowser
from tkHyperlinkManager import HyperlinkManager
from functools import partial
from PIL import  Image, ImageTk

#-----------------------------

def callback(url):
   webbrowser.open_new_tab(url)


#--------------------------

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    
    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, ' \n')

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, 'You: ' + msg + '  \n\n', 'userText')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        
    
        res = chatbot_response(msg)
        #--------------------

        resSt = str(res)
        if(resSt.startswith('https:')):
            ChatLog.insert(END, "Bot: You should check the university website ")
            hyperlink = HyperlinkManager(ChatLog)
            ChatLog.insert(END, "this link \n\n", hyperlink.add(partial(webbrowser.open, resSt)))

        elif(resSt.startswith('Hello:')):
            wordList = resSt.split();
            resSt = wordList[-1];
            ChatLog.insert(END, "Bot: Hello, welcome to the university chatbot ")
           
        elif(resSt.startswith('Courses:')):
            wordList = resSt.split();
            resSt = wordList[-1];
            ChatLog.insert(END, "Bot: You can check all department's lecture schedule ")
            hyperlink = HyperlinkManager(ChatLog)
            ChatLog.insert(END, "in here :) \n\n", hyperlink.add(partial(webbrowser.open, resSt)))
        elif(resSt.startswith('Payment:')):
            wordList = resSt.split();
            resSt = wordList[-1];
            ChatLog.insert(END, "Bot: You can call the default university number (+14563747) or check website ")
            hyperlink = HyperlinkManager(ChatLog)
            ChatLog.insert(END, "check the website. \n\n", hyperlink.add(partial(webbrowser.open, resSt)))
        elif(resSt.startswith('Price:')):
            wordList = resSt.split();
            resSt = wordList[-1];
            ChatLog.insert (END, "Bot: You can see all department's price policy at this website")
            hyperlink = HyperlinkManager(ChatLog)
            ChatLog.insert(END, "table. \n\n", hyperlink.add(partial(webbrowser.open, resSt)))
        elif(resSt.startswith('intake:')):
            wordList = resSt.split();
            resSt = wordList[-1];
            ChatLog.insert(END, "Bot: You can check the current intakes in the following website ")
            hyperlink = HyperlinkManager(ChatLog)
            ChatLog.insert(END, "list! \n\n", hyperlink.add(partial(webbrowser.open, resSt)))
        else:
            ChatLog.insert(END, "Bot: " + res + '\n\n')    
        
            

        #-----------------------
 
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
 

base = Tk()
base.title(" University ChatBot")
base.geometry("500x600")
base.resizable(width=FALSE, height=FALSE)


ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial", wrap=WORD)

ChatLog.config(state=DISABLED)
ChatLog.tag_config('userText', foreground="green", justify=RIGHT)


image = ImageTk.PhotoImage(Image.open('C:\\Users\\Mert\\Desktop\\ChatBot\\images\\UUlogo.png'))
label1 = tkinter.Label(base, image=image)
label2 = tkinter.Label(base, text=" University ChatBot")
label1.pack()
label2.pack()


scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set


SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )


EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial", wrap=WORD)




scrollbar.place(x=476,y=6, height=386)
ChatLog.place(x=0,y=115, height=380, width=470)
EntryBox.place(x=128, y=501, height=90, width=342)
SendButton.place(x=6, y=501, height=90)


base.mainloop()