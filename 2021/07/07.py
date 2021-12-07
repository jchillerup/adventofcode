N,c=sorted(map(int,open('i').read().split(","))),lambda n:n**2+n
L=len(N)
print(sum([abs(n-N[L//2])for n in N]),sum([c(abs(n-sum(N)//L))for n in N])//2)