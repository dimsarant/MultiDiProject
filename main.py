import os
import sys
from src.lsh import *
from src.shingling import *
from src.minhash import *
import numpy as np


if __name__ == "__main__":
    text_list = []
    test = "aaaaabbbbbccccc"
    test_new = "aaaaabbbbbccccc"
    test_test = "bbbbbcccccddddd"

    text_list.append(test)
    text_list.append(test_new)
    text_list.append(test_test)
    similarities=np.array(calculate_similarity(filter_buckets(getSignatures(getSinglingMatrix(text_list), 100)),len(text_list)))
    probabilities=similarities[np.triu_indices(len(similarities),1)]
    print("\nResults:")
    for index, comb in enumerate(combinations(range(len(text_list)), 2)):
        print("Texts "+str(comb)+" : similarity = "+str(probabilities[index]))
