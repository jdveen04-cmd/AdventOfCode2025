lines = open('input.txt').readlines()
lines = [line.rstrip() for line in lines]

def rotate(pos, string):
    direction, count = string[0], int(string[1:])
    if direction == "R":
        pos += count
        passes = pos//100
    elif direction == "L" :
        if pos == 0:
            pos -= count
            passes = (-pos)//100
        else:
            pos -= count
            passes = (-pos)//100 + 1
    else:
        raise ValueError("Invalid direction")
    return passes, pos % 100


part1, part2, position = 0, 0, 50
for line in lines:
    passes, position = rotate(position, line)
    if position == 0: part1 += 1
    part2 += passes

print(part1,part2)

