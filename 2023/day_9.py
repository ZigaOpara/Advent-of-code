import helpers


def generate_sequences(sequence):
    sequences = [sequence]
    idx = 0
    while True:
        differences = []
        for i in range(len(sequences[idx][1:])):
            differences.append(sequences[idx][i + 1] - sequences[idx][i])
        sequences.append(differences)
        if all([x == 0 for x in differences]):
            break
        idx += 1
    sequences.reverse()
    return sequences


def find_next_value(sequence):
    sequences = generate_sequences(sequence)
    for i, s in enumerate(sequences[1:]):
        s.append(s[-1] + sequences[i][-1])
    return sequences[-1][-1]


def find_prev_value(sequence):
    sequences = generate_sequences(sequence)
    for i, s in enumerate(sequences[1:]):
        s.insert(0, s[0] - sequences[i][0])
    return sequences[-1][0]


def part_one(puzzle_input):
    return sum(map(find_next_value, puzzle_input))


def part_two(puzzle_input):
    return sum(map(find_prev_value, puzzle_input))


loaded_puzzle_input = helpers.load_puzzle_input(2023, 9)
parsed = list(map(lambda x: list(map(int, x.split(' '))), loaded_puzzle_input))
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))