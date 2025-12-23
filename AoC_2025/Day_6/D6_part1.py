import operator
from typing import Any

def solve_math_problem(operands: list[tuple], operators: list[tuple]) -> int:
    '''
    Calculates sum of operations between elements of a list of tuples applying corresponding operands from anohter tuple.
    
    :param operands: List of operands.
    :type operands: list[tuple]
    :param operators: List of operators to apply on operands.
    :type operators: list[tuple]
    :return: Description
    :rtype: int
    '''
    # Dictionary for matching arithmetic operations to their string symbols
    OPERATORS: dict[str, Any] = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '//': operator.floordiv,
        '%': operator.mod,
    }
    total_sum = 0
    # Put first operands and corresponding operator symbol into a tuple:
    for *curr_operands, curr_operator in zip(*operands, operators[0]):
        # Get the operation function that matches curr_operator symbol
        operation_func = OPERATORS[curr_operator]
        intermediate_result = None
        
        for operand in curr_operands:
            if intermediate_result is None:
                intermediate_result = operand
                continue
            else:
                intermediate_result = operation_func(intermediate_result, operand)
        total_sum += intermediate_result

    return total_sum

def main() -> int:
    with open("D6_input.txt", "r") as f:
        math_problem_operands: list[tuple] = []
        math_problem_operators: list[tuple] = []

        lines = iter(f)
        current_line = next(lines, None)
        while current_line is not None:
            next_line = next(lines, None)

            split_line = tuple(current_line.strip().split())
            
            # Check if number of operators and operands in all lines match
            if math_problem_operands and len(split_line) != len(math_problem_operands[0]):
                raise Exception("Number of math problem operands has to be the same!")
            
            # If last line -> does not convert into 'int'
            if next_line is None:
                math_problem_operators.append(tuple(split_line))
            else:
                try:
                    math_problem_operands.append(tuple(map(int, split_line)))
                except ValueError:  # Raises if any string values are non-convertible into 'int' type
                    print(f"All operands have to be numbers!")
            
            current_line = next_line
        

        math_problem_total_sum: int = solve_math_problem(math_problem_operands, math_problem_operators)
    return math_problem_total_sum

if __name__ == "__main__":
    print(main())