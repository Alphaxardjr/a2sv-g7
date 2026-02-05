s_length = int(input())
word = input().lower()

letters = set(word)
if len(letters)>=26:
    print("YES")
else:
    print("NO")
# lating_char = {
#     "a":"a",
#     "b":"b",
#     "c":"c",
#     "d":"d",
#     "e":"e",
#     "f":"f",
#     "g":"g",
#     "h":"h",
#     "i":"i",
#     "j":"j",
#     "k":"k",
#     "l":"l",
#     "m":"m",
#     "n":"n",
#     "o":"o",
#     "p":"p",
#     "q":"q",
#     "r":"r",
#     "s":"s",
#     "t":"t",
#     "u":"u",
#     "v":"v",
#     "w":"w",
#     "x":"x",
#     "y":"y",
#     "z":"z"
# }



# def pangram(word):
#     words = {}
#     for char in word:
#         if char.lower() not in lating_char:
#             words[char]= char
    
#     return len(words)>=26
# if pangram(word):
#     print("YES")
# else:
#     print("NO")


