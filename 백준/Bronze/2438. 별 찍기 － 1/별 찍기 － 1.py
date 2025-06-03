n = int(input())
result = ""

for i in range(1, n + 1):
    result += "*" * i
    if i != n:
        result += "\n"

print(result)

