def binary_search(my_list, item):
    low_my_list = 0  # нажний порог поиска
    height_my_list = len(my_list) - 1  # верхний порог, длинна списка минус 1
    while low_my_list < height_my_list:  # пока верно условие выполнять >
        mid = int((low_my_list + height_my_list) / 2)  # делим весь список на 2 (Бинарный поиск)
        answer = my_list[mid]  # ответ равен значению под индексом равным mid
        if mid == item:  # если mid == item
            return answer  # выводить ответ == answer
        if mid > item:  # если середина списка > чем item
            height_my_list = mid - 1  # конец списка равен середина списка - 1
        else:
            low_my_list = mid + 1  # если середина списка < чем item то начало списка равено середина списка + 1
    return None


test_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z"]

print(binary_search(test_list, 6))

