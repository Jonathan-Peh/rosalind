import sys

hamming = 0
s, t = sys.argv[1], sys.argv[2]

for i in range(len(s)):
    if s[i] != t[i]:
        hamming = hamming + 1

print(hamming)
