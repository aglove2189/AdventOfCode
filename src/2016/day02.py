from get_data import get_data

data = get_data(2016, 2).splitlines()

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x, y = 1, 1
code = ""
for line in data:
    for move in line:
        if move == "U" and x > 0:
            x -= 1
        elif move == "D" and x < 2:
            x += 1
        elif move == "L" and y > 0:
            y -= 1
        elif move == "R" and y < 2:
            y += 1
    code += str(keypad[x][y])
print(code)
