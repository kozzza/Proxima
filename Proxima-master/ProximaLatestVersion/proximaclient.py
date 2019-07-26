from tkinter import *
import random as rand
import DataFetch as df
import tpt
from twilio.rest import Client

master = Tk()
master.resizable(width=False, height=False)
master.title("Proxima Login")

directory = 'https://proxima-database.firebaseio.com/'

Label(master, text="Keytag").grid(row=0)
Label(master, text="Username").grid(row=1)
Label(master, text="Password").grid(row=2)

keytag = Entry(master)
username = Entry(master)
password = Entry(master)

keytag.grid(row=0, column=1)
username.grid(row=1, column=1)
password.grid(row=2, column=1)

phonecheck = False

def addphone():
    master.tk()
    master.title("Add Phone")

    Label(master, text="Number").grid(row=0)
    number = Entry(master)
    number.grid(row=0, column=1)

    Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)

    Button(master, text='Add', command=lambda: addNumber()).grid(row=5, column=2, sticky=W, pady=4)

    def addNumber():
        global phonenumber
        phonenumber = number.get()
        global sendcheck
        sendcheck = True

    master.mainloop()


def proxima():
    verifcode = ''

    for digit in range(6):
        verifcode += str(rand.randint(0, 10))
        digit += 1
    master = Tk()

    master.title("Proxima Client")

    proximarunning = True

    Label(master, text="Proxima is running...").grid(row=0)
    Button(master, text='Add Phone', command=master.quit).grid(row=2, column=1, sticky=W, pady=4)

    if sendcheck == True:
        Label(master, text=verifcode).grid(row=1)

    if phonecheck == True:
        client = Client('*******************', '********************')
        client.messages.create(to="+1"+str(phonenumber), from_="+**********",body=verifcode)

    master.mainloop()

    if proximarunning == True:

        master = Tk()
        master.title("PROXIMAVERIF")

        Label(master, text="VERIFCODE").grid(row=0)

        verif = Entry(master)

        verif.grid(row=1, column=1)

        if verif.get() == verifcode:
            amountSent = tpt.entry.get()
            uuidOfRecipient = tpt.recipient.get()
            senderkeytag = tpt.keytag.get()

            getrecipientbalance = df.fetch_data('tpt', directory + '/' + uuidOfRecipient + '/Balance')
            getsenderbalance = df.fetch_data('tpt', directory + '/' + senderkeytag + '/Balance')
            recipientbalance = int(getrecipientbalance)
            senderbalance = int(getsenderbalance)
            intAmountSent = int(amountSent)

            newsenderbalance = senderbalance - intAmountSent
            newrecipientbalance = recipientbalance + intAmountSent

        else:
            print("ACCESS DENIED")


def loginCheck():

    seconddirect = 'https://proxima-database.firebaseio.com/users/' + keytag.get()

    if str(password.get()) == df.fetch_data('prox', seconddirect + '/Password') and str(username.get()) == df.fetch_data('prox', seconddirect + '/Username'):
        proxima()
    else:
        print("you failed")

Button(master, text='Quit', command = master.quit).grid(row=5, column=1, sticky=W, pady=4)

Button(master, text = 'Login', command = lambda: loginCheck()).grid(row=5, column=2, sticky=W, pady=4)

master.mainloop()