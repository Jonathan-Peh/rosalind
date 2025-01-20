read = ""
dictionary = {}
id_no = ""
with open("rosalind_gc.txt","r") as file:
    while True:
        line = file.readline().rstrip()
        if len(line) == 0:
            dictionary[id_no] = (read.count("G") + read.count("C"))/len(read)
            break
        elif line[0] != ">":
            read = read+line

        elif line[0] == ">":
            if id_no == "":
                id_no = line[1:]
            else:
                dictionary[id_no] = (read.count("G") + read.count("C"))/len(read)
                read = ""
                id_no = line[1:]

print(max(dictionary, key=dictionary.get),max(dictionary.values())*100)
