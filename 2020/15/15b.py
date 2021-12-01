import tqdm

def set_occurence(occurences, key, value):
    if occurences[key] is None:
        occurences[key] = [value]
        return
    
    occurences[key] = [occurences[key][-1], value]

def get_second_to_last_occurence(occurences, v):
    try:
        return occurences[v][-2]
    except:
        return None
        

def run_game(seed, num_turns=2020):
    occurences = [None]*num_turns
    for i, v in enumerate(seed):
        set_occurence(occurences, v, i)

    seed_len = len(seed)
    seed.extend([None]*(num_turns-len(seed)))

    for i in tqdm.tqdm(range(seed_len, num_turns)):        
        lo2 = get_second_to_last_occurence(occurences, seed[i-1])
        if lo2 is None:
            last_seen_difference = 0
        else:
            last_seen_difference = i-(lo2+1)

        set_occurence(occurences, last_seen_difference, i)
        seed[i] = last_seen_difference

    return seed[-1]

assert(run_game([0,3,6]) == 436)
assert(run_game([1,3,2]) == 1)
assert(run_game([2,1,3]) == 10)
assert(run_game([1,2,3]) == 27)
assert(run_game([2,3,1]) == 78)
assert(run_game([3,2,1]) == 438)
assert(run_game([3,1,2]) == 1836)

print(run_game([7,12,1,0,16,2], 30000000))