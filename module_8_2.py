def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            if isinstance(item, str) and len(item.strip()) > 0:
                raise ValueError
            result += float(item)
        except (ValueError, TypeError):
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1

    return result, incorrect_data

def calculate_average(numbers):
    try:
        if isinstance(numbers, str):
            numbers = list(numbers)

        if not hasattr(numbers, '__iter__'):
            raise TypeError

        total_sum, incorrect_data_count = personal_sum(numbers)
        count_of_numbers = len(numbers) - incorrect_data_count

        if count_of_numbers == 0:
            raise ZeroDivisionError

        return total_sum / count_of_numbers

    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')