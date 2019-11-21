from random import randint
from tqdm import tqdm

def getHashfunction(num_of_hash_fun, len_of_array):
    return [lambda x: (randint(0,32)*x + randint(0,32)) % len_of_array for _ in tqdm(range(num_of_hash_fun), "Creating {} hash functions".format(num_of_hash_fun))]

def getSignatures(boolean_mat, num_of_hash_fun):
    hash_func_table = getHashfunction(num_of_hash_fun, len(boolean_mat))

    signatures = [[len(boolean_mat)]*(num_of_hash_fun) for _ in range(len(boolean_mat[0]))]

    for index, row in enumerate(boolean_mat):
        for hash_index, hash_func in enumerate(hash_func_table):
            for col_index, column in enumerate(row):
                if column == 1:
                    if hash_func(index)<signatures[col_index][hash_index]:
                        signatures[col_index][hash_index]=hash_func(index)
    return signatures
