# 4) Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.

N = int(input('enter the number N: '))
sum = 0
for i in range(1, N + 1):
    sum += 1 / i
print(sum)