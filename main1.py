n = abs(int(input('Введите количество элементов: ')))
Ai = input("Введите целые числа: ").split()
A= list(map(int, Ai)) 
X = int(input('Введите число X: '))
min = abs(X - A[0])
index = 0
for i in range(1, n):
    count = abs(X - A[i])
    if count < min:
        min = count
        index = i
print(f'Число {A[index]} близкок числу {X}')