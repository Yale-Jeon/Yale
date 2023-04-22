def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return None

# 문자열로 된 연산식 입력 받기
exp = input("연산식을 입력하세요: ")

# 연산자 우선순위 설정
precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0}

# 스택 초기화
operands = []
operators = []

# 문자열 분리하기
tokens = exp.split()

# 각 토큰을 순회하며 스택에 push
for token in tokens:
    if token.isdigit():
        operands.append(float(token))
    elif token in precedence.keys():
        if token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                op = operators.pop()
                num2 = operands.pop()
                num1 = operands.pop()
                result = calculate(num1, num2, op)
                operands.append(result)
            operators.pop()  # '('를 제거
        else:
            while operators and precedence[operators[-1]] >= precedence[token]:
                op = operators.pop()
                num2 = operands.pop()
                num1 = operands.pop()
                result = calculate(num1, num2, op)
                operands.append(result)
            operators.append(token)

# 남은 연산자들을 계산
while operators:
    op = operators.pop()
    num2 = operands.pop()
    num1 = operands.pop()
    result = calculate(num1, num2, op)
    operands.append(result)

# 결과 출력
print("결과:", operands[0])