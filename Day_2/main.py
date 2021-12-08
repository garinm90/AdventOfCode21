commands = []

with open("input.txt") as file:
    for line in file:
        (key, val) = line.split()
        commands.append((key,val))

horizontal_position = 0
depth = 0
aim = 0
# commands = [('forward', 5), ('down', 5), ('forward', 8), ('up',3), ('down',8),('forward',2)]
for command in commands:
    operation = command[0]
    val = int(command[1])
    print(f'Move {operation} {val} units')
    if operation == 'forward':
        horizontal_position += val
        depth += (aim * val)
    elif operation == 'up':
        aim -= val
    elif operation == 'down':
        aim += val

print(horizontal_position)
print(depth)

print(horizontal_position * depth)