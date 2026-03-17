n = int(input())
cards = list(map(int,input().split()))
cards.sort(reverse=True)
sereja,dima = 0,0
for i,marks in enumerate(cards):
    if i%2 == 0:
        sereja += marks
    else:
        dima += marks
print(sereja,dima)