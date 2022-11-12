import helpers

def find_most_common_bits(input):
    result = ''
    for index in range(len(input[0])):
        zero = 0
        one = 0
        for line in input:
            if line[index] == '0':
                zero += 1
            else:
                one += 1
        if zero > one:
            result += '0'
        else:
            result += '1'
    return result


def invert_byte_string(input):
    result = input.replace('1', '2').replace('0', '1').replace('2', '0')
    return result


def part_one(input):
    gamma = find_most_common_bits(input)
    epsilon = invert_byte_string(gamma)
    result = int(gamma, 2) * int(epsilon, 2)
    return result


def part_two(input):
    gamma = find_most_common_bits(input)
    epsilon = invert_byte_string(gamma)
    input_oxygen = input.copy()
    input_co2 = input.copy()

    for index in range(len(input_oxygen[0])):
        if len(input_oxygen) == 1:
            break
        gamma = find_most_common_bits(input_oxygen)
        input_oxygen = list(filter(lambda line: line[index] == gamma[index], input_oxygen))

    for index in range(len(input_co2[0])):
        if len(input_co2) == 1:
            break
        epsilon = find_most_common_bits(input_co2)
        epsilon = invert_byte_string(epsilon)
        input_co2 = list(filter(lambda line: line[index] == epsilon[index], input_co2))

    result = int(input_oxygen[0], 2) * int(input_co2[0], 2)
    return result


input = helpers.load_puzzle_input(3)

print('Part one result: %s' % (helpers.run_and_time(part_one, input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, input)))
