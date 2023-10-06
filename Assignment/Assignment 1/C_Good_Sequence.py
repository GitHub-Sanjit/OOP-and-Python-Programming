n=int(input())
lst=list(map(int, input().split()))
dect = {}
res = 0

for i,value in enumerate(lst):
    if value not in dect.keys():
        dect[value] = 0
    dect[value] += 1
    
for key, value in dect.items():
    if value < key:
        res += value
    else:
        res += value - key
        
print(res)