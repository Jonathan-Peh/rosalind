# Yes, I could have just done naive exact matching, but I wanted to practice some Boyer-Moore
import sys
ACGTtointind = {"A":0,"C":1,"G":2,"T":3}

def preproc_badcharacter(pattern,length):
    table = [-1]*4
    for i in range(length):
        table[ACGTtointind[pattern[i]]] = i
    return(table)

def searchstring_bmbc(pattern,text):
    len_p = len(pattern)
    len_t = len(text)
    bm_bc = preproc_badcharacter(pattern,len_p)
    shifted = 0
    results = []

    while(shifted <= len_t - len_p):
        i = len_p -1
        while i>=0:
            if pattern[i] == text[shifted+i]:
                i -= 1
            else: break

        if i == -1:
            results.append(str(shifted+1))
            if shifted + len_p < len_t:
                shifted += 1
        else:
            shifted += max(1, i - bm_bc[ACGTtointind[text[shifted+i]]])
    return(results)


text, pattern = sys.argv[1], sys.argv[2]

print(" ".join(searchstring_bmbc(pattern,text)))
