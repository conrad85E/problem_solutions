def is_invalid(num: int) -> bool:
    '''
    Returns True if passed number is an invalid ID.
    An ID is invalid if it consists of two repeating numbers
    (Ex. 55 | 1212 | 123123 are invalid)
    
    :param num: A number to check the validity
    :type num: int
    :return: True if num is invalid | False otherwise
    :rtype: bool
    '''
    num_str = str(num)
    num_len = len(num_str)
    if num_len % 2 == 0:
        first_half = num_str[:num_len // 2]
        second_half = num_str[num_len // 2:]
        if first_half == second_half:
            return True
    return False


def next_invalid_id(num: int) -> int:
    '''
    Returns the next invalid number that goes after a passed number.
    
    :param num: Current number
    :type num: int
    :return: The next invalid number that follows the input number.
    :rtype: int
    '''
    # Next invalid ID is constructed with half number
    next_inv_num_half_str = ""
    
    num_str = str(num)

    # An invalid ID has even number of digits
    if len(num_str) % 2 == 0:
        # Step 1: Divide number in halves
        curr_num_first_half_str = num_str[:len(num_str) // 2]
        curr_num_second_half_str = num_str[len(num_str) // 2:]
        curr_num_first_half_int, curr_num_second_half_int = int(curr_num_first_half_str), int(curr_num_second_half_str)
        # Step 2a: If left side greater, then make right side equal left side
        if curr_num_first_half_int > curr_num_second_half_int:
            next_inv_num_half_str = str(curr_num_first_half_int)
        # Step 2b: Otherwise add 1 to left side and make right side equal left side
        elif curr_num_first_half_int <= curr_num_second_half_int:
            next_inv_num_half_str = str(curr_num_first_half_int + 1)
    else:
        # If number has odd number of digits (ex. 95461)
        # Then next invalid number is 100100
        zeros = len(num_str) // 2
        next_inv_num_half_str = "1" + "0" * zeros
    
    next_inv_num = int(next_inv_num_half_str * 2)
    return next_inv_num


def find_invalid_ids_sum(range: list[str, str]) -> int:
    '''
    Finds all invalid IDs in passed range.
    
    :param range: Range to check for invalid IDs
    :type range: list[str, str]
    :return: Sum of all invalid IDs found in the passed range
    :rtype: int
    '''
    start_str, end_str = range
    start_int, end_int = int(start_str), int(end_str)
    curr_str, curr_int = start_str, start_int
    invalid_ids_sum = 0

    while end_int >= curr_int:
        if is_invalid(curr_int):
            invalid_ids_sum += curr_int
        curr_int = next_invalid_id(curr_int)
    
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