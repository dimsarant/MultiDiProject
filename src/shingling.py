from functools import reduce
from itertools import combinations
from hashlib import md5
from tqdm import tqdm
from random import randint
from pprint import pprint
from math import ceil,sqrt

def calculate_similarity(total_bucket_list,num_of_docs):
    occurance_matrix = [[0]*num_of_docs for _ in range(num_of_docs)]
    for band in total_bucket_list:
        for bucket in band:
            for comb in combinations(bucket, 2):
                occurance_matrix[comb[0]][comb[1]] += 1
    return occurance_matrix

def filter_buckets(signature_matrix):
    bands_num = 20
    num_of_buckets = 2*ceil(sqrt(len(signature_matrix)))
    total_bucket_list = []
    for band in tqdm(range(0,len(signature_matrix[0]),5),"Creating buckets for each band"):
        band_list = [[] for _ in range(num_of_buckets)]
        for doc_idx in range(len(signature_matrix)):
            band_list[abs(hash(tuple(signature_matrix[doc_idx][band:band+5]))) % num_of_buckets].append(doc_idx)
        total_bucket_list.append(band_list)
    return total_bucket_list

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

def getHashfunction(num_of_hash_fun, len_of_array):
    return [lambda x: (randint(0,32)*x + randint(0,32)) % len_of_array for _ in tqdm(range(num_of_hash_fun), "Creating {} hash functions".format(num_of_hash_fun))]

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
    test = "aaaaabbbbbccccc"
    test_new = "aaaaabbbbbccccc"
    test_test = "dsa hsaiofhj"

    text_list.append(test)
    text_list.append(test_new)
    text_list.append(test_test)
    # pprint(getSinglingMatrix(text_list))

    print(calculate_similarity(filter_buckets(getSignatures(getSinglingMatrix(text_list), 100)),len(text_list)))
