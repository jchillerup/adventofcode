gamestrings = open('input.txt').read().split("\n")

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def parse(gs):
    game_id, drawingsetstrings = gs.split(": ")

    game_id = int(game_id.replace("Game ", ""))
    
    for dset in drawingsetstrings.split("; "):
        drawings = dset.split(", ")

        for drawing in drawings:
            quantity, identifier = drawing.split(" ")
            quantity = int(quantity)

            if quantity > bag[identifier]:
                return False, game_id
            # print(quantity)
    return True, game_id
    # print(game_id)
sum = 0
for gs in gamestrings:
    res, id = parse(gs)

    if res:
        sum += id

print(sum)