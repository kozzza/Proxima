from firebase import firebase

#define database to use as a link
tptfb = firebase.FirebaseApplication('https://third-party-software.firebaseio.com/')
proxfb = firebase.FirebaseApplication('https://proxima-database.firebaseio.com/')

def append_data(fb, directory, key, value):
    if (fb == 'tpt'):
        db = tptfb
    elif (fb == 'prox'):
        db = proxfb
    #add data to database, specifying directory, and key:value
    append = db.put(directory, key, value)
    return append

def fetch_data(fb, directory):
    if (fb == 'tpt'):
        db = tptfb
    elif (fb == 'prox'):
        db = proxfb
    #grab data from specific directory
    fetch = db.get(directory, None)
    return fetch #Without return value, function returns None which cannot be hashed and leads to many other problems
