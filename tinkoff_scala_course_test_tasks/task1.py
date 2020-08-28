def collatz(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

def get_collatz(a):
    i=0
    while a!=1:
        # print(a, end=', ')
        a=collatz(a)
        i+=1
    return i


def interval_sum():
    e = input()
    a,b = (int(i) for i in e.split())
    x = 0
    for i in range(a,b+1):
        x+=get_collatz(i)
    print(x)
    return x

interval_sum()
# print(interval_sum(2,5))