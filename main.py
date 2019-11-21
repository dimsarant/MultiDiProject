import os
import sys
<<<<<<< HEAD
from src.lsh import *
from src.shingling import *
from src.minhash import *
=======
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+"\\src")
from lsh import *
from minhash import *
from shingling import *
from itertools import combinations
import numpy as np

>>>>>>> 05f74f696dab297c2cbec6b35d86dd855e28ecfe


if __name__ == "__main__":
    text_list = []
    test = "aaaaabbbbbccccc"
    test_new = "aaaaabbbbbccccc"
    test_test = "bbbbbcccccddddd"

    text_list.append(test)
    text_list.append(test_new)
    text_list.append(test_test)
    similarities=np.array(calculate_similarity(filter_buckets(getSignatures(getSinglingMatrix(text_list), 100)),len(text_list)))
    probabilities=similarities[np.triu_indices(len(similarities),1)]*10/2
    print("\nResults:")
    for index, comb in enumerate(combinations(range(len(text_list)), 2)):
        print("Texts "+str(comb)+" : similarity = "+str(probabilities[index])+"%")
