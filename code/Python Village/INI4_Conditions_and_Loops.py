import sys

a, b = int(sys.argv[1]), int(sys.argv[2])

sum = 0

while a <= b:
    if a%2 == 1:
        sum = sum + a
    a = a + 1

print(sum)
