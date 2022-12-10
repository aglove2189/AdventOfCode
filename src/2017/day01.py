# -*- coding: utf-8 -*-
from get_data import get_data

data = get_data(2017, 1)

captcha = list(map(int, str(data)))
print(sum(c for i, c in enumerate(captcha) if c == captcha[i-1]))

print(sum(c for i, c in enumerate(captcha) if c == captcha[i - len(captcha) // 2]))
