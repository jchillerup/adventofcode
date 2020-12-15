import tqdm
turns = list(map(int, open('input-little.txt').read().split(",")))

def find_last_occurence(list, needle):
    for j in range(len(list)-2, -1, -1):
        if list[j] == needle:
            return j
    return None

def run_game(turns):
    occurences = dict()    
    for i, v in enumerate(turns):
        if occurences.get(v) is None:
            occurences[v] = [i]
        else:
            occurences[v].append(i)

    for i in tqdm.tqdm(range(len(turns), 30000000)):        
        try:
            lo2 = occurences[turns[i-1]][-2]
        except:
            lo2 = None
        
        if lo2 is None:
            turns.append(0)
            try:
                occurences[0].append(i)
            except:
                occurences[0] = [i]
        else:
            last_seen_turn = i-(lo2+1)
            
            turns.append(last_seen_turn)
            try:
                occurences[last_seen_turn].append(i)
            except KeyError:
                occurences[last_seen_turn] = [i]

    return turns[-1]

#assert(run_game([0,3,6]) == 436)
#assert(run_game([1,3,2]) == 1)
#assert(run_game([2,1,3]) == 10)
#assert(run_game([1,2,3]) == 27)
#assert(run_game([2,3,1]) == 78)
#assert(run_game([3,2,1]) == 438)
#assert(run_game([3,1,2]) == 1836)

print(run_game([7,12,1,0,16,2]))