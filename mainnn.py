n = int(input())
result = [ 'чётное' if i % 2 == 0 else 'нечётное' for i in range(1,n+1)]
print(result)