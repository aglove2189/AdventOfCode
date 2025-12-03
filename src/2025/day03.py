from get_data import get_data

data = get_data(2025, 3).split()


def solve(data, num_batteries):
    total = 0
    for d in data:
        to_drop = len(d) - num_batteries
        stack = []
        for i in d:
            while stack and i > stack[-1] and to_drop > 0:
                stack.pop()
                to_drop -= 1
            stack.append(i)
        total += int("".join(stack[:num_batteries]))
    return total


print(solve(data, 2))
print(solve(data, 12))
