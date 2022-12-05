
f = open(r'C:\Users\robin\Downloads\rosalind_fibd.txt')
n, k = f.readline().strip().split(" ")
def fib(n, k):
    if n <= 2:
        return 1
    else:
        return fib(n-1,k) + k * fib(n-2,k)
print(fib(int(n), int(k)))