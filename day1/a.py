from pathlib import Path 

def find_larger_inputs(input):
    count = 0
    for i in range(1, len(input)):
        if input[i] > input[i - 1] :
            count += 1
    return count


if __name__ == '__main__':
    input = [int(i) for i in Path('input.txt').read_text().splitlines()]
    print(f'Answer: {find_larger_inputs(input)}')
