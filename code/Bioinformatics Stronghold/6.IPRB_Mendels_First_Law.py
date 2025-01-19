import sys

k, m, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

t = k+m+n
case_no = [0] * 5

case_no[0] = k*m/t/(t-1)*1*2
case_no[1] = k*n/t/(t-1)*1*2
case_no[2] = k*(k-1)/t/(t-1)*1
case_no[3] = m*(m-1)/t/(t-1)*0.75
case_no[4] = m*n/t/(t-1)*0.5*2

print(sum(case_no))
