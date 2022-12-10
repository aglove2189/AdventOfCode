import itertools

from get_data import get_data

print(get_data(2021, 21))


class Die:
    def __init__(self):
        self.generator = itertools.cycle(range(1, 101))
        self.rolls = 0

    def roll(self):
        self.rolls += 3
        return sum(next(self.generator) for _ in range(3))


class Player:
    def __init__(self, position, score):
        self.position = position
        self.score = score

    def move(self, roll):
        self.position = (self.position + roll) % 10
        self.score += self.position + 1


def part1():
    player1 = Player(4, 0)
    player2 = Player(5, 0)
    die = Die()
    while True:
        for player in (player1, player2):
            player.move(die.roll())
            if player.score >= 1000:
                return min(player1.score, player2.score) * die.rolls


print(part1())
