from pathlib import Path

def lantern_fish(input):
    fish_timers = [int(x) for x in input[0].split(',')]
    
    for _ in range(80):
        total_fish = []
        for fish in fish_timers:
            if fish == 0:
                total_fish.append(6)
                total_fish.append(8)
            else:
                total_fish.append(fish - 1)
        fish_timers = total_fish
    return len(total_fish)

if __name__ == '__main__':
    input = Path('input.txt').read_text().splitlines()
    print(f'Answer: {lantern_fish(input)}')