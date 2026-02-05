n = int(input())
cards =list(map(int,input().split(" ")))

# ===================  Naive approach ==============

sereja_count = 0
dima_count = 0
counter = 0
while counter<=n:
    if cards:
        score = max(cards[0],cards[-1])
        # print(score)
        cards.remove(score)
        if counter %2 ==0:
            dima_count+=score
        else:
            sereja_count+=score
    counter +=1
        
print(dima_count,sereja_count)

#=================== optmized approach ==================

sereja,dima = 0,0
left,right = 0,len(cards)-1
turn = 0

while left<=right:
    if cards[left]> cards[right]:
        score = cards[left]
        left +=1
    else:
        score = cards[right]
        right -=1
    
    if turn%2 == 0:
        sereja += score
    else:
        dima += score 

    turn +=1
print(sereja,dima)



