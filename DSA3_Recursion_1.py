#Recursion 1
        #Print a Name n times
        #Print 1 to N
        #Print N to 1


#Print a Name n times
def printN(n):
    #Way1
    if n==0:
        return
    print("Your Name")
    printN(n-1)

def  printN1(i,n):
    if i>n:
        return
    print("Your Name")
    printN1(i+1,n)


  #Print 1 to N
def printToN(i,n):
      if i>n:
          return
      print(i)
      printToN(i+1,n)


#Print N to 1
def printNToO(n):
    if n==0:
        return
    print(n)
    printNToO(n-1)

