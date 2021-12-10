import helpers
import numpy

def expect(opening):
    if opening == '{':
        return '}'
    elif opening == '(':
        return ')'
    elif opening == '[':
        return ']'
    elif opening == '<':
        return '>'
    else:
        return None


def calculate_syntax_error(illegal_chars):
    result = 0
    for char in illegal_chars:
        if char == ')':
            result += 3
        elif char == ']':
            result += 57
        elif char == '}':
            result+= 1197
        elif char == '>':
            result += 25137
        else:
            return 0
    return result


def calculate_autocomplete_scores(incomplete_lines):
    line_results = []
    for line in incomplete_lines:
        result = 0
        for char in line:
            result *= 5
            if char == ')':
                result += 1
            elif char == ']':
                result += 2
            elif char == '}':
                result+= 3
            elif char == '>':
                result += 4
            else:
                return 0
        line_results.append(result)
    return line_results


def legalize(input):
    illegal_chars = []
    legal = []
    opening = ['{', '(', '[', '<']
    for line in input:
        is_legal = True
        tags = []
        for char in list(line):
            if char in opening:
                tags.append(char)
            else:
                if expect(tags[-1]) == char:
                    tags.pop()
                else:
                    illegal_chars.append(char)
                    is_legal = False
                    break
        if is_legal:
            legal.append(tags)
    return illegal_chars, legal


def part_one(input):
    illegal_chars, legal = legalize(input)
    result = calculate_syntax_error(illegal_chars)
    return result


def part_two(input):
    illegal_chars, legal = legalize(input)
    legal = list(map(lambda x: list(map(lambda y: expect(y), x)), legal))
    legal = list(map(lambda x: list(reversed(x)), legal))
    results = sorted(calculate_autocomplete_scores(legal))
    result = results[int(len(results) / 2)]
    return result


input = helpers.load_puzzle_input(10)
test_input = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]'
]
print('Part one result: %s'%(helpers.run_and_time(part_one, input)))
print('Part two result: %s'%(helpers.run_and_time(part_two, input)))