import sys

def to_string(num_history, op_history):
    "Build a string from the buffer of number and operator"

    s = bracket_history[2] + bracket_history[0] + str(num_history[0]) + ' ' + op_history[0] + ' ' + str(num_history[1]) + bracket_history[1] + ' ' + op_history[1] + ' ' + str(num_history[2]) + bracket_history[3] + ' ' + op_history[2] + ' ' + str(num_history[3]) 
    return s

def greedy(num1, num2):
    "Input 2 operand. Finds the operator that gives local maximum score and returns the local maximum score."

    global global_op

    add_result = num1 + num2
    add_score = score(add_result, '+')

    min_result = num1 - num2
    min_score = score(min_result, '-')

    mul_result = num1 * num2
    mul_score = score(mul_result, '*')

    div_score = -9999 # assigned for used in local_score
    div_result = -9999 # assigned for used in local_score

    if (num2 != 0):
        div_result = num1 / num2
        div_score = score(div_result, '/')

    local_score = max(add_score, min_score, mul_score, div_score)

    if (local_score == add_score):
        global_op = '+'
        return add_result

    elif (local_score == min_score):
        global_op = '-'
        return min_result

    elif (local_score == mul_score):
        global_op = '*'
        return mul_result

    elif (local_score == div_score):
        global_op = '/'
        return div_result

    else:
        print("Magic Error")
        return

def op_prior(op):
    "Returns the priority of operator"
    if op == '+' or op == '-':
        return 0

    elif op == '*' or op == '/':
        return 1

    else:
        print('Illegal Argument')
        return

def op_value(op):
    "Returns the value of operator affection to score"
    if op == '+':
        return 5

    elif op == '-':
        return 4

    elif op == '*':
        return 3

    elif op == '/':
        return 2

    else:
        print('Illegal Argument')
        return

def score(result, op):
    "Returns the score from a result and an operator"
    diff = abs(result - 24)

    if (len(op_history) == 0):
        score = op_value(op) - diff
        return score

    else:
        prev_op = op_history[len(op_history) - 1]

        if (op_prior(op) > op_prior(prev_op)):
            score = op_value(op) - diff - 1

        else:
            score = op_value(op) - diff

        return score

def score_final(result):
    "Returns final score of a complete equation."
    diff = abs(result - target)

    op_vals = 0
    for op in op_history:
        op_vals += op_value(op)

    return op_vals - diff - charge

target = 24 # verge
op_history = [] # operator buffer of an equation
num_history = [] # number buffer of an equation
bracket_history = [] # bracket buffer of an equation
charge = 0 # penalty of using brackets

# Prompt input
numbers = []
while (len(numbers) < 4):
    st = input('--> ')
    for c in st.split():
        numbers.append(int(c))

# 1st node
result_1 = greedy(numbers[0], numbers[1])

op_history.append(global_op)
num_history.append(numbers[0])
num_history.append(numbers[1])

fork_1 = greedy(result_1, numbers[2])
fork_2 = greedy(result_1, numbers[3])

if (fork_1 > fork_2):
    result_1 = fork_1
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[2])

    result_1 = greedy(result_1, numbers[3])
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')
    
    op_history.append(global_op)
    num_history.append(numbers[3])
    
else:
    result_1 = fork_2
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[3])

    result_1 = greedy(result_1, numbers[2])
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[2])

score_1 = score_final(result_1)
str_1 = to_string(num_history, op_history)

op_history.clear() # reset operator history
num_history.clear() # reset number history
bracket_history.clear() # reset bracket history
charge = 0 # reset charge

# 2nd node
result_2 = greedy(numbers[0], numbers[2])

op_history.append(global_op)
num_history.append(numbers[0])
num_history.append(numbers[2])

fork_1 = greedy(result_2, numbers[1])
fork_2 = greedy(result_2, numbers[3])

if (fork_1 > fork_2):
    result_2 = fork_1
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[1])

    result_2 = greedy(result_2, numbers[3])
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[3])

else:
    result_2 = fork_2
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[3])

    result_2 = greedy(result_2, numbers[1])
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[1])

score_2 = score_final(result_2)
str_2 = to_string(num_history, op_history)

op_history.clear() # reset operator history
num_history.clear() # reset number history
bracket_history.clear() # reset bracket history
charge = 0 # reset charge

# 3rd node
result_3 = greedy(numbers[0], numbers[3])

op_history.append(global_op)
num_history.append(numbers[0])
num_history.append(numbers[3])

fork_1 = greedy(result_3, numbers[1])
fork_2 = greedy(result_3, numbers[2])

if (fork_1 > fork_2):
    result_3 = fork_1
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[1])

    result_3 = greedy(result_3, numbers[2])
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[2])

else:
    result_3 = fork_2
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[2])

    result_3 = greedy(result_3, numbers[1])
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[1])

score_3 = score_final(result_3)
str_3 = to_string(num_history, op_history)

op_history.clear() # reset operator history
num_history.clear() # reset number history
bracket_history.clear() # reset bracket history
charge = 0 # reset charge

# 4th node
result_4 = greedy(numbers[1], numbers[2])

op_history.append(global_op)
num_history.append(numbers[1])
num_history.append(numbers[2])

fork_1 = greedy(result_4, numbers[0])
fork_2 = greedy(result_4, numbers[3])

if (fork_1 > fork_2):
    result_4 = fork_1
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[0])

    result_4 = greedy(result_4, numbers[3])
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[3])

else:
    result_4 = fork_2
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[3])

    result_4 = greedy(result_4, numbers[0])
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[0])

score_4 = score_final(result_4)
str_4 = to_string(num_history, op_history)

op_history.clear() # reset operator history
num_history.clear() # reset number history
bracket_history.clear() # reset bracket history
charge = 0 # reset charge

# 5th node
result_5 = greedy(numbers[1], numbers[3])

op_history.append(global_op)
num_history.append(numbers[1])
num_history.append(numbers[3])

fork_1 = greedy(result_5, numbers[0])
fork_2 = greedy(result_5, numbers[2])

if (fork_1 > fork_2):
    result_5 = fork_1
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[0])

    result_5 = greedy(result_5, numbers[2])
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[2])

else:
    result_5 = fork_2
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[2])

    result_5 = greedy(result_5, numbers[0])
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[0])

score_5 = score_final(result_5)
str_5 = to_string(num_history, op_history)

op_history.clear() # reset operator history
num_history.clear() # reset number history
bracket_history.clear() # reset bracket history
charge = 0 # reset charge

# 6th node
result_6 = greedy(numbers[2], numbers[3])

op_history.append(global_op)
num_history.append(numbers[2])
num_history.append(numbers[3])

fork_1 = greedy(result_6, numbers[0])
fork_2 = greedy(result_6, numbers[1])

if (fork_1 > fork_2):
    result_6 = fork_1
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[0])

    result_6 = greedy(result_6, numbers[1])
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[1])

else:
    result_6 = fork_2
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[1])

    result_6 = greedy(result_6, numbers[0])
    if (op_prior(op_history[len(op_history)-1]) < op_prior(global_op)):
        bracket_history.append('(')
        bracket_history.append(')')
        charge += 1

    else:
        bracket_history.append('')
        bracket_history.append('')

    op_history.append(global_op)
    num_history.append(numbers[0])

score_6 = score_final(result_6)
str_6 = to_string(num_history, op_history)

op_history.clear() # reset operator history
num_history.clear() # reset number history
bracket_history.clear() # reset bracket history
charge = 0 # reset charge

# take max score from all local score
max_score = max(score_1, score_2, score_3, score_4, score_5, score_6)
if (max_score == score_1):
    print(str_1)
elif (max_score == score_2):
    print(str_2)
elif (max_score == score_3):
    print(str_3)
elif (max_score == score_4):
    print(str_4)
elif (max_score == score_5):
    print(str_5)
elif (max_score == score_6):
    print(str_6)
print('Score: ', max_score)
