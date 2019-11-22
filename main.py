import os
import sys
import numpy as np
import pandas as pd
from src.lsh import *
from src.shingling import *
from src.minhash import *
from src.cosim import *


def select_candidates(probabilities):
    candidates = pd.DataFrame([list(range(len(text_list))),list(probabilities)], index=['Combinations', 'Probabilities'])
    candidates = candidates.sort_values(by='Probabilities', axis=1, ascending=False)
    candidates = list(candidates.iloc[0])
    return candidates


if __name__ == "__main__":
    text_list = []
    test = "aaaaa bbbbb ccccc"
    test_new = "aaaaa bbbbb ccccc"
    test_test = "bbbbb ccccc ddddd"

    text_list.append(test)
    text_list.append(test_new)
    text_list.append(test_test)
    similarities=np.array(calculate_similarity(filter_buckets(getSignatures(getSinglingMatrix(text_list), 100)),len(text_list)))
    probabilities=similarities[np.triu_indices(len(similarities),1)]
    print("\nBucket Results:")
    for index, comb in enumerate(combinations(range(len(text_list)), 2)):
        print("Texts "+str(comb)+" : similarity = "+str(probabilities[index]))

    print("\nSimilarity Results:")
    similarity=cosign_sim(text_list)
    combinations = list(combinations(range(len(text_list)), 2))
    for candidate in select_candidates(probabilities):
        print("Texts "+str(combinations[candidate])+" : similarity = "+str(similarity[candidate])+"%")
