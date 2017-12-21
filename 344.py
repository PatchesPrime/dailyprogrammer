def b_n(integer):
    data = [x for x in bin(int(integer))[2:].split('1') if x != '']

    # Even though b_0 should be 0...The wiki says it's always 1..so..
    if integer == 0:
        return 1

    for x in data:
        if len(x) % 2 != 0:
            return 0
    return 1


# All should be true.
print('Test 1: ', b_n(19611206) == 0)
print('Test 2: ', b_n(4) == 1)
print('Test 3: ', b_n(20) == 0)
print('Test 4: ', b_n(5) == 0)

# Challenge says 'if given 20' the last digit should be 0.
# range() in python goes UP to, but does not include, the number.
# With that said, fixed by going to 21.
t5 = '1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0'
print('Test 5: ', t5 == ', '.join([str(b_n(x)) for x in range(21)]))
