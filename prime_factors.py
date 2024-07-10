class PrimeFactors:
    def of(self, n) -> []:
        factors = []
        if n == 1:
            return factors
        while n > 1:
            if n % 2 == 0:
                factors.append(2)
                n /= 2
            elif n % 7 == 0:
                factors.append(7)
                n /= 7
            elif n % 5 == 0:
                factors.append(5)
                n /= 5
            elif n % 3 == 0:
                factors.append(3)
                n /= 3

        return factors
