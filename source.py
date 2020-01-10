from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# import os
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
import pyttsx3 as pp

eng = pp.init()
voices = eng.getProperty('voices')

eng.setProperty('voice', voices[0].id)

def speak(word):
    eng.say(word)
    eng.runAndWait()

bot = ChatBot('BOOGIE_MAN',storage_adapter='chatterbot.storage.SQLStorageAdapter')
trainer= ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')



# trainer = ListTrainer(bot)
#
# for files in os.listdir('english/'):
#     data = open('english/'+files,'r').readlines()
#     trainer.train(data)

# while True:
#     msg = input('YOU')
#     if msg.strip() != 'Bye' or 'bye':
#         reply= bot.get_response(msg)
#
#     if msg.strip() == 'Bye' or 'bye':


main = Tk()

main.geometry('600x750')

main.title('BOOGIEMAN')
def clicked():
    query = text1.get()
    response = bot.get_response(query)
    msgs.insert(END,'YOU : '+ query)
    msgs.insert(END,'BOOGIEMAN : '+ str(response))
    speak(response)
    text1.delete(0,END)
    msgs.yview(END)

img = PhotoImage(file='bot1.png')

img1 = Label(main,image=img)
img1.pack(pady=5)

frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)

frame.pack()

text1 = Entry(main,font=('ARIAL',20))
text1.pack(fill=X,pady=5)

btn = Button(main,text='ask me',font=('ARIAL',20),command=clicked)
btn.pack()


def enter(event):
    btn.invoke()

main.bind('<Return>', enter)

main.mainloop()

