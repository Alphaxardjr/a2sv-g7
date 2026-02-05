rounds = int(input())
is_not_dead = True

for round in range(rounds):
    monsters, bullets =map(int,input().split(" "))
    monster_health = list(map(int,input().split(" ")))
    monster_position = list(map(int,input().split(" ")))

    while(is_not_dead):
        
