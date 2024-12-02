class RootCalculator:
    def __init__(self, root_degree, precision=2):
        self.root_degree = root_degree
        self.precision = precision

    def __call__(self, number):
        return round(pow(number, 1 / self.root_degree), self.precision)
