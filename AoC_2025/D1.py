def rotate(direction: str, steps: int, start: int) -> tuple[int, int]:
    '''
    Performs one move
    
    :param direction: Direction of rotation ("L" or "R").
    :type direction: str
    :param steps: Number of clicks in a given rotation.
    :type steps: int
    :param start: Starting position before the rotation.
    :type start: int
    :return: Tuple of a [new position] and [number of passes of 0 mark] during the rotation.
    :rtype: tuple[int, int]
    '''
    dial_length = 100       # number of digits on the dial
    end_position = 0        # end position after one turn
    zeros_passed = 0        # num of zeros passed in a turn

    if direction == "R":
        end_position = (start + steps) % dial_length
        zeros_passed = (start + steps) // dial_length
        
    elif direction == "L":
        end_position = (start - steps) % dial_length

        if steps == start:
            if start != 0:
                zeros_passed = 1
        elif steps > start:
            if start == 0:
                zeros_passed = steps // dial_length
            else:
                zeros_passed = (steps - start) // dial_length + 1
        elif steps < start:
            zeros_passed = 0
    
    return end_position, zeros_passed

curr_position = 50
zeros_passed_total = 0

with open("D1_input.txt", "r") as file:
    for line in file:
        turn = line.strip()

        direction = turn[0]     # "L" or "R"
        steps = int(turn[1:])   # amount of steps

        if direction not in "LR":
            raise ValueError("The 'direction' must be 'L' or 'R'")
        next_position, zeros_passed = rotate(direction, steps, curr_position)
        zeros_passed_total += zeros_passed
        curr_position = next_position

print(zeros_passed_total)