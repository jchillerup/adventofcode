def cost(n):return n*(1+n)/2
def mean(N):return sum(N)//len(N)
N=sorted(map(int,open('input.txt').read().split(",")))
print(sum([abs(n-N[len(N)//2]) for n in N]))
print(int(sum([cost(abs(n-mean(N))) for n in N])))


#
# print(sum([abs(n-N[len(N)//2]) for n in N]))