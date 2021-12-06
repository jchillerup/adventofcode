G,F = map(int,open('i').read().split(",")),[0]*9
for f in G: F[f]+=1
for z in range(256):
    F.append(F.pop(0))
    F[6] += F[8]
    if z in [79,255]: print(sum(F))