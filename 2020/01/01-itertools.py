import itertools

numbers = [int(x) for x in open('input').read().split("\n")]

# Star 1
for i,j in itertools.combinations_with_replacement(numbers, 2):
    if i+j == 2020:
        print(i*j)

# Star 2
for i,j,k in itertools.combinations_with_replacement(numbers, 3):
    if i+j+k == 2020:
        print(i*j*k)