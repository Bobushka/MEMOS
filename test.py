# найти сумму чисел от 1 до n
n = int(input('n = '))
print(n)
summ = 0
while n:
    summ = summ + n
    n -= 1
print(summ)
