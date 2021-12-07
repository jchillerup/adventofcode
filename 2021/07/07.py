N,c,s=sorted(map(int,open('i').read().split(","))),lambda n:n**2+n,sum
print(s([abs(n-N[len(N)//2])for n in N]),s([c(abs(n-s(N)//len(N)))for n in N])//2)