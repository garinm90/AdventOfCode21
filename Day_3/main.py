from collections import Counter
input_s = '''\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''
new_values = [] 

with open("input.txt") as file:
    for line in file.readlines():

# for line in input_s.splitlines():
        line_split = list(line.strip())
        for i, character in enumerate(line_split):
            integer = int(character)
            try:
                new_values[i] += character
            except IndexError as error:
                new_values.append(character)

final = ''   
for value in new_values:
    most_common = Counter(value).most_common(1)    
    final += most_common[0][0]

inverted_final = ''.join('1' if x == '0' else '0' for x in final)
gamma = int(final, 2)
epsilon  = int(inverted_final, 2)

print(gamma * epsilon)