import sys
from collections import Counter

s = sys.argv[1]

counts = Counter(s)

print(counts["A"],counts["C"],counts["G"],counts["T"])
