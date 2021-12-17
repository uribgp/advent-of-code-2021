def AOC_9_a():
  with open("input.txt") as file:
    tubemap = file.read().splitlines()
    lows = get_lows(tubemap)
    print(lows)
    print(sum([int(num) + 1 for (num, x, y) in lows]))

def get_lows(tubemap):
  lows = []
  for y,line in enumerate(tubemap):
    for x,num in enumerate(line):
      num = int(num)
      neighs = neighbours(tubemap, x, y)
      # print(num, neighs, num < min([num for (num, x, y) in neighs]))
      if(num < min([val for (val, x, y) in neighs])):
        lows.append((int(num), x, y))
  return lows

def neighbours(tubemap, x, y):
  a = neigh_up(tubemap, x, y)
  b = neigh_down(tubemap, x, y)
  c = neigh_left(tubemap, x, y)
  d = neigh_right(tubemap, x, y)

  return [x for x in [a,b,c,d] if x is not None]

def neigh_up(tubemap, x, y):
  return (int(tubemap[y - 1][x]), x, y) if y != 0 else None

def neigh_down(tubemap, x, y):
  return (int(tubemap[y + 1][x]), x, y) if y != len(tubemap) - 1 else None

def neigh_left(tubemap, x, y):
  return (int(tubemap[y][x - 1]), x, y) if x != 0 else None

def neigh_right(tubemap, x, y):
  return (int(tubemap[y][x + 1]), x, y) if x != len(tubemap[0]) - 1 else None

if __name__ == '__main__':
    print(f'Answer: {AOC_9_a()}')