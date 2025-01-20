import sys
from codon_table import codon_table #found under misc folder

s = sys.argv[1]
protein = []

for i in range(len(s)//3):
    sub = s[3*i:3*(i+1)]
    amino = codon_table[sub]
    if amino != "Stop":
        protein += amino

print("".join(protein))
