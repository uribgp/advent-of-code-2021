from pathlib import Path

def least_fuel(input):
    fuel_required = 0
    number_input = [int(x.strip()) for x in input.split(',')]
    number_input.sort()
    median = number_input[len(number_input) // 2]
    for crab_position in number_input:
        fuel_required += abs(median - crab_position)
    return fuel_required


if __name__ == '__main__':
    input = Path('input.txt').read_text().splitlines()
    print(f'Answer: {least_fuel(input[0])}')