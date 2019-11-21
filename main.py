import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+"\\src")
from lsh import *
from minhash import *
from shingling import *



if __name__ == "__main__":
    text_list = []
    test = "aaaaabbbbbccccc"
    test_new = "aaaaabbbbbccccc"
    test_test = "dsa hsaiofhj"

    text_list.append(test)
    text_list.append(test_new)
    text_list.append(test_test)
    print(calculate_similarity(filter_buckets(getSignatures(getSinglingMatrix(text_list), 100)),len(text_list)))
