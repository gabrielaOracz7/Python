import itertools
import random

# a) iterator zwracający 0, 1, 0, 1, 0, 1, 0, 1,...
it1 = itertools.cycle([0, 1])

test_it1_sample = [next(it1) for _ in range(10)]
assert test_it1_sample == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]


#b) iterator zwracający przypadkowo jedną wartość z ("N", "E", "S", "W")
directions = ["N", "E", "S", "W"]
it2 = iter(lambda: random.choice(directions), -1)
for _ in range(10):
    print(next(it2))


#c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6,...
it3 = itertools.cycle(range(0, 7))

test_it3_sample = [next(it3) for _ in range(10)]
assert test_it3_sample == [0, 1, 2, 3, 4, 5, 6, 0, 1, 2]
