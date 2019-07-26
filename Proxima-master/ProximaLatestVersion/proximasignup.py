from tkinter import *
import uuid
import string as s
import DataFetch as df
from subprocess import call
import RandomDataGenerator as rdg

user_id = str(uuid.uuid4())[:8]
directory = 'https://proxima-database.firebaseio.com/users/'

master = Tk()
master.resizable(width=False, height=False)
master.title("Proxima Signup")

Label(master, text=("User ID",user_id)).grid(row=0)
Label(master, text="Username").grid(row=1)
Label(master, text="Password").grid(row=2)


username = Entry(master)
password = Entry(master)

username.grid(row=1, column=1)
password.grid(row=2, column=1)

def createProfile():
	directory = 'https://proxima-database.firebaseio.com/users/'

	df.append_data('prox', directory, user_id, {'Username' : username.get(), 'Password' : password.get()})

	directory += user_id

	hashedData = rdg.gen_data()

	df.append_data('prox', directory, 'Data Hash', hashedData.hexdigest())

	quit()

def validation():
	print("SKRRT")
	invalidChars = set(s.punctuation.replace("_", ""))
	if (any(char in invalidChars for char in username.get()) or
		any(char in invalidChars for char in password.get())):
		print("Special Characters Not Allowed")
		username.delete(0, 'end')
		password.delete(0, 'end')
	elif (len(password.get()) < 8):
		print("Password is too short!")
		username.delete(0, 'end')
		password.delete(0, 'end')
	else:
		print("Success!")
		createProfile()

	if (True):
		for name in df.fetch_data('prox', directory):
			if (df.fetch_data('prox', directory + name + '/Username').lower() == (username.get()).lower()):
				print("Username Taken!")
				username.delete(0, 'end')


Button(master, text='Quit', command=master.quit).grid(row=7, column=1, sticky=W, pady=4)
Button(master, text = 'Create', command=lambda: validation()).grid(row=7, column=2, sticky=W, pady=4)

mainloop()