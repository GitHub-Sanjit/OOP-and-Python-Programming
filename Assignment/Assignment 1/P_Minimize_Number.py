# n = int(input())
# arr=list(map(int,input().split()))
# flag=False
# for i in arr:
#     if i%2 !=0:
#         flag=True
#         break
# if flag:
#     print(0)
# else:
#     ans=0
#     while all(i%2==0 for i in arr):
#         for i in range(n):
#             arr[i]//=2
#         ans+=1
#     print(ans)


n = int(input())
lst = list(map(int, input().split()))
res = 0

while True:
    if any(i % 2 != 0 for i in lst):
        break
    for i in range(n):
        lst[i] //= 2
    res += 1
print(res)
