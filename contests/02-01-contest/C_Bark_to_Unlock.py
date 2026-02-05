password = input()
words_count = int(input())

# the string only form when either l+f of each word 

word = ""
first_letters = []
last_letters = []
for _ in range(words_count):
    f,l= input()
    first_letters.append(f)
    last_letters.append(l)

for f,l in zip(first_letters,last_letters):
    if f+l == password or l+f == password:
        # print("YES")
        print(f+l,"yes")
        print(l+f,"yes")
    else:
        print(f+l,"no")
        print(l+f,"no")
# print(word)
# if password in word:
#     print("YES")
# else:
#     print("NO")
DesiciveBytes


