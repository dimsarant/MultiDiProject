from functools import reduce
from hashlib import md5
from tqdm import tqdm
from random import randint
from pprint import pprint

def getSignatures(boolean_mat, num_of_hash_fun):
    hash_func_table = getHashfunction(num_of_hash_fun, len(boolean_mat))

    signatures = [[len(boolean_mat)]*num_of_hash_fun for _ in range(len(boolean_mat[0]))]

    for index, row in enumerate(boolean_mat):
        for hash_index, hash_func in enumerate(hash_func_table):
            for col_index, column in enumerate(row):
                if column == 1:
                    if hash_func(index)<signatures[col_index][hash_index] or signatures[col_index][hash_index] is None:
                        signatures[col_index][hash_index]=hash_func(index)
    return signatures

def getHashfunction(num_of_hash_fun, len_of_array):
    return [lambda x: (randint(0,32)*x + randint(0,32)) % len_of_array for _ in tqdm(range(num_of_hash_fun), "Creating {} hash functions".format(len_of_array))]

def getSinglingMatrix(text_list):
    universe = set()
    for text in tqdm(text_list, "Creating Universe dictionary from each document"):
        for shingle in shingles(text):
            universe.add(shingle)

    universe = sorted(universe)
    # return universe
    print("Universe of shingles got sorted")

    shingle_array = [[1 if shingle in shingles(doc_text) else 0 for doc_text in text_list] for shingle in tqdm(
        universe, "Creating Shingling matrix")]

    print("Shingling Matrix just got created for all documents")
    return shingle_array


def shingles(text):
    if len(text) > 1000:
        return get_shingles(text, 10)
    return get_shingles(text, 5)


def get_shingles(text, k):
    list = [md5(text[i:i + k].encode('ascii')).hexdigest()
            for i in range(len(text) - k)]
    unique_list = reduce(
        lambda x, y: x + [y] if x == [] or x[-1] != y else x, list, [])
    return unique_list


if __name__ == "__main__":
    text_list = []
    test = "dhjsakdhjksladh aaaah hdhh dhisis bb b sbbbbbbbbbbbds"
    test_new = "dhjsakdhjksladh aaaah hdhh dhisis bb b sbbbbbbbbbbbds a"
    test_test = "hfoisahgopsdhgjopsjfops fi[psa fpwirpwisapfi a"

    text_list.append(test)
    text_list.append(test_new)
    text_list.append(test_test)
    # pprint(getSinglingMatrix(text_list))

    print(getSignatures(getSinglingMatrix(text_list), 100))
