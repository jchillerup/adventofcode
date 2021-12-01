import itertools, time
from copy import copy, deepcopy
tiles = [list(row) for row in open('input.txt').read().strip().split("\n")]

def get_tile(tiles, x, y):
    if x < 0 or x >= len(tiles):
        return None
    if y < 0 or y >= len(tiles[0]):
        return None

    return tiles[x][y]

def get_num_adjacent(tiles, x, y, search_value):
    adjacent_tiles = [get_tile(tiles, x+i, y+j) for i,j in itertools.product([-1, 0, 1], [-1, 0, 1])]
    del adjacent_tiles[4]  # we don't want to count the seat we're asking about

    return adjacent_tiles.count(search_value)


def iterate(tiles):
    new_tiles = deepcopy(tiles)
    for x, row in enumerate(tiles):
        for y, tile in enumerate(row):
            #print(x, y, tile)
            #assert(tile == get_tile(tiles, x, y))

            if tile == 'L' and get_num_adjacent(tiles, x, y, "#") == 0:
                new_tiles[x][y] = "#"
            
            if tile == '#' and get_num_adjacent(tiles, x, y, "#") >= 4:
                new_tiles[x][y] = "L"
    return new_tiles

def serialize(l):
    return "".join(["".join(l[i]) for i in range(len(l))])


prev_board = list()

i=0
while True:
    prev_board = deepcopy(tiles)
    new_board = iterate(tiles)
    if serialize(prev_board) == serialize(new_board):
        print(i)
        print(serialize(new_board).count("#"))
        break;
    
    tiles = deepcopy(new_board)
    i+=1