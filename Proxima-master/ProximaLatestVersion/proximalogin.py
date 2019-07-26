from tkinter import *
import DataFetch as df

user_id = "2277c6c1"

directory = 'https://proxima-database.firebaseio.com/users/' + user_id

master = Tk()
master.resizable(width=False, height=False)
master.title("Proxima Login")

Label(master, text="Username").grid(row=1)
Label(master, text="Password").grid(row=2)

username = Entry(master)
password = Entry(master)

username.grid(row=1, column=1)
password.grid(row=2, column=1)

def loginCheck():
    if (username.get() == df.fetch_data('prox', directory + "/Username") and password.get() == df.fetch_data('prox', directory + "/Password")):
        #subject to change with making user and pass read from hardware when user creates account
        print("Success!")
        quit()  #run some function
    else:
        print("Incorrect Login")
        quit()

Button(master, text='Quit', command=master.quit).grid(row=7, column=1, sticky=W, pady=4)
Button(master, text = 'Login', command=lambda: loginCheck()).grid(row=7, column=2, sticky=W, pady=4)

mainloop()