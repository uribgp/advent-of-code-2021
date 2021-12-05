from pathlib import Path

def find_coords(input):
    coords = [0,0]
    for direction in input:
        directions = direction.split()
        directions[1] = int(directions[1])
        if directions[0] == "forward":
            coords[0] += directions[1]
        if directions[0] == "up":
            coords[1] -= directions[1]
        if directions[0] == "down":
            coords[1] += directions[1]
    return coords[0] * coords[1]

if __name__ == '__main__':
    input = Path('input.txt').read_text().splitlines()
    print(f'Answer: {find_coords(input)}')
