def personal_sum(*numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        for j in range(len(i)):
            try:
                result += i[j]
            except TypeError:
                print(f'Некорректный тип данных для подсчёта суммы - {i[j]}')
                incorrect_data += 1
    return (result, incorrect_data)

def calculate_average(*numbers):
    try:
        summ_all = personal_sum(*numbers)
        summ_ = summ_all[0]
        in_data_ = summ_all[1]

        result = summ_ / (len(*numbers)-in_data_)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None
    else:
        return result


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать