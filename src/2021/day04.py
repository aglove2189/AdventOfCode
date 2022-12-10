# -*- coding: utf-8 -*-
from get_data import get_data

data = get_data(2021, 4)

nums, *boards = data.split('\n\n')
nums = list(map(int, nums.split(',')))
boards = [[list(map(int, row.split())) for row in b.splitlines()] for b in boards]


def find_winners(nums, boards):
    drawn = set()
    complete = [False for _ in range(len(boards))]
    for num in nums:
        drawn.add(num)
        for i, board in enumerate(boards):
            horizontal = any(all(r in drawn for r in row) for row in board)
            vertical = any(all(r[i] in drawn for r in board) for i in range(len(board)))
            if horizontal or vertical:
                complete[i] = True
                yield num * sum(r for row in board for r in row if r not in drawn)
                if all(complete):
                    return


print(next(find_winners(nums, boards)))

for winner in find_winners(nums, boards):
    pass
print(winner)
