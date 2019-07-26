import uuid
import hashlib as hash

def gen_data():
    randomdata = uuid.uuid4().hex

    for i in range(10):
        randomdata += uuid.uuid4().hex
        i += 1

    bytesToHash = randomdata.encode('UTF-8')

    hashedData = hash.sha256(bytesToHash)

    return hashedData


