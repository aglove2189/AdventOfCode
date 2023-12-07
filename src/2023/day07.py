from collections import Counter

from get_data import get_data

data = get_data(2023, 7).splitlines()
hands_bids = [d.split() for d in data]
types = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)]


def get_ranks(hand, jokers_wild=False):
    order = "J23456789TQKA" if jokers_wild else "23456789TJQKA"
    possible_ranks = []
    for replacement in "23456789TQKA":
        hand_rank = types.index(tuple(sorted(Counter(hand.replace("J", replacement)).values())))
        possible_ranks.append(hand_rank)
    return max(possible_ranks), list(map(order.index, hand))


for jokers_wild in (False, True):
    ranks_bids = sorted((get_ranks(hand, jokers_wild), int(bid)) for hand, bid in hands_bids)
    print(sum(rank * bid for rank, (_, bid) in enumerate(ranks_bids, start=1)))
