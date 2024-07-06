#Recursion 2
    #1_Sum of first n numbers
    #2_Factorial of number n

#1_Sum of first n numbers
def SumN(i,n,Sm):
    if i>n:
        return Sm
    return SumN(i+1,n,Sm+i)

#2_Factorial of number n
def fact_1(i,n):
    #Way 1
    if i>n:
        return 1
    return i*fact_1(i+1,n)

def fact_2(n):
    #Way 2
    if n==1:
        return 1
    return n*fact_2(n-1)



