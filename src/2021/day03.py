from collections import Counter

from get_data import get_data

data = get_data(2021, 3).split("\n")

theta, epsilon = "", ""
for i in range(len(data[0])):
    c = Counter(j[i] for j in data)
    if c["0"] > c["1"]:
        theta += "0"
        epsilon += "1"
    else:
        theta += "1"
        epsilon += "0"
print(int(theta, 2) * int(epsilon, 2))

oxygen_data = data.copy()
for i in range(len(oxygen_data[0])):
    c = Counter(j[i] for j in oxygen_data)
    if c["0"] > c["1"]:
        oxygen_data = [k for k in oxygen_data if k[i] == "0"]
    else:
        oxygen_data = [k for k in oxygen_data if k[i] == "1"]
    if oxygen_data:
        oxygen = oxygen_data[0]

co2_data = data.copy()
for i in range(len(co2_data[0])):
    c = Counter(j[i] for j in co2_data)
    if c["0"] > c["1"]:
        co2_data = [k for k in co2_data if k[i] == "1"]
    else:
        co2_data = [k for k in co2_data if k[i] == "0"]
    if co2_data:
        co2 = co2_data[0]
print(int(oxygen, 2) * int(co2, 2))
