#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # add data to ht
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)
    
    # set departure by querying
    # by None key
    route[0] = hash_table_retrieve(hashtable, "NONE")

    # now we use the ith - 1
    # to find desination that links
    # to departure point
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i - 1])

    return route
