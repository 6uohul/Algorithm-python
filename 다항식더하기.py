# 프로그래머스 알고리즘 테스트 문제풀이
'''

다항식 더하기
[문제 설명]
한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다.
다항식을 계산할 때는 동류항끼리 계산해 정리합니다.
덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요.
같은 식이라면 가장 짧은 수식을 return 합니다.

'''

def solution(polynomial):
    polynomials = polynomial.strip().split(' + ')
    x_sum = 0
    int_sum = 0
    for i in range(0, len(polynomials)):
        if 'x' in polynomials[i]:
            if polynomials[i] == "x":
                x_sum += 1
            elif len(polynomials[i]) >= 2:
                num = int(polynomials[i][:-1])
                x_sum += num
        else:
            int_sum += int(polynomials[i])

    if x_sum == 0:
        result = "{0}".format(int_sum)
    elif x_sum == 1:
        result = "x + " + str(int_sum) if int_sum != 0 else "x"
    else:
        result = "{0}x + ".format(x_sum) + str(int_sum) if int_sum != 0 else "{0}x".format(x_sum)
    print(result)

solution("x + x + x")