from get_data import get_data
from itertools import combinations
import z3

data = get_data(2025, 10).splitlines()
part1 = 0
part2 = 0

for d in data:
    target, *buttons_raw, joltage = d.split()

    target = target.replace("[", "").replace("]", "")
    target = {i for i, char in enumerate(target) if char == "#"}

    buttons = []
    for b in buttons_raw:
        b = b.replace("(", "").replace(")", "")
        buttons.append(set(map(int, b.split(","))))

    joltage = joltage.replace("{", "").replace("}", "")
    joltage = list(map(int, joltage.split(",")))

    found = False
    for i in range(len(buttons) + 1):
        for combo in combinations(buttons, i):
            current_state = set()
            for btn in combo:
                current_state ^= btn

            if current_state == target:
                part1 += i
                found = True
                break
        if found:
            break

    opt = z3.Optimize()

    presses = [z3.Int(f"p_{i}") for i in range(len(buttons))]
    opt.add(p >= 0 for p in presses)

    for i, j in enumerate(joltage):
        affected_by = [p for k, p in enumerate(presses) if i in buttons[k]]
        opt.add(sum(affected_by) == j)

    opt.minimize(sum(presses))

    if opt.check() == z3.sat:
        model = opt.model()
        part2 += sum(model[p].as_long() for p in presses)

print(part1)
print(part2)
