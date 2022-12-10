from get_data import get_data

data = get_data(2020, 5)


def find(space, range_=range(127)):
    for c in space:
        if c in ("B", "R"):
            range_ = range_[len(range_) // 2 : :]
        else:
            range_ = range_[0 : len(range_) // 2]
    try:
        return range_[0] + 1
    except IndexError:
        return 0


seat_ids = [find(i[0:7]) * 8 + find(i[7::], range_=range(7)) for i in data.splitlines()]
print(max(seat_ids))
print([i for i in range(min(seat_ids), max(seat_ids)) if i not in seat_ids])
