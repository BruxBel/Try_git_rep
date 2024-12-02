class RootCalculator:
    def __init__(self, root_degree, precision=2):
        self.root_degree = root_degree
        self.precision = precision
        # Изменение: добавляем новый атрибут в одной ветке
        self.method_type = "basic"  # Это добавление для создания конфликта

    def __call__(self, number):
        return round(pow(number, 1 / self.root_degree), self.precision)

    # Изменение: добавление метода в одной ветке
    def calculate_root(self, number):
        return pow(number, 1 / self.root_degree)
