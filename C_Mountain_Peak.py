# from collections import defaultdict
# t= int(input())
# for _ in range(t):
#     n = int(input())
#     h = list(map(int,input().split()))

#     # left = 0

#     # 4 6 1 2 5 3 [4,6,]
#     # 2 1 4 3     []
#     # l r       [2,4,3]
#     # [5 3 1 2 4] = [5,]
#     # h_map = set()
#     # res = []
#     # found = False
#     # for right in range(n):
#     #     r_found = False
#     #     if h[right] > h[left]:
#     #         r_found = True
#     #         res.append(left)
#     #         res.append(right)
#     #         while right < n:
#     #             if h[res[-1]] > h[right]:
#     #                 res.append(right)
#     #                 found = True
#     #                 break
#     #             right +=1
#     #     left +=1
#     # print(res)
#     # if len(res)==3:
#     #     print("YES")
#     #     x,y,z = res
#     #     print(x,y,z)
#     # else:
#     #     print('NO')
#     found = False
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if h[i]<h[j] and h[j] > h[k]:
#                     print("YES")
#                     print(i,j,k)
#                     found = True
#                     break
#         if found:
#             break
# if not found:
#     print("NO")


t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    found = False
    # Iterate through the array, checking triples in one pass
    for j in range(1, n-1):  # j is the middle element
        if h[j] > h[j-1] and h[j] > h[j+1]:
            print("YES")
            # Output indices in 1-based format (common in Codeforces)
            print(j, j+1, j+2)
            found = True
            break

    if not found:
        print("NO")

            