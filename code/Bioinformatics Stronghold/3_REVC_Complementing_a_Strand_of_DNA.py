import sys

s = sys.argv[1]

reverse_complement = list()

getcomplement = {
    "A":"T",
    "C":"G",
    "G":"C",
    "T":"A"
    }

for i in range(len(s)):
    reverse_complement.append(getcomplement[s[-(i+1)]])

print("".join(reverse_complement))
