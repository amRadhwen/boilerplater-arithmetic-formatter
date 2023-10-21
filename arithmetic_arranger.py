# check problems number
def check_problems_number(problems):
    valid = True
    if len(problems) > 5:
        valid = False
    return valid


# These two functions can be merged in one function using regex as verification method !

# check if operation is valid (contains only one of the operators '+' or '-')
def check_operators(problems):
    valid = True
    for problem in problems:
        if "+" not in problem and "-" not in problem:
            valid = False
            return valid
    return valid

# check if operands are valid (contains only 4 digits)
# can be merged with check check_operands_isfourdigits

def check_operands_isdigits(problems):
    valid = True
    for problem in problems:
        left_operand = problem.split()[0]
        right_operand = problem.split()[2]
        if not left_operand.isdigit() or not right_operand.isdigit():
            valid = False
            return valid
    return valid

# check if operand is only four digits
# depends on check_operands_isdigits()
def check_operands_isfourdigits(problems):
    valid = True
    for problem in problems:
        left_operand = problem.split()[0]
        right_operand = problem.split()[2]
        if len(left_operand) > 4 or len(right_operand) > 4:
            valid = False
            return valid
    return valid

# calculate the result for each problem
# return a dict
# operation is the key and result is the value

def resolve_problems(problems):
    equations = {}
    for problem in problems:
        equations[problem] = str(eval(problem))
    return equations


# Equations display formatter

def equations_display_format(equations):
    arranged_problems = ""
    loperands = []
    roperands = []
    operators = []
    lengths = []
    # Extract loperators, roperatos operators and the longest operator value each one of them in a list
    for equation in equations.keys():
        # check for the longest operand
        loperand = equation.split()[0]
        roperand = equation.split()[2]
        operator = equation.split()[1]
        loperands.append(loperand)
        roperands.append(roperand)
        operators.append(operator)
        longest = max(loperand, roperand, key=len)
        lengths.append(len(longest))

    # print the loperands list
    for iterval in range(0, len(equations)):
        arranged_problems += ("{:>"+str(lengths[iterval]+2)+"}").format(
            loperands[iterval])+"    "

    # print a line break
    arranged_problems += "\n"

    # print roperands list when each element is preceded by the operator
    for iterval in range(0, len(equations)):
        arranged_problems += operators[iterval]+(
            "{:>"+str(lengths[iterval]+1)+"}").format(roperands[iterval]) + "    "

    # print another line break
    arranged_problems += "\n"

    # print the line of dashes
    for iterval1 in lengths:
        for iterval2 in range(0, iterval1+2):
            arranged_problems += "-"
        arranged_problems += "    "

    # again print another line break
    arranged_problems += "\n"

    # print the result of each equation
    for iterval in range(0, len(equations.values())):
        arranged_problems += ("{:>"+str(lengths[iterval]+2)+"}").format(list(equations.values())[iterval]) + "    "

    return arranged_problems


# arithmetic_arranger function

def arithmetic_arranger(problems):
    Error = ""
    if not check_problems_number(problems):
        Error += "Error: Too many problems.\n"
        
    if not check_operators(problems):
        Error += "Error: Operator must be '+' or '-'.\n"
        
    if not check_operands_isdigits(problems):
        Error += "Error: Numbers must only contain digits.\n"
    elif not check_operands_isfourdigits(problems):
            Error += "Error: Numbers cannot be more than four digits.\n"

    if len(Error) > 0:
        return Error
    else:
        arranged_problems = equations_display_format(resolve_problems(problems))
        return arranged_problems
