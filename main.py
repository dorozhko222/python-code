n = input()
list = []
list.append(n)
result = [5 if len(i) > 5 else len(i) for i in list]
print(result)