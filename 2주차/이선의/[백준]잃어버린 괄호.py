'''
+, -, ()만으로 식 만들고 괄호 삭제
괄호를 적절히 쳐서 이 식의 값을 최소로
'''

exp = input()
terms = exp.split("-")

ans = 0

if exp[0] != "-":
    numbers = terms[0].split("+")
    numbers_sum = 0
    for n in numbers:
        numbers_sum += int(n)
    ans += numbers_sum
else:
    ans -= int(terms[1])
    terms = terms[1:]

for i in range(1, len(terms)):
    numbers = terms[i].split("+")
    numbers_sum = 0
    for n in numbers:
        numbers_sum += int(n)
    ans -= numbers_sum

print(ans)