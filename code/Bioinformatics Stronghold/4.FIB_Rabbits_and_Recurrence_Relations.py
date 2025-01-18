import sys

n, k = int(sys.argv[1]), int(sys.argv[2])

months_passed=3
end_of_month = {1:1,2:1}

while months_passed <= n:
    end_of_month[months_passed] = end_of_month[months_passed - 2]*k +end_of_month[months_passed - 1]
    months_passed = months_passed + 1

print(end_of_month[n])
