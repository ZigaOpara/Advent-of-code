import helpers

digit_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def extract_digits(line):
    digits = ''
    for char in line:
        try:
            int(char)
            digits += char
        except ValueError:
            continue
    return digits


def part_one(puzzle_input):
    calibration_values = []
    for line in puzzle_input:
        digits = extract_digits(line)
        calibration_values.append(int(digits[0]+digits[-1]))
    return sum(calibration_values)


def part_two(puzzle_input):
    digits = digit_map.keys()
    calibration_values = []
    for line in puzzle_input:
        new_line = ''
        for i in range (len(line)):
            for digit in digits:
                if line[i:].startswith(digit):
                    new_line += str(digit_map[digit])
                    i += len(digit)-1
                else:
                    new_line += line[i]
        extracted_digits = extract_digits(new_line)
        calibration_values.append(int(extracted_digits[0]+extracted_digits[-1]))
    return sum(calibration_values)


loaded_puzzle_input = helpers.load_puzzle_input(2023, 1)
print('Part one result: %s' % (helpers.run_and_time(part_one, loaded_puzzle_input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, loaded_puzzle_input)))