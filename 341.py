tests = (
    '33244332',
    '82156821568221',
    '1111101111011011',
    '124489903108444899'
)


def getRepeats(string):
    lookup = dict()

    # Could do int(len(string) + 1) / 2, len(string) // 2 + 1, or math.ceil
    # In spirit of fairness, the divide by two logic was DaPinkOne's idea.
    for seg in range(1, (len(string) // 2)):
        for chunk in range((len(string) - seg) + 1):
            data = string[chunk:chunk+seg]  # Pretty variables ooo

            if not lookup.get(data):
                # Do it once.
                count = string.count(data)

                if count > 1:
                    lookup[data] = count

    return lookup


for test in tests:
    print(getRepeats(test))
