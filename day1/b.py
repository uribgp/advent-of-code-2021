from pathlib import Path 

def find_larger_inputs_3s(input):
    count = 0
    for i in range(0, len(input) - 3):
        sum_a = input[i] + input[i + 1] + input[i + 2]
        sum_b = input[i + 1] + input[i + 2] + input[i + 3]
        if  sum_b > sum_a :
            count += 1
    return count


if __name__ == '__main__':
    input = [int(i) for i in Path('input.txt').read_text().splitlines()]
    print(f'Answer: {find_larger_inputs_3s(input)}')
