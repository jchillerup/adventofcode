import itertools, time
from copy import copy, deepcopy
from functools import lru_cache
tiles = [list(row) for row in open('input.txt').read().strip().split("\n")]

def get_tile(tiles, x, y):
    if x < 0 or x >= len(tiles):
        return None
    if y < 0 or y >= len(tiles[0]):
        return None

    return tiles[x][y]

def ray(tiles, x, y, direction):
    # print(x, y, direction)
    c = get_tile(tiles, x, y)

    if c is None or c != ".":
        return c
    else:
        return ray(tiles, x+direction[0], y+direction[1], direction)

def get_num_adjacent(tiles, x, y, search_value):
    directions = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
    del directions[4]

    adjacent_tiles = [ray(tiles, x+direction[0], y+direction[1], direction) for direction in directions]
    
    return adjacent_tiles.count(search_value)


def iterate(tiles):
    new_tiles = deepcopy(tiles)
    for x, row in enumerate(tiles):
        for y, tile in enumerate(row):
            #print(x, y, tile)
            #assert(tile == get_tile(tiles, x, y))

            if tile == 'L' and get_num_adjacent(tiles, x, y, "#") == 0:
                new_tiles[x][y] = "#"
            
            if tile == '#' and get_num_adjacent(tiles, x, y, "#") >= 5:
                new_tiles[x][y] = "L"
    return new_tiles

def serialize(l):
    return "\n".join(["".join(l[i]) for i in range(len(l))])


prev_board = list()
i=0
while True:
    prev_board = deepcopy(tiles)
    new_board = iterate(tiles)
    print(prev_board)
    if serialize(prev_board) == serialize(new_board):
        print(i)
        print(serialize(new_board).count("#"))
        break;
    
    tiles = deepcopy(new_board)
    i+=1