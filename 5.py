
b = {65: 'A', 42: 'o', 57: 'e', 26: 'u', 46: 'i', 28: 'p', 38: 'b', 35: 'd', 15: 't', 24: 'g', 61: 'k', 12: 'v', 17: 'f', 55: 'z', 19: 's', 8: 'h', 16: 'm', 43: 'r'}

c = sorted(list(b.keys()))

while len(list(b.keys()))!= 3:
    e = c[0]
    f = c[1]
    lol = b[e] + b[f]
    b.pop(e)
    b.pop(f)
    b[e+f] = lol
    c = sorted(list(b.keys()))

print(b)

a = b.values()
for i in a:
    print(len(i))

answer = {159: 'fsbor', 199: 'hvgiupz', 249: 'ekAtmd'}

