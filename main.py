import os
import sys
from src.lsh import *
from src.shingling import *
from src.minhash import *


if __name__ == "__main__":
    text_list = []
    test = "aaaaabbbbbccccc"
    test_new = "aaaaabbbbbccccc"
    test_test = "dsa hsaiofhj"

    text_list.append(test)
    text_list.append(test_new)
    text_list.append(test_test)
    print(calculate_similarity(filter_buckets(getSignatures(getSinglingMatrix(text_list), 100)),len(text_list)))
