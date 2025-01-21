#Basic premise was that you could get number of birth and death numbers on each month from no. born in previous months
import sys
n, m = int(sys.argv[1]),int(sys.argv[2])

Alive = 1
bornOnMonth = {1:1}

for month in range(2,n+1):
    died = 0
    born = 0
    for i in range(month - m, month-2+1):
        born += bornOnMonth.get(i,0)

    died = bornOnMonth.get(month - m, 0)
    bornOnMonth[month] = born
    Alive = Alive - died + born

print(Alive)
