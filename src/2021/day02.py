from get_data import get_data

data = get_data(2021, 2)
data = [i.split(" ") for i in data.splitlines()]

x, y, aim = 0, 0, 0
for command, ammount in data:
    if command == "up":
        aim -= int(ammount)
    elif command == "down":
        aim += int(ammount)
    elif command == "forward":
        x += int(ammount)
        y += aim * int(ammount)
print(x * aim)
print(x * y)
