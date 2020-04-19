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
    for value in range(length):
        weight = weights[value]
        hash_table_insert(ht, weight, value)

    for i in range(length):
        weight = weights[i]
        weight_limit = limit - weight
        if hash_table_retrieve(ht, weight_limit):
            return [hash_table_retrieve(ht, weight_limit), i]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
