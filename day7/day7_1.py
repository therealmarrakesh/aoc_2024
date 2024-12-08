from itertools import product

equations = []

with open("day7_input.txt") as f:
    for line in f:
        test_value, operands = line.strip().split(":")
        test_value = int(test_value)
        operands = tuple(map(int, operands.strip().split()))
        equation = (test_value, operands)
        equations.append(equation)


def test_combinations(equation):
    test_value = equation[0]
    operands = equation[1]
    
    # Switch comment to support only add and mul
    #op_combos = product((0, 1), repeat=len(operands) - 1)
    op_combos = product((0, 1, 2), repeat=len(operands) - 1)

    for operators in op_combos:
        total = operands[0]
        for i, operator in enumerate(operators):
            if operator == 0:
                total += operands[i + 1]
            elif operator == 1:
                total *= operands[i + 1]
            else:
                total = int(str(total) + str(operands[i + 1]))

        if total == test_value:
            return test_value
    return 0


def add_results(equations):
    result_total = 0
    for equation in equations:
        result_total += test_combinations(equation)
    return result_total

print(f"Total calibration result:", add_results(equations))
