def pretty_fast():
    return sum([x for x in range(100_000)])


def little_bit_slower():
    nums = []
    for i in range(1_000):
        for j in range(1_000):
            nums.append(i + j)


def very_slow():
    nums = []
    for i in range(100):
        for j in range(1_000):
            for z in range(1_000):
            	nums.append(i + j + z)
