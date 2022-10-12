import sys

n = int(sys.stdin.readline())
boks = list(sys.stdin.readline().rstrip().split(' '))
temp = boks[0].split('+')
real, imaginary = int(temp[0]), int(temp[1][:-1])

for bok in boks[1:]:
    temp = bok.split('+')
    r, i = int(temp[0]), int(temp[1][:-1])
    real, imaginary = (real * r) - (i * imaginary), (real * i) + (r * imaginary)
    real, imaginary = real % 10007 if real > 0 else -(-imaginary % 10007), imaginary % 10007 if imaginary > 0 else -(-imaginary % 10007)
print(f'{real}+{imaginary}i')