#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    ## loop over weights and
    ## add them to a hash table
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i )

    ## loop over again for comp
    # we check for limit - weight as a key 
    # in the hash table

    for i in range(len(weights)):
        # get diff
        diff = limit - weights[i]
        # check for key
        if hash_table_retrieve(ht, diff):
            idx = hash_table_retrieve(ht, diff)
            return (idx, i)



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
