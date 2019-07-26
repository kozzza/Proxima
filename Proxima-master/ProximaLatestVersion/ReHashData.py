import hashlib as hash
import DataFetch as df

def rehash_Data(userid):
    directory = 'https://proxima-database.firebaseio.com/users/' + userid + '/'

    dataToReHash = df.fetch_data('prox', directory + 'Data Hash')

    print(dataToReHash)

    bytesToReHash = dataToReHash.encode('UTF-8')

    ReHashedData = hash.sha256(bytesToReHash)

    df.append_data('prox', directory, 'Data Hash', ReHashedData.hexdigest())