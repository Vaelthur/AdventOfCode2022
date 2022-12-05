# Part 1
def is_contained(first: str, second: str) -> bool:
    start_1 = int(first.split("-")[0])
    end_1 = int(first.split("-")[1])
    start_2 = int(second.split("-")[0])
    end_2 = int(second.split("-")[1])

    if (start_1 <= start_2 and end_1 >= end_2) or (start_2 <= start_1 and end_2 >= end_1):
        return True
    else: 
        return False


def get_number_contained_zones() -> int:

    with open("input.txt") as f:
        pairs = f.readlines()

    amount = 0
    for pair in pairs:
        if is_contained(first=pair.split(",")[0], second=pair.split(",")[1]):
            amount+=1
    return amount


# Part 2
def is_overlapped(first: str, second: str) -> bool:
    start_1 = int(first.split("-")[0])
    end_1 = int(first.split("-")[1])
    start_2 = int(second.split("-")[0])
    end_2 = int(second.split("-")[1])

    for i in range(start_1, end_1+1):
        if i in range(start_2, end_2+1):
            return True
        

    return False



def get_number_overlapped_zones() -> int:
    
    with open("input.txt") as f:
        pairs = f.readlines()

    amount = 0

    for pair in pairs:
        if is_overlapped(first=pair.split(",")[0], second=pair.split(",")[1]):
            amount+=1
    
    return amount


if __name__ == "__main__":
    print("number of contained pairs is ", get_number_contained_zones())
    print("number of overlapped pairs is ", get_number_overlapped_zones())