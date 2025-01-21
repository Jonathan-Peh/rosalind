collectionlist = []
read = ""

ACGTtoInd = {"A":0, "C":1, "G":2, "T":3} # Dictionary used as looping can be done over the indices, but not the nucleotides (Unequal difference in ASCII values of characters)

with open("rosalind_cons.txt","r") as f: # Reads files. Each element in collection list is a string of a read
    while True:
        l = f.readline().rstrip()
        if len(l) == 0:
            collectionlist.append(read)
            break
        elif l[0] == ">":
            if len(read) != 0:
                collectionlist.append(read)
            read = ""
        else:
            read += l

collection_matrix = [0]*len(collectionlist[0]) # Initialises matrix. Note: [[a]*b]*c creats c exact duplicates of [a]*b. Even ADDRESSES are duplicated. Took me a while to realise
for i in range(len(collection_matrix)):
    collection_matrix[i] = [0]*4

for i in range(len(collectionlist[0])): # This collection matrix is  essentially the required consensus matrix, with coloumns nested in rows
    for j in range(len(collectionlist)):
        for k in ACGTtoInd:
            if collectionlist[j][i] == k:
                collection_matrix[i][ACGTtoInd[k]] +=1


MaxIndices = [0]*len(collection_matrix) # Finds index of most prominent nucelotide in each position
for i in range(len(collection_matrix)):
    MaxIndex = collection_matrix[i].index(max(collection_matrix[i]))
    MaxIndices[i] = MaxIndex

String = "" # Iterates through MaxIndices to convert index to nucleotide
for i in range(len(MaxIndices)):
    for key in ACGTtoInd:
        if ACGTtoInd[key] == MaxIndices[i]:
           String += key

#The rest is just presentation
print("".join(String))
transpose = list(zip(*collection_matrix))

print("A:", " ".join(str(x) for x in transpose[0]))
print("C:", " ".join(str(x) for x in transpose[1]))
print("G:", " ".join(str(x) for x in transpose[2]))
print("T:", " ".join(str(x) for x in transpose[3]))
