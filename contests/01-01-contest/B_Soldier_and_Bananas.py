# 3 = ist baba
# 17 = initial
# 4 = no of BaseExce
# Loop for every banna
# 1-3
# 2-6
# 3-9
# 4-12
# 30 -17
# == 13

k,n,w = map(int,input().split(" "))
total_money = 0
for i in range(1,w+1):
    total_money += i*k
    
if n>total_money:
    print(0)
else:
    print(total_money-n)




