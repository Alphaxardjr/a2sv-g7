t = int(input())
for _ in range(t):
    n = int(input())
    s= input()
    s_arr = [int(i) for i in s]
    pal_s = s_arr[:-1]
    # pal_s = [s_arr[i] for i in range(len(s_arr)-1,0,-1)]
    # print(pal_s)
    print("yes") if s_arr == pal_s else print("No")