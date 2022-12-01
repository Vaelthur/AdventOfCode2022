# imports
from typing import List

# functions
def find_max_amount()-> int:
    '''
    Given the input file find the max amount of calories carried by a single elf.
    '''
    sum_items: List[int]= []

    with open("input.txt") as f:
        input = f.read()
    
    # list of str with the calories inside of each bag
    elves = input.split('\n\n')

    for bag in elves:
        # list of items inside each bag
        items = bag.split('\n')
        buffer = 0
        # iterate over items & sum
        for item in items:
            buffer += int(item)
        sum_items.append(buffer)

    return max(sum_items)

def find_top3_sum_amount() -> int:
    '''
    Given the input file find the total amount of calories carried by the top 3 carrying elves.
    '''
    sum_items: List[int]= []

    with open("input.txt") as f:
        input = f.read()
    
    elves = input.split('\n\n')

    for bag in elves:
        items = bag.split('\n')
        buffer = 0
        for item in items:
            buffer += int(item)
        sum_items.append(buffer)

    top3 = 0
    for i in range(0,3):
        idx = sum_items.index(max(sum_items))
        top3 += sum_items.pop(idx)

    return top3



if __name__ == '__main__':
    largest = find_max_amount()
    top3 = find_top3_sum_amount()

    print("Largest amount of calories is ", largest)
    print("top3 amount sum is ", top3)