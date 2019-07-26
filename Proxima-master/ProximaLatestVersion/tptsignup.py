from tkinter import *
import uuid
import DataFetch as df

keytag = str(uuid.uuid4())[:8]

master = Tk()
master.resizable(width=False, height=False)
master.title("Third Party Transaction Signup")

directory = 'https://third-party-software.firebaseio.com/users'

Label(master, text=("Keytag:",keytag)).grid(row=0)
Label(master, text="Username").grid(row=1)
Label(master, text="Password").grid(row=2)
Label(master, text="Balance").grid(row=3)


username = Entry(master)
password = Entry(master)
balance = Entry(master)

username.grid(row=1, column=1)
password.grid(row=2, column=1)
balance.grid(row=3, column=1)

def createDirectorydos():

	df.append_data('tpt', directory, keytag, {'User' : username.get(), 'Password' : password.get(), 'Balance' : balance.get()})


Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)
Button(master, text = 'Create', command = lambda: createDirectorydos()).grid(row=5, column=2, sticky=W, pady=4)

mainloop()