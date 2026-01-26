t = int(input())
def expression(n):
    for i in range(n):
        num1,num2 = map(int,input().split("+"))
        print(num1+num2)

expression(t)
