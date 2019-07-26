from tkinter import *
import uuid
import tptfetch as tptdf 
import hashlib as hash
import tptfetch as tptdf
import proximaclient as pc


master = Tk()
master.resizable(width=False, height=False)
master.title("Third Party Transaction Login")

directory = 'https://third-party-software.firebaseio.com/'

Label(master, text="Keytag").grid(row=0)
Label(master, text="Username").grid(row=1)
Label(master, text="Password").grid(row=2)

keytag = Entry(master)
username = Entry(master)
password = Entry(master)

keytag.grid(row=0, column=1)
username.grid(row=1, column=1)
password.grid(row=2, column=1)

sendcheck = False

def tpt():
	directory = 'https://third-party-software.firebaseio.com/users'

	def click(key):
		global memory
		if key == 'C':
			entry.delete(0, END) 
		elif key == 'Send':

			sendcheck = True

			if pc.proximarunning == True:

				master = Tk()
				master.title("PROXIMAVERIF")

				Label(master, text="VERIFCODE").grid(row=0)

				verif = Entry(master)

				verif.grid(row=1, column=1)

				if verif.get() == pc.verifcode:
					amountSent = entry.get()
					uuidOfRecipient = recipient.get()
					senderkeytag = keytag.get()

					getrecipientbalance = tptdf.fetch_data(directory + '/' + uuidOfRecipient + '/Balance')
					getsenderbalance = tptdf.fetch_data(directory + '/' + senderkeytag + '/Balance')
					recipientbalance = int(getrecipientbalance)
					senderbalance = int(getsenderbalance)
					intAmountSent = int(amountSent)

					newsenderbalance = senderbalance - intAmountSent
					newrecipientbalance = recipientbalance + intAmountSent

				else:
					print("ACCESS DENIED")

			else:

				amountSent = entry.get()
				uuidOfRecipient = recipient.get()
				senderkeytag = keytag.get()

				getrecipientbalance = tptdf.fetch_data(directory + '/' + uuidOfRecipient + '/Balance')
				getsenderbalance = tptdf.fetch_data(directory + '/' + senderkeytag + '/Balance')
				recipientbalance = int(getrecipientbalance)
				senderbalance = int(getsenderbalance)
				intAmountSent = int(amountSent)

				newsenderbalance = senderbalance - intAmountSent
				newrecipientbalance = recipientbalance + intAmountSent


				if senderbalance < intAmountSent:
					print("Balance: 0")

			tptdf.append_data(directory, '/' + senderkeytag + '/Balance', newsenderbalance)
			tptdf.append_data(directory, '/' + uuidOfRecipient + '/Balance', newrecipientbalance)

            
		else:
			entry.insert(END, key)

	master = Tk()
	master.title("Third Party Transaction Software")
	btn_list = [
	'1',  '2',  '3',  
	'4',  '5',  '6', 
	'7',  '8',  '9', 
	'0',  '.',  'C', 
	'Send']

	r = 2
	c = 0

	for b in btn_list:
		rel = 'ridge'
		cmd = lambda x=b: click(x)
		Button(master,text=b,width=5,relief=rel,command=cmd).grid(row=r,column=c)
		c += 1
		if c > 4:
			c = 0
			r += 1

	entry = Entry(master, width=33, bg="blue")
	entry.grid(row=0, column=0, columnspan=5)
	recipient = Entry(master, width=33, bg="white")
	recipient.grid(row=1, column=0,columnspan=5)

	RECIPIENTUUID = recipient.get()
    
	master.mainloop()


def loginCheck():
	

	firstdirect = 'https://third-party-software.firebaseio.com/users/' + keytag.get()
	print(password.get())
	print(tptdf.fetch_data(firstdirect + '/Password'))
	print(username.get())
	print(tptdf.fetch_data(firstdirect + '/User'))
	print(tptdf.fetch_data(firstdirect))
	
	if str(password.get()) == tptdf.fetch_data(firstdirect + '/Password') and str(username.get()) == tptdf.fetch_data(firstdirect + '/User'):
		print("successs")
		tpt()
	else:
		print("failure")

Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)

Button(master, text = 'Login', command = lambda: loginCheck()).grid(row=5, column=2, sticky=W, pady=4)


mainloop()
