# 4) Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1


list_1 = [1, 2, 3, 4, 5]
list_1.append(list_1.pop(0))
print(list_1)