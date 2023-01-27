from csv import list_dialects
from re import A
import sys
from collections import Counter
sys.stdin = open("./stack.txt","r")

a = list(map(int,(input().split())))
print(a)
# 소수판별하는 함수
def bk(k):
    # k가 음수이거나 1일떄
    if k <= 0 or k == 1 or k == 4 :
        return 'F'
    # k가 2일 때
    elif k == 2 or k == 3 :
        return 'T'
    # k가 2보다 클 때
    elif k > 100 :
        for i in range(2,k-1):
            if k % i == 0:
                return 'F'

            # else: 
            # 처음엔 여기 else 넣고 return 을 받았음
            # for문이 다 돌고나서 return T를 받아야하는게 맞음
        return 'T'
sum = 0
for i in range(a[0], a[1]+1):
    if bk(i) == 'T':
        print(i)

    else:
        pass