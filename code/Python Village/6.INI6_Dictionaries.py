import sys
from collections import Counter

s = sys.argv[1:]

counts = Counter(s)

for text, count in counts.items():
    print(text,count)
