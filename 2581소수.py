from csv import list_dialects
from re import A
import sys
from collections import Counter
sys.stdin = open("./stack.txt","r")

a = int(input())
b = int(input())

# 소수판별하는 함수
def bk(k):
    # k가 음수이거나 1일떄
    if k <= 0 or k == 1:
        return 'F'
    # k가 2일 때
    elif k == 2 :
        return 'T'
    # k가 2보다 클 때
    elif k > 2 :  
        for i in range(2,k):
            if k % i == 0:
                return 'F'
            # else: 
            # 처음엔 여기 else 넣고 return 을 받았음
            # for문이 다 돌고나서 return T를 받아야하는게 맞음
        return 'T'
sum = 0
t_list = []
for i in range(a,b+1):
    if bk(i) == 'T':
        sum = sum + i
        t_list.append(i)

    else:
        pass

if len(t_list) == 0:
    print(-1)
else:
    print(sum)
    print(t_list[0])

