
def MortalFibonacci(n, m):
    living = [1, 1]

    for i in range(2, n):
        tmp = living[i - 1] + living[i - 2]
        if i == m:
            tmp = tmp - 1
        if i > m:
            tmp = tmp - living[i - m - 1]
        living.append(tmp)
    return living[-1]


n = 98
m = 19

print(MortalFibonacci(n, m))