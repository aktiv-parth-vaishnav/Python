number=int(input("enter a number: "))
def armstrong(n):
    number=str(n)
    digit= len(number)
    sum=0

    for x in number:
       sum= sum+int(x) ** digit
    return sum

ans=armstrong(number)
if ans == number:
    print("yes")
else:
    print("no")


