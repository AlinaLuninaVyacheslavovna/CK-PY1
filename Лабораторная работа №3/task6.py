list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0
max_num = list_numbers[max_index]

for i, current_num in enumerate(list_numbers):
    if current_num >= max_num:
        max_num = current_num
        max_index = i

list_numbers[-1], list_numbers[max_index] = max_num, current_num

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
