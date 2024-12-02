class RootCalculator:
    def __init__(self, root_degree, precision=2):
        self.__root_degree = root_degree  # Приватный атрибут
        self.__precision = precision      # Приватный атрибут

    def __call__(self, number):
        return round(pow(number, 1 / self.__root_degree), self.__precision)

    # Геттер для root_degree (опционально)
    def get_root_degree(self):
        return self.__root_degree

    # Сеттер для root_degree (опционально)
    def set_root_degree(self, value):
        if value > 0:
            self.__root_degree = value
        else:
            raise ValueError("Root degree must be greater than 0.")

    # Геттер для precision (опционально)
    def get_precision(self):
        return self.__precision

    # Сеттер для precision (опционально)
    def set_precision(self, value):
        if value >= 0:
            self.__precision = value
        else:
            raise ValueError("Precision must be a non-negative number.")
