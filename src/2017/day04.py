# -*- coding: utf-8 -*-
from collections import Counter

from get_data import get_data

data = get_data(2017, 4)


def is_valid(passphrase):
    passphrase = passphrase.split()
    return len(passphrase) == len(set(passphrase))

print(sum([is_valid(p) for p in data.strip().split('\n')]))


def is_valid2(passphrase):
    passphrase = passphrase.split()
    passphrase2 = set([tuple(sorted(Counter(p).items())) for p in passphrase])
    return len(passphrase) == len(passphrase2)

print(sum([is_valid2(p) for p in data.strip().split('\n')]))
