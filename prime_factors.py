class PrimeFactors:
    def __init__(self):
        self.__divisor = 2
        self.__factors = []

    def of(self, number) -> []:
        if number < 2:
            return self.__factors

        if number % self.__divisor == 0:
            self.__factors.append(self.__divisor)
            number //= self.__divisor
        else:
            self.__divisor += 1
        return self.of(number)
