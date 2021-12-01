slope = [x.strip() for x in open('input.txt', 'r').read().strip().split("\n")]
slope_width = len(slope[0])

def get_num_trees(r, c):
    position = [0,0]
    trees = 0
    while position[0] < len(slope)-r:
        position[0] += r
        position[1] += c

        try:
            if slope[position[0]][position[1] % slope_width] == "#":
                trees += 1
        except IndexError:
            print(position)

    return trees



single = get_num_trees(1, 3)
print(single)


mult = 1
mult *= get_num_trees(1, 1)
mult *= get_num_trees(1, 3)
mult *= get_num_trees(1, 5)
mult *= get_num_trees(1, 7)
mult *= get_num_trees(2, 1)
print(mult)