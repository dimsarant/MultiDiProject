from functools import reduce
from hashlib import md5
from tqdm import tqdm


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
