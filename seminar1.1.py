import math

n = int(input('Сколько километров машина проезжает за день? '))
m = int(input('Сколько километров нужно проехать? '))
days = math.ceil(m / n)
print(days)