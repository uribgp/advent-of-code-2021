from pathlib import Path

def intersecting_vents(input):
    grid = {}
    answer = 0
    for line in input:
        start, finish = line.split('->')
        x1, y1 = start.split(',')
        x2, y2 = finish.split(',')
        x1 = int(x1.strip())
        x2 = int(x2.strip())
        y1 = int(y1.strip())
        y2 = int(y2.strip())
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        if x1 == x2 or y1 == y2:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x,y) not in grid:
                        grid[(x,y)] = 0
                    grid[(x,y)] += 1
    for k in grid:
        if grid[k] > 1:
            answer += 1
    return answer

if __name__ == '__main__':
    input = Path('input.txt').read_text().splitlines()
    print(f'Answer: {intersecting_vents(input)}')