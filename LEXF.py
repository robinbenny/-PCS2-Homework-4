import itertools
n = 3
s='A B C D E F G H'
lst = list(map(str,s.split()))
x = list(itertools.product(lst, repeat=n))

print(*[''.join(i) for i in x],sep='\n')