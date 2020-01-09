# get last proof from server

# run through valid proof function t
# to get a valid proof

# submit it to the mining endpoint

import random
import hashlib

def proof_of_work(last_proof, n):
    print("Searching for next proof")
    proof = random.random() 

    while valid_proof(last_proof, proof, n) is False:
        # add ran num to proof
        proof += 1
    print("Proof found: " + str(proof) + " bishes")
    return proof


def valid_proof(last_proof, proof, n):
    """
    Validates the Proof:  does valid_proof(last_proof, proof, n)
    contain n leading zeroes (given in last_proof as dif lvl)
    """
    ## we will take the last_proof
    ## and hash it with random numbers
    ## until last_proof + proof hashed has
    ## the amount of leading zeroes

    ## encode it and hash it
    ## store the hash
    # encode as byte
    proof_encode = f'{last_proof}{proof}'.encode()
    proof_hashed = hashlib.sha256(proof_encode).hexdigest()

    ## check that the hash has the correct
    ## leading amt of zeroes
    nonce = proof_hashed[:n]

    if nonce == "0" * n:
        print("hash found : ", proof)
        # return proof_hashed

    return nonce == "0" * n


p1 = 4772069499598679
n1 = 6

t1 = proof_of_work(p1, n1)