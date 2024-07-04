#Sieve Of Eratosthesis
            #1_Prime or not Prime
            #2_Given a series of number ritn it is prime or not


# 1_Prime or not Prime
def isPrime(num):
    i=2
    while i*i<=num:
        if num%i==0:
            return False
    return True


#2_Given a series of number ritn it is prime or not
series=list(map(int,input().split()))

k=20
primes=[1]*(k+1)
primes[0]=primes[1]=0

for i in range(2,k+1):
    if isPrime(0):
        primes[i]=1
    else:
        primes[i]=0
print(primes)

for i in range(2,k+1):
    if primes[i]==1:
        j=i*i
        while j<=k:
            primes[j]=0
            j=j+1

print(primes)