test0 = '''1 3
2 3
4 5'''

test1 = '''6 8
5 8
8 9
5 7
4 7'''

test2 = '''2 4
3 6
1 3
6 8'''


bonus = '''15 18
13 16
9 12
3 4
17 20
9 11
17 18
4 5
5 6
4 5
5 6
13 16
2 3
15 17
13 14'''


def solve(lines):
    '''
    Final version.

    The first try only passed test 1 and 2, but not 0 or bonus.

    Second try passed them all, but was inefficient. Basic logic
    it had (in psuedo code):
        if any([i in ranges for i in max_stop_in_ranges]): total++

    Longer explination of second try:
        If 'i' is in the ranges at any point, the light was on
        so we increment the total time the light was on.
        eg. using test0
          i = 0, i not in any of ranges, so False (no increment)
          i = 1, i in range(1, 3), so True (increment)
          i = 2, i in range(1, 3) and range(2, 3), True (increment)
          i = 3, i not in any ranges, False (no increment)
          i = 4, i in range(4, 5) (ranges[2]), True (increment)
          i = 5, i not in any range, False (no increment)

        As you can see we increment 3 times, so total = 3


    The final version is roughly the same idea, but skipping steps. Rather
    than checking if something is in the ranges, it just builds a set of all
    returned numbers from the ranges and reports its  length. Same result,
    different path.
    '''
    ranges = list()
    for line in lines.split('\n'):
        # Generic 'turn the pairs into a tuple of ints'
        ints = tuple(map(int, line.split()))

        # This will give us a list of ranges. The ranges
        # are the period of time the lights were on.
        ranges.append(range(*ints))

    # Rebuild ranges with their values and turn into a set.
    ranges = set([y for x in ranges for y in x])

    # return length of the set
    return len(ranges)


def cheeky(lines):
    '''How short can I make solve?'''
    # Hahahahaha come at me bro
    return len(set([y for x in [range(*tuple(map(int, line.split()))) for line in lines.split('\n')] for y in x]))


print('solve(test0) == 3? {}'.format(solve(test0) == 3))
print('solve(test1) == 5? {}'.format(solve(test1) == 5))
print('solve(test2) == 7? {}'.format(solve(test2) == 7))
print('solve(bonus) == 14? {}'.format(solve(bonus) == 14))
