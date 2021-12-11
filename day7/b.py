from pathlib import Path

def calculate_values(num):
    return num*(num + 1) / 2


def least_fuel(input):
    fuel_required = 999999999999999
    number_input = [int(x.strip()) for x in input.split(',')]

    for median in range(2000):
        current_score = 0
        for crab in number_input:
            total_distance = abs(crab - median)
            current_score += calculate_values(total_distance)
        if current_score < fuel_required:
            fuel_required = current_score
    return fuel_required


if __name__ == '__main__':
    input = Path('input.txt').read_text().splitlines()
    print(f'Answer: {least_fuel(input[0])}')