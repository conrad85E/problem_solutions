def is_invalid(num: int) -> bool:
    '''
    Returns True if passed number is an invalid ID.
    An ID is invalid if it consists of repeating numbers.
    (Ex. 555 | 12121212 | 364364364364 are invalid)
    
    :param num: A number to check the validity
    :type num: int
    :return: True if num is invalid | False otherwise
    :rtype: bool
    '''
    if num < 11:
        return False
    
    num_str = str(num)
    num_len = len(num_str)

    for i in range(1, num_len // 2 + 1):
        if num_str == num_str[-i:] * (num_len // i):
            return True
    
    return False

def find_invalid_ids_sum(range: list[str, str]) -> int:
    '''
    Finds all invalid IDs in passed range.
    (Brute force)
    
    :param range: Range to check for invalid IDs
    :type range: list[str, str]
    :return: Sum of all invalid IDs found in the passed range
    :rtype: int
    '''
    start_str, end_str = range
    start_int, end_int = int(start_str), int(end_str)
    invalid_ids_sum = 0

    while end_int >= start_int:
        if is_invalid(start_int):
            invalid_ids_sum += start_int
        start_int += 1
    
    return invalid_ids_sum

def main():
    invalid_ids_sum = 0
    with open("D2_input.txt", "r") as f:
        ranges = [tuple(range.split("-")) for range in f.read().split(",")]
        for range in ranges:
            invalid_ids_sum += find_invalid_ids_sum(range)
    print(invalid_ids_sum)

if __name__ == "__main__":
    main()