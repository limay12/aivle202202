def divisor(n):
    num=0
    for i in range(1, n+1):
        if n % i == 0: num += 1
    return num

def solution(left, right): 
    sum=0
    for i in range(left, right+1):
        if divisor(i) % 2 == 0:
            sum += i
        else: sum -=i
    return sum