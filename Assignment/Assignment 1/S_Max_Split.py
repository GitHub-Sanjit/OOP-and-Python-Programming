s = str(input())
left, right = 0, 0
lst = []

for i in s:
    if i == "L":
        left += 1
    else:
        right += 1
    if left == right:
        lst.append(s[: left + right])
        s = s[left + right :]
        left, right = 0, 0

print(len(lst))
for i in lst:
    print(i)
