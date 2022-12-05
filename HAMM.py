sa =  ('string a')
sb =  ('string b')
c = 0
for i in range(len(sa)):
    if sa[i] != sb[i]:
        c = c + 1
print(c)