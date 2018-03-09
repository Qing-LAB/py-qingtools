import random
from datetime import datetime


def generate_single_op_exp() -> str:
    oplist = (' + ', ' - ')
    num1 = random.randint(0, 20)
    num2 = random.randint(0, 10)
    op1 = random.randint(0, len(oplist) - 1)
    order = random.randint(0, 1)
    if order == 0:
        str1 = str(num1) + oplist[op1] + str(num2)
    else:
        str1 = str(num2) + oplist[op1] + str(num1)
    return str1


def generate_dual_op_exp() -> str:
    while True:
        oplist = (' + ', ' - ', ' - ', ' - ')
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        num3 = random.randint(0, 100)
        op1 = random.randint(0, len(oplist) - 1)
        op2 = random.randint(0, len(oplist) - 1)
        op3 = random.randint(0, 1)  # parenthesis
        if op3 == 0:
            str1 = '(' + str(num2) + oplist[op2] + str(num3) + ')'
            str2 = str(num1) + oplist[op1] + str1
        else:
            str1 = str(num1) + oplist[op1] + str(num2)
            str2 = str1 + oplist[op2] + str(num3)
        if eval(str1) >= 0 and eval(str2) >= 0:
            return str2
            # return str2


def check_answer(s, trial=1):
    flag = 0
    count = 0

    while count < trial and flag == 0:
        try:
            count += 1
            ans_str = input(s + ' = ? ')
            ans_num = int(ans_str)
            if ans_num == eval(s):
                print("Correct!")
                flag = 1
            else:
                if count < trial:
                    print(f'Wrong answer. Give another try!')
                else:
                    print(f'Wrong answer. No mor trials left. the correct answer is {str(eval(s))}')
        except ValueError:
            print('Invalid number!')

    return flag


if __name__ == '__main__':
    ans = []
    total_run = 10
    total_exp = 0
    trials_allowed = 2

    interactive = input('Interactive test? (Y/N)')
    if interactive[0] == 'y' or interactive[0] == 'Y':
        interactive = True
        print("OK! Let's get started'")
        print(f"For each calculation you have {str(trials_allowed)} allowed")
    else:
        interactive = False

    start = datetime.now()
    correct = 0

    for i in range(0, total_run):
        str_exp = generate_dual_op_exp()

        if interactive:
            correct += check_answer(str_exp, trials_allowed)
        else:
            print(str_exp + ' = __________')
            ans.insert(i, str_exp + " = " + str(eval(str_exp)))

        total_exp += 1

        str_exp = generate_single_op_exp()

        if interactive:
            correct += check_answer(str_exp, trials_allowed)
        else:
            print(str_exp + ' = __________')
            ans.insert(i, str_exp + " = " + str(eval(str_exp)))

        total_exp += 1

    end = datetime.now()

    if not interactive:
        print('\n\nanswers:')
        for i in range(0, total_exp):
            print(ans[i])
    else:
        print(f'You have answered {str(correct)} correctly out of {str(total_exp)} questions.')
        print(f'Total used time (hh:mm:ss) {str(end - start)}')
