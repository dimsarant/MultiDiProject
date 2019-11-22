import re
from math import factorial

def cosign_sim(text_list):
    unique_words = []
    doc_words = []
    for text in text_list:
        words = re.split(r'\W+', text)
        doc_words.append(words)
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
    unique_words.sort()
    #bazw tis times emfanishs ths kathe lekshs gia kathe arxeio
    doc_appear = []
    for i in range(len(text_list)):
        doc_appear.append([0]*len(unique_words))
        for j in range(len(doc_words[i])):
            for k in range(len(unique_words)):
                if(unique_words[k]==doc_words[i][j]):
                    doc_appear[i][k] += 1
    #briskw thn omoiothta metaksi twn arxeiwn
    doc_abs = []
    for i in range(len(doc_appear)):
        temp=0
        for j in range(len(doc_appear[i])):
            temp+=doc_appear[i][j]**2
        temp=temp**(0.5)
        doc_abs.append(temp)
    similarity = []
    #upologismos similarities
    for i in range(len(text_list)):
        for j in range(i+1, len(doc_appear)):
            mul=0
            for k in range(len(doc_appear[i])):
                mul+=doc_appear[i][k]*doc_appear[j][k]
            similarity.append(round(100*mul/(doc_abs[i]*doc_abs[j]),2))
    return similarity
