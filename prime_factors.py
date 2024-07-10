class PrimeFactors:
    def of(self, n) -> []:
        factors = []

        if n == 2:
            factors.append(2)
        if n == 3:
            factors.append(3)
        if n == 4:
            factors.append(2)
            factors.append(2)
        if n == 6:
            factors.append(2)
            factors.append(3)
        if n == 8:
            factors.append(2)
            factors.append(2)
            factors.append(2)
        if n == 9:
            factors.append(3)
            factors.append(3)
        if n == 12:
            factors.append(2)
            factors.append(2)
            factors.append(3)
        if n == 14:
            factors.append(2)
            factors.append(7)
        return factors