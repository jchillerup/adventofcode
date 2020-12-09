import itertools

numbers = [int(x) for x in open('input.txt', 'r').read().strip().split("\n")]

def sliding_window(iterable, n=2):
    iterables = itertools.tee(iterable, n)
    
    for iterable, num_skipped in zip(iterables, itertools.count()):
        for _ in range(num_skipped):
            next(iterable, None)
    
    return zip(*iterables)


PREAMBLE_LENGTH = 25

def check(haystack, sum_):
    for a,b in itertools.combinations(haystack, 2):
        prospective_sum = a+b
        if prospective_sum == sum_:
            return True

    return False

for sum_, haystack in zip(numbers[PREAMBLE_LENGTH:], sliding_window(numbers, PREAMBLE_LENGTH)):
    if check(haystack, sum_) == False:
        print(sum_)
        break;

# Star 2

for win_length in range(len(numbers)):
    
    for w in sliding_window(numbers, win_length):
        #print(w)
        #print(sum(w))
        if sum(w) == sum_:
            print(w)
            print(min(w)+max(w))