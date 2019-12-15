import os
import sys
import numpy as np
from src.lsh import filter_buckets, calculate_similarity, combinations
from src.shingling import getSinglingMatrix
from src.minhash import getSignatures
from src.cosim import cosign_sim


# def select_candidates(probabilities):
#     candidates = pd.DataFrame([list(range(len(text_list))), list(probabilities)],
#                               index=['Combinations', 'Probabilities'])
#     candidates = candidates.sort_values(by='Probabilities', axis=1, ascending=False)
#     candidates = list(candidates.iloc[0])
#     return candidates


if __name__ == "__main__":

    text_list = []
    for file in os.listdir("data/"):
        if file.endswith(".txt"):
            filename = os.path.join("data", file)

            f = open(filename, 'r')
            text_list.append(f.read())

    similarities = np.array(calculate_similarity(filter_buckets(
        getSignatures(getSinglingMatrix(text_list), 100)), len(text_list)))

    triu_idx = combinations(range(len(text_list)), 2)

    print("\nSimilarity Results:")
    for i, j in triu_idx:
        if similarities[i][j] != 0:
            # print(similarities[i][j]])
            similarity = cosign_sim([text_list[i], text_list[j]])
            # combinations = list(combinations(range(len(text_list)), 2))
            print("Texts ({},{}) : similarity = {}%".format(i, j, similarity))
