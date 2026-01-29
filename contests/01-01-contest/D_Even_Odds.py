n,k = map(int,input().split(" "))
odds = ""
evens = ""
# Brute force soln
for num in range(1,n+1):
    if num % 2 ==0:
        evens +=str(num)
    else:
        odds +=str(num)

final_out = odds+evens
print(final_out[k-1])

# optimized solution

