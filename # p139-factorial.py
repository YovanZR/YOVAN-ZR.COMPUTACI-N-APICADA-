def factorial(n:int)->int:
    if n<0: return -1
    r=1
    for i in range(2,n+1):
        r*=i
    return r

n=int(input('Número: '))
res=factorial(n)
print(res)
