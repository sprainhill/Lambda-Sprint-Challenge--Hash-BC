import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random
import string

def ran_gen(size=2, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size)) 

r1 = ran_gen()
r2 = ran_gen()
r3 = ran_gen()

print(f"\nr1 : {r1}\n")
print(f"\nr2 : {r2}\n")
print(f"\nr3 : {r3}\n")

def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print("Searching for next proof")
    proof = ran_gen()
    #  TODO: Your code here
    ## we will take the last_proof p
    ## encode it and hash it
    ## store the hash

    # encode as bytes
    last_proof_encode = f'{last_proof}'.encode()

    last_proof_hashed = hashlib.sha256(last_proof_encode).hexdigest()

    proof_encode = f'{proof}'.encode()

    proof_hashed = hashlib.sha256(proof_encode).hexdigest()

    
    ## take random number p'
    ## hash it
    ## compare the first 6 digits of hashed p'
    ## to the stored last 6 digits of hashed p
    while valid_proof(last_proof_hashed, proof_hashed) is False:
        # generate a different random string and add
        # to the previous proof
        add_ran_str = ran_gen()
        # print(f"proof + add_ran_str : {proof + add_ran_str}")
        proof = proof + add_ran_str

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
    
    ## check the last sux chars of the hash
    ## of proof p against the first
    ## six chars of the hash of our proof p'


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
