'''

'''

arr = list(input())
arr.sort()

ans = ""
total = 0

for a in arr:
    if a <= '9':
        total += int(a)
    else:
        ans += a

ans += str(total)
print(ans)