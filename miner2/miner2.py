import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random
import string

def ran_gen(size=1, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size)) 

r1 = ran_gen()
r2 = ran_gen()
r3 = ran_gen()

print(f"\nr1 : {r1}\n")
print(f"\nr2 : {r2}\n")
print(f"\nr3 : {r3}\n")

def proof_of_work(last_proof):
    """
    find a number proof such that the hash of 
    proof + last_proof (from the server)
    contain the correct dif
    """

    start = timer()

    print("Searching for next proof")
    proof = random.random() 
    ## take random number p'
    
    ## hash it
  
    while valid_proof(last_proof, proof) is False:
        # generate a different random string and add
        # to the previous proof
        # add_ran_str = ran_gen()
        # print(f"proof + add_ran_str : {proof + add_ran_str}")
        add_ran_num = random.random()
        proof += add_ran_num
        # new_proof = proof + add_ran_str
        # proof = new_proof
        

    # if valid_proof evaluates as true
    # return that proof as our p'

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """

    # TODO: Your code here!
    
    ## we will take the last_proof p
    ## encode it and hash it
    ## store the hash

    # encode as bytes
    last_proof_encode = f'{last_hash}'.encode()

    last_proof_hashed = hashlib.sha256(last_proof_encode).hexdigest()

    proof_encode = f'{proof}'.encode()

    proof_hashed = hashlib.sha256(proof_encode).hexdigest()

    ## check the last six chars of the hash
    ## of proof p against the first
    ## six chars of the hash of our proof p'
    last_hash_chars = last_proof_hashed[-6:]

    hash_chars = proof_hashed[:6]

    return last_hash_chars == hash_chars


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
