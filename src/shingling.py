from functools import reduce
from hashlib import md5

def shingles(text):
    if len(text) > 1000: return get_shingles(text, 10)
    return get_shingles(text, 5)

def get_shingles(text, k):
    list = [md5(text[i:i+k].encode('ascii')).hexdigest() for i in range(len(text) - k)]
    unique_list = reduce(lambda x,y: x+[y] if x==[] or x[-1] != y else x, list,[])
    return unique_list

if __name__ == "__main__":
    test = shingles("dhjsakdhjksladh aaaah hdhh dhisis bb b sbbbbbbbbbbbds")
    print(test)
