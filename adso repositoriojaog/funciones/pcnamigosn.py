def amigos(a,b):
    sma=0
    for i in range(1,a):
        if a%i==0:
            sma+=i
        return sma
    sum=0
    for j in range(1,b+1):
        if b%j==0:
            sum+=j
        return sum
def amg(a,b):
    sum=amigos(a,b)
print(amigos(220,284))







