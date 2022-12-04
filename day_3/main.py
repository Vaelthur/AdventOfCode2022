import string
from typing import List

# Part 1
def get_shared_letter(items: str) -> str:

    first = items[:len(items)//2]
    second = items[len(items)//2:]

    for i in first:
        if i in second:
            return i


def get_priority_amount(lower: List[str], upper: List[str]) -> int:

    with open('input.txt') as f:
        backpacks = f.readlines()

    amount = 0

    for back in backpacks:
        letter = get_shared_letter(back)
        if letter.islower():
            amount+=lower.index(letter)+1
        else:
            amount+=26+upper.index(letter)+1

    return amount

# Part 2
def find_badge_letter(a: str, b: str, c: str) -> str:
    for l in a:
        if l in b and l in c:
            return l

    
def get_badge_priority(lower: List[str], upper: List[str]) -> int:

    with open("input.txt") as f:
        backpacks = f.readlines()

    priority = 0

    for i in range(2, len(backpacks),3):
        badge = find_badge_letter(backpacks[i], backpacks[i-1], backpacks[i-2])

        if badge.islower():
            priority += lower.index(badge)+1
        else: 
            priority += 26+upper.index(badge)+1
        
    return priority



if __name__ == '__main__':
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)

    print("Priority amount is ", get_priority_amount(lower=lower, upper=upper))
    print("badge priority amount is ", get_badge_priority(lower=lower, upper=upper))
