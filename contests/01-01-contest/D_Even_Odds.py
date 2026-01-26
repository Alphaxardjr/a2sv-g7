n,k = map(int,input().split(" "))
odds = ""
evens = ""

for num in range(1,n+1):
    if num % 2 ==0:
        evens +=str(num)
    else:
        odds +=str(num)

final_out = odds+evens
print(final_out[k-1])

5
1,2,3,4,5
