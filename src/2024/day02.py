from get_data import get_data


def safe(report):
    return all(1 <= abs(r1 - r2) <= 3 for r1, r2 in zip(report, report[1:])) and (
        report == sorted(report) or report == sorted(report, reverse=True)
    )


def safe2(report):
    return any(safe(report[:i] + report[i + 1 :]) for i in range(len(report)))


data = [list(map(int, d.split())) for d in get_data(2024, 2).splitlines()]
print(sum(map(safe, data)))
print(sum(map(safe2, data)))
