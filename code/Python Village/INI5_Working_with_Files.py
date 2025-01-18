f = open("rosalind_ini5.txt","r")
out = open("output.txt", "a")

while True:
    f.readline()
    l = f.readline()
    if len(l) == 0:
        break
    else:
        out.write(l)
