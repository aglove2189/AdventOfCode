import hashlib

from get_data import get_data

data = get_data(2015, 4)

for i in range(100000000):
    h = hashlib.md5((data + str(i)).encode()).hexdigest()
    # if h[:5] == '00000':
    if h[:6] == "000000":
        print(i)
        break
