import random
from datetime import datetime


def generate_num() -> str:
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


if __name__ == '__main__':
    ans = []
    total_exp = 20

    interactive = input('Interactive test? (Y/N)')
    if interactive[0] == 'y' or interactive[0] == 'Y':
        interactive = True
        print("OK! Let's get started'")
    else:
        interactive = False

    start = datetime.now()
    correct = 0
    for i in range(0, total_exp):
        strexp = generate_num()

        if interactive:
            inputcheck = True
            while inputcheck:
                try:
                    userans = input(strexp + ' = ? ')
                    usernum = int(userans)
                    if usernum == eval(strexp):
                        correct += 1
                    else:
                        print(f'error. the correct answer is {str(eval(strexp))}')
                    inputcheck = False
                except ValueError:
                    print('Invalid number!')

        else:
            print(strexp + ' = __________')
            ans.insert(i, strexp + " = " + str(eval(strexp)))
    end = datetime.now()

    if not interactive:
        print('\n\nanswers:')
        for i in range(0, total_exp):
            print(ans[i])
    else:
        print(f'You have answered {str(correct)} correctly out of {str(total_exp)} questions.')
        print(f'Total used time (hh:mm:ss) {str(end - start)}')
