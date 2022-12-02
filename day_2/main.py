
from typing import List

# I think that this could be handled as a circular vector, but wasnt worth the time & effort

# Part 1
def determine_result_match(op: str, me: str, abc: List[str], xyz: List[str]) -> int:
    if abc.index(op) == xyz.index(me):
        return 3
    match op:
        case 'A':
            if me == 'Y':
                return 6
            else: return 0
        case 'B':
            if me == 'Z':
                return 6
            else: return 0
        case 'C':
            if me == 'X':
                return 6
            else: return 0

def find_score(opp: List[str], mine: List[str]):
    with open("input.txt") as f:
        input = f.read()
    matches = input.split('\n')

    outcomes = 0

    for match in matches:
        values = match.split(' ')
        outcomes += mine.index(values[1]) +1 + determine_result_match(op=values[0],me=values[1], abc=opp, xyz=mine)

    return outcomes

    
# Part 2
def find_what_to_play(opp: str, out: str) -> str:
    match out:
        case 'X': # lose
            match opp:
                case 'A':
                    return 'Z'
                case 'B':
                    return 'X'
                case 'C':
                    return 'Y'
        case 'Y': # draw
            match opp:
                case 'A':
                    return 'X'
                case 'B':
                    return 'Y'
                case 'C':
                    return 'Z'
        case 'Z': # win
            match opp:
                case 'A':
                    return 'Y'
                case 'B':
                    return 'Z'
                case 'C':
                    return 'X'

def find_actual_score(opp: List[str], out: List[str]):
    with open("input.txt") as f:
        input = f.read()
    matches = input.split('\n')

    outcomes = 0

    for match in matches:
        values = match.split(' ')
        outcomes += out.index(values[1])*3 + out.index(find_what_to_play(opp=values[0], out=values[1]))+1

    return outcomes


if __name__ == "__main__":
    opponent = ['A', 'B', 'C']
    mine = ['X', 'Y', 'Z']

    print("my total score is ", find_score(opp=opponent, mine=mine))

    print("my total score according to strategy is ", find_actual_score(opp=opponent, out=mine))