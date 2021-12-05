from pathlib import Path


def find_coords_aim(input):
    coords = [0,0]
    aim = 0

    for line in input:
        direction, length = line.split()
        length = int(length)
        if direction == "forward":
            coords[0] += length
            coords[1] += length * aim
        if direction == "up":
            aim -= length
        if direction == "down":
            aim += length

    return coords[0] * coords[1]


if __name__ == '__main__':
    input = Path('input.txt').read_text().splitlines()
    print(f'Answer: {find_coords_aim(input)}')
