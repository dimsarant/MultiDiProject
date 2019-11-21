from math import ceil,sqrt
from tqdm import tqdm
from itertools import combinations

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

def calculate_similarity(total_bucket_list,num_of_docs):
    occurance_matrix = [[0]*num_of_docs for _ in range(num_of_docs)]
    for band in total_bucket_list:
        for bucket in band:
            for comb in combinations(bucket, 2):
                occurance_matrix[comb[0]][comb[1]] += 1
    return occurance_matrix
