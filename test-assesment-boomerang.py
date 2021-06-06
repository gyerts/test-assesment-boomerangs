import math

# Imagine a sky full of stars, represented by a sequence of
# two-dimensional coordinate points. Defining a "boomerang"
# as a set of 3 stars where if lines are drawn from 2 stars to
# the third vertex star, they would be equal length. Given this
# definition, implement the boomerang_count function, which
# computes the count of unique boomerangs that may be
# formed from a provided list of stars.


def boomerang_count(points) -> int:
    res = 0

    for i, a in enumerate(points):
        map = {}
        for j, b in enumerate(points):
            if i == j:
                continue
            d = get_distance(a, b)
            map[d] = map.get(d, 0) + 1

        for val in map.values():
            res += val * (val-1) / 2

    return res


def get_distance(a, b):
    f = (b[0] - a[0]) ** 2
    s = (b[1] - a[1]) ** 2
    return f if f else s

# *********************************************************
# Example test cases that must pass.
# Examples are provided with ASCII art showing their layout
# and the boomerangs listed as the three stars in the
# boomerang with the vertex star listed in the middle.
# *********************************************************

# Simple 3 stars in a row:
#
# A--B--C.
# Boomerangs: ABC
count = boomerang_count((
    (0, 0),
    (1, 0),
    (2, 0),
))
assert count == 1


# Equilateral triangle:
#
#   A
#  / \
# B---C
# Boomerangs: ABC, ACB, CAB

# there is mistake in this test case, in the test assessment you said that
# Boomerangs are:
#   [v] ABC - correct lines has the same length   (1,7 - 1,7)
#   [-] ACB - incorrect lines not the same length (2   - 1,7)
#   [-] CAB - incorrect lines not the same length (2   - 1,7)
count = boomerang_count((
    (0, 0),
    (1, math.sqrt(3)),
    (2, 0),
))
assert count == 1


# Hub and Spoke:
#
#    C
#    |
# B--A--D
# Boomerangs: BAC, CAD, BAD, BCD
# Missed Boomerangs: BCA, ACB, DCA, ACD
count = boomerang_count((
    ( 0, 0),
    (-1, 0),
    ( 0, 1),
    ( 1, 0),
))
assert count == 8
