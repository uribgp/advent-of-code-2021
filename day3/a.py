from pathlib import Path

def calculate_power_consumption(input):
    gamma = ""
    epsilon = ""
    input_length = len(input[0])

    for i in range(input_length):
        count_0 = 0
        count_1 = 0
        for line in input:
            if line[i] == "0":
                count_0 += 1
            else:
                count_1 +=1

        if count_0 > count_1:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    return int(gamma, 2) * int(epsilon, 2)
    # return power_consumption; gamma * epsilon




if __name__ == '__main__':
    input = Path('input.txt').read_text().splitlines()
    print(f'Answer: {calculate_power_consumption(input)}')