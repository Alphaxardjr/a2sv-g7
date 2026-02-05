user_name = input()
# ========== naive approach ===========
# def remove_duplicate(string):
#     uname = []
#     for char in string:
#         if char not in uname:
#             uname.append(char)
#     return len(uname)

# if remove_duplicate(user_name) %2 ==0:
#     print("CHAT WITH HER!")
    
# else:
#     print("IGNORE HIM!")

# =========== optmized approach ==========

if len(set(user_name)) %2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
