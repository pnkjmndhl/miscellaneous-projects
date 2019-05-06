import re
import sys
import textwrap

txt_filename = 'new10000.txt'


matrix = sys.argv[1]

grid = ' '.join(textwrap.wrap(matrix, 4)).split()
GRID = [x.upper() for x in grid]

for value in GRID:
    print '\t\t'+value


nrows, ncols = len(grid), len(grid[0])

import re

alphabet = ''.join(set(''.join(grid)))
bogglable = re.compile('[' + alphabet + ']{5,}$', re.I).match

words = set(word.rstrip('\n') for word in open(txt_filename) if bogglable(word))
prefixes = set(word[:i] for word in words
               for i in range(2, len(word) + 1))


def solve():
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            for result in extending(letter, ((x, y),)):
                yield result


def extending(prefix, path):
    if prefix in words:
        yield (prefix, path)
    for (nx, ny) in neighbors(path[-1]):
        if (nx, ny) not in path:
            prefix1 = prefix + grid[ny][nx]
            if prefix1 in prefixes:
                for result in extending(prefix1, path + ((nx, ny),)):
                    yield result


def neighbors((x, y)):
    for nx in range(max(0, x - 1), min(x + 2, ncols)):
        for ny in range(max(0, y - 1), min(y + 2, nrows)):
            yield (nx, ny)


list_of_words = ' '.join(sorted(set(word for (word, path) in solve()))).split(" ")
list_of_words.sort(key=len, reverse=True)

for word in list_of_words:
    print word
