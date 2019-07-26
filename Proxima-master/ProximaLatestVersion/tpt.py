from tkinter import *
import DataFetch as df

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

        else:

            amountSent = entry.get()
            uuidOfRecipient = recipient.get()
            senderkeytag = keytag.get()

            getrecipientbalance = df.fetch_data('tpt', directory + '/' + uuidOfRecipient + '/Balance')
            getsenderbalance = df.fetch_data('tpt', directory + '/' + senderkeytag + '/Balance')
            recipientbalance = int(getrecipientbalance)
            senderbalance = int(getsenderbalance)
            intAmountSent = int(amountSent)

            newsenderbalance = senderbalance - intAmountSent
            newrecipientbalance = recipientbalance + intAmountSent

            if senderbalance < intAmountSent:
                print("Balance: 0")

        df.append_data('tpt', directory, '/' + senderkeytag + '/Balance', newsenderbalance)
        df.append_data('tpt', directory, '/' + uuidOfRecipient + '/Balance', newrecipientbalance)

    master = Tk()
    master.title("Third Party Transaction Software")
    btn_list = [
        '1', '2', '3',
        '4', '5', '6',
        '7', '8', '9',
        '0', '.', 'C',
        'Send']

    r = 2
    c = 0

    for b in btn_list:
        rel = 'ridge'
        cmd = lambda x=b: click(x)
        Button(master, text=b, width=5, relief=rel, command=cmd).grid(row=r, column=c)
        c += 1
        if c > 4:
            c = 0
            r += 1

    entry = Entry(master, width=33, bg="blue")
    entry.grid(row=0, column=0, columnspan=5)
    recipient = Entry(master, width=33, bg="white")
    recipient.grid(row=1, column=0, columnspan=5)

    RECIPIENTUUID = recipient.get()

    master.mainloop()


def loginCheck():
    firstdirect = 'https://third-party-software.firebaseio.com/users/' + keytag.get()
    print(password.get())
    print(df.fetch_data('tpt', firstdirect + '/Password'))
    print(username.get())
    print(df.fetch_data('tpt', firstdirect + '/User'))
    print(df.fetch_data('tpt', firstdirect))

    if str(password.get()) == df.fetch_data('tpt', firstdirect + '/Password') and str(username.get()) == df.fetch_data('tpt', firstdirect + '/User'):
        print("successs")
        tpt()
    else:
        print("failed")


Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)

Button(master, text='Login', command=lambda: loginCheck()).grid(row=5, column=2, sticky=W, pady=4)

mainloop()