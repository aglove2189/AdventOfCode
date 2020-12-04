import os
import click


template = '''# -*- coding: utf-8 -*-
from get_data import get_data\n

data = get_data({yr}, {day})\n'''


@click.command()
@click.option('--year', '-yr', multiple=True)
def build_templates(year):
    for yr in year:
        os.makedirs(yr, exist_ok=True)
        for day in range(1, 26):
            fn = f'{yr}/day{str(day).zfill(2)}.py'
            if not os.path.exists(fn):
                with open(fn, 'w') as f:
                    f.write(template.format(yr=yr, day=day))


if __name__ == '__main__':
    build_templates()
