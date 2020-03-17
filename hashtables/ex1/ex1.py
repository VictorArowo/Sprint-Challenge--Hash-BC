#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    if length < 2:
        return None

    for i, num in enumerate(weights):
        difference = limit - num
        if hash_table_retrieve(ht, difference) is not None:
            if hash_table_retrieve(ht, difference) > i:
                return [hash_table_retrieve(ht, difference), i]
            return [i, hash_table_retrieve(ht, difference)]
        else:
            hash_table_insert(ht, num, i)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
