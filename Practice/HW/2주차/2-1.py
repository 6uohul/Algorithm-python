# 후위 표기법(postfix notation)은 연산자가 피연산자 뒤에 오는 수식 표현 방식입니다.
# 이 문제에서는 주어진 후위 표기법 수식을 계산하는 프로그램을 작성해야 합니다

def evaluate_postfix(expression):
    stack = []

    for s in expression.split():
        if s.isdigit():
            stack.append(int(s))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if s == '+':
                result = operand1 + operand2
            elif s == '-':
                result = operand1 - operand2
            elif s == '*':
                result = operand1 * operand2
            elif s == '/':
                result = operand1 / operand2

            stack.append(int(result))

    return stack.pop()

# 테스트
expression = "4 2 / 3 - 2 *"
result = evaluate_postfix(expression)
print(result)