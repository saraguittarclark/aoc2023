numstr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numstr_flip = [s[::-1] for s in numstr]
dictnum = dict(zip(numstr, range(1,10)))
dictnum_flip = dict(zip(numstr_flip, range(1,10)))

def find_first(s, part2=False, reverse=False):
    if reverse:
        s = s[::-1]
        d = dictnum_flip
    else:
        d = dictnum
    for i, c in enumerate(s):
        if c.isnumeric():
            return c
        if part2:
            for k,v in d.items():
                if s[i:].startswith(k):
                    return str(v)
            

def solve(fn, part2=False):
    with open(fn) as f:
        lines = f.readlines()

    total = 0

    for li in lines:
        left = find_first(li, part2)
        right = find_first(li, part2, reverse=True)
        total += int(left + right)
    
    return total

def main():
    assert solve('test.txt') == 142
    print(solve('input.txt'))
    assert solve('test2.txt', part2=True) == 281
    print(solve('input.txt', part2=True))
if __name__ == '__main__':
    main()
