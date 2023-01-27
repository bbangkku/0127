from csv import list_dialects
from re import A
import sys
from collections import Counter
sys.stdin = open("./stack.txt","r")

import math
a = int(input())
a_li = []
a_sor = sorted(a_li)

# a가 1이면 아무것도 출력하지않는다.
if a == 1:
    print('')
# a가 어떤 수의 제곱일 때 그 수를 출력


# a가 1이 아닐 때,
else:
# 범위를 줄이기위해 루트 a인 b 만듬 (소수점이기 때문에 올림해야함)
    b = math.ceil(a**0.5)
    for i in range(2, b+1):
    # a가 i로 나누어떨어지지 않을때까지
        while a % i == 0:
            if a % i == 0:
                # a_li에 추가하고 a를 i로 나누는 과정 반복
                a_li.append(i)
                a = a // i
    # a가 1이 아니라면 마지막 숫자 a를 추가
    if a != 1:
        a_li.append(a)
# 정렬하고 순서대로 출력
for j in range(len(a_li)):
    # if len(a_li) == 2 and a_li[0] == a_li[1] : 
    #     print(a_li[0])
    #     break
    # else:
        print(sorted(a_li)[j])



# print(sorted(a_li)) 
