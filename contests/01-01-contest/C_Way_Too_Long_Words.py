n = int(input())
# Loop for each word
# if not greater print it if 
# take first and last and slice the world

for _ in range(n):
    word = input()
    if len(word)<=10:
        print(word)
    else:
        first_letter = word[0]
        last_letter = word[-1]
        abbreviation = len(word[1:-1])
        word = first_letter+str(abbreviation)+last_letter
        print(word)
