n = int(input('Введите длину шоколадки: '))
m = int(input('Введите ширину школоладки: '))
k = int(input('Введите количество долек, которое хотите отломать: '))
if k < m * n and (k % m == 0 or k % n == 0):
    print('YES')
else:
    print('NO')