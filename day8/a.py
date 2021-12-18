from pathlib import Path
from collections import defaultdict, Counter

def total_digits(input):
    answer = 0
    for line in input:
        first, second = line.split('|')
        first = first.split()
        second = second.split()
        letter_dict = defaultdict(list)
        for letter in first:
            letter_dict[len(letter)].append(letter)
        for letter in second:
            if len(letter_dict[len(letter)]) == 1:
                answer += 1
    return answer



if __name__ == '__main__':
    input = Path('input.txt').read_text().splitlines()
    print(f'Answer: {total_digits(input)}')