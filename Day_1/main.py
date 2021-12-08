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


number_of_increase = 0
last_value = 0
for i in range(len(inputs)):
    if len(inputs) - i < 3:
        break
    set_of_3 = inputs[i:i+3]
    total = sum(set_of_3)
    if i == 0 :
        continue
    if total > last_value:
        number_of_increase += 1
    last_value = total
    
print(number_of_increase)
