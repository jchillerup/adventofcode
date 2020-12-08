
numbers = [int(x) for x in open('input').read().split("\n")]

# Star 1
for i in range(len(numbers)):
    for j in range(i+1):
        if numbers[i]+numbers[j] == 2020:
            print(numbers[i]*numbers[j])

# Star 2
for i in range(len(numbers)):
    for j in range(i+1):
        for k in range(j+1):
            if numbers[i]+numbers[j]+numbers[k] == 2020:
                print(numbers[i]*numbers[j]*numbers[k])

                