def max_joltage(bank: str) -> int:
    '''
    Finds the biggest two digit number comprised from line of digits passed in.
    
    :param bank: Line of digits as a string.
    :type bank: str
    :return: The biggest two digit number from the bank.
    :rtype: int
    '''
    first_battery = float("-inf")
    second_battery = float("-inf")

    for i in range(len(bank)):
        curr_battery = int(bank[i])
        if curr_battery > first_battery and i != (len(bank) - 1):
            first_battery = curr_battery
            second_battery = float("-inf")
        else:
            if curr_battery > second_battery:
                second_battery = curr_battery
    
    return first_battery * 10 + second_battery
    
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