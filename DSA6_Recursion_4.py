#Recursion 4
    #Check if a string is pallindrome or not
    #Fibonacci number

#Check if a string is pallindrome or not
string=input()
def ispal(s,e,string):
    if s>e:
        return True
    if string[s]!=string[e]:
        return False
    return ispal(s+1,e-1,string)

#Fibonacci number
def fibonacci(n):
    if n==1:
        return 1
    return n*fibonacci(n-1)




