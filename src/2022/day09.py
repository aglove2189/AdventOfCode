from get_data import get_data

data = get_data(2022, 9).splitlines()


def solve(num_knots):
    knots = [[0, 0] for _ in range(num_knots)]
    visited = {(0, 0)}

    for line in data:
        dir_, steps = line.split()

        for _ in range(int(steps)):
            if dir_ == "L":
                knots[0][0] -= 1
            elif dir_ == "R":
                knots[0][0] += 1
            elif dir_ == "U":
                knots[0][1] += 1
            elif dir_ == "D":
                knots[0][1] -= 1

            for i in range(1, num_knots):
                diffx = knots[i - 1][0] - knots[i][0]
                diffy = knots[i - 1][1] - knots[i][1]

                if abs(diffx) > 1 or abs(diffy) > 1:
                    if diffx > 0:
                        knots[i][0] += 1
                    elif diffx < 0:
                        knots[i][0] -= 1

                    if diffy > 0:
                        knots[i][1] += 1
                    elif diffy < 0:
                        knots[i][1] -= 1

            visited.add(tuple(knots[-1]))

    return len(visited)


print(solve(2))
print(solve(10))
