def c(n):return n**2+n
N=sorted(map(int,open('input.txt').read().split(",")))
print(sum([abs(n-N[len(N)//2]) for n in N]),sum([c(abs(n-sum(N)//len(N))) for n in N])//2)