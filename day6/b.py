from pathlib import Path
from collections import defaultdict

def lantern_fish(input):
    fish_timers = [int(x) for x in input[0].split(',')]
    
    lantern_fish_map = {}

    for fish in fish_timers:
        if fish not in lantern_fish_map:
            lantern_fish_map[fish] = 0
        lantern_fish_map[fish] += 1        

    for day in range(256):
        total_fish = defaultdict(int)
        for fish, count in lantern_fish_map.items():
            if fish == 0:
                total_fish[6] += count
                total_fish[8] += count
            else:
                total_fish[fish - 1] += count
        lantern_fish_map = total_fish
    return sum(lantern_fish_map.values())

if __name__ == '__main__':
    input = Path('input.txt').read_text().splitlines()
    print(f'Answer: {lantern_fish(input)}')