def max_joltage(bank: str) -> int:
    '''
    Finds the biggest twelve digit number from a line of digits passed in.
    
    :param bank: Line of digits as a string.
    :type bank: str
    :return: The biggest twelve digit number from the bank.
    :rtype: int
    '''
    biggest_batteries = [float("-inf")] * 12
    num_biggest_batteries = len(biggest_batteries)
    bank_len = len(bank)


    for i in range(bank_len):
        curr_battery = int(bank[i])

        # "l" index denotes the approach of the end of the input digit line
        if (bank_len - i) >= num_biggest_batteries:
            l = 0
        else:
            l = num_biggest_batteries - (bank_len - i)
        
        for j in range(l, num_biggest_batteries):
            # Check if the current digit from input line is greater than current digit in the list of 12 biggest
            # Check always from the left
            if curr_battery > biggest_batteries[j]:
                # The first digit in the list of biggest that is less -> becomes the current digit from the input line
                biggest_batteries[j] = curr_battery
                # Everithing to the right of it resets
                biggest_batteries[j + 1:] = [float("-inf")] * (num_biggest_batteries - j - 1)
                break
    
    # Turn the list of biggest digits into a number
    final_joltage = 0
    for i in range(num_biggest_batteries):
        final_joltage += biggest_batteries[i] * (10 ** (num_biggest_batteries - i - 1))
    return final_joltage
    
def main():
    joltage_sum = 0
    with open("D3_input.txt", "r") as f:
        for line in f:
            bank = line.strip()
            bank_joltage = max_joltage(bank)
            joltage_sum += bank_joltage
    print(joltage_sum)

if __name__ == "__main__":
    main()