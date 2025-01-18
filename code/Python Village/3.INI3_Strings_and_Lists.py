import sys

s, a, b, c, d = str(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])

print(s[a:b+1], s[c:d+1])
