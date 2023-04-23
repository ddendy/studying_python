n = int(input('Факториал какого числа нужно посчитать?'))
count = 1
fact = 1
while count <= n:
    fact = fact * count
    count += 1
print(fact)
