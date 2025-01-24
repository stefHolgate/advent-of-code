import re

red = 12
green = 13
blue = 14

def solution_one():
    tot = 0
    ok_games = []
    with open('day-02-data.txt') as f:        
        for i, line in enumerate(f):
            cur_line = line.strip()[8:].replace(';',',').split(', ')

            for x in cur_line:
                n = int(x[:2])
                ok_games.append(i)

                if n > max(red, green, blue):
                    print(i)
                    ok_games.remove(i)
                    break

    return set(ok_games)


def main():
    print(solution_one())


if __name__ == '__main__':
    main()