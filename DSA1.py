# Basic Math Problem
            # Count Digits In numbers
            # Reverse a number
            # Pallindrome
            # GCD or HCF
            # Armstrong
            # Print all divisor
            # Check for prime
import math


# Count Digits In numbers
def countNumbers(num):
    #way 1
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

def countNumbers2(num):
    #way2
    return math.floor(math.log(num))+1

 # Reverse a number
def reverseNumber(num):
    ans=0
    while num>0:
        rem=num%10
        ans=ans*10+rem
        num=num//10
    return ans

 # Pallindrome
def pallindrome(num):
    return reverseNumber(num)==num

  # GCD or HCF
def GCD(a,b):
    divisor=min(a,b)
    dividend=max(a,b)
    while dividend%divisor!=0:
        temp=dividend
        dividend=divisor
        divisor=temp%divisor
    return divisor


 # Armstrong
def armstrong(num):
    ans=0
    temp=num
    k=countNumbers(num)
    while num>0:
        rem=num%10
        ans=ans+rem**k
        num=num//10
    return temp==ans


# Print all divisor
def numDivisor(num):
    #way1
    for i in range(1,num+1):
        if num%i==0:
            print(i)

def numDivisor2(num):
    #way2
    k=1
    while k*k<=num:
        if num%k==0:
            print(k)
            if k!=(num//k):
                print(num//k)
        k+=1


# Check for prime
def isPrime(num):
    #Way 1
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def isPrime2(num):
    #way2
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i+=1
    return True

num = int(input())
ans=isPrime2(num)
print(ans)