#기본수학2

#1929_소수구하기(에라토스테네스의 체)

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

m, n = map(int, input().split())

for i in range(m, n+1):
    if isPrime(i) == True:
        print(i)


#4948_베르트랑 공준_첫시도(시간초과)

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

while True:
    n = int(input())
    result = 0
    if n == 0:
        break
    else:
        for i in range(n+1, 2*n+1):
            if isPrime(i) == True:
                result+=1
        print(result)


#4948_베르트랑 공준_두번째시도(성공)
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

number = list(range(2,246912))
prime = []
for i in number:
    if isPrime(i) == True:
        prime.append(i)

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    else:
        for i in prime:
            if n < i <= 2*n:
                cnt+=1
        print(cnt)


#9020_골드바흐의 추측_첫시도(시간초과)
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

t = int(input())
for i in range(t):
    n = int(input())
    prime = []
    gold = []
    minus = []
    for i in range(2,n):
        if isPrime(i) == True:
            prime.append(i)
    for i in prime:
        for j in prime:
            if i+j == n:
                gold.append([i,j])
                minus.append(abs(j-i))
    print(gold[minus.index(min(minus))][0],gold[minus.index(min(minus))][1])
