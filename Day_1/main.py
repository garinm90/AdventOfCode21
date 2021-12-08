with open("input.txt") as file:
    inputs = file.readlines()
    inputs = [int(i.strip()) for i in inputs]

number_of_increase = 0
last_value = 0
for value in inputs:
    if last_value == 0:
        last_value = value
        continue
    if value > last_value:
        number_of_increase += 1
    last_value = value

print(number_of_increase)