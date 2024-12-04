# "Создание исключений"
# "Некорректность"


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):                                        # проверка vin-номера
            self.__vin = vin
        if self.__is_valid_numbers(numbers):                                # проверка номера машины
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) == False:                            # vin-номер не целочисленный
            raise IncorrectVinNumber(f'Некорректный тип vin номера {vin_number}')
        elif 1000000 > vin_number or vin_number > 9999999 == True:          # Неверный диапазон vin-номера
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера {vin_number}')
        return True

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) == False:                               # номер машины не строка
            raise IncorrectVinNumber(f'Некорректный тип данных для номеров {numbers}')
        elif len(numbers) != 6:                                             # Неверная длина номера
            raise IncorrectVinNumber(f'Неверная длина номера {numbers}')
        return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message



try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

try:
    fourth = Car('Model4', 202020202, 222525)
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{fourth.model} успешно создан')

try:
    fifth = Car('Model5', '202020505', '123456')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{fifth.model} успешно создан')
