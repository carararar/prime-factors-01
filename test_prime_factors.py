from unittest import TestCase

from prime_factors import PrimeFactors


class TestPrimeFactors(TestCase):
    def setUp(self):
        super().setUp()
        self.sut = PrimeFactors()

    def test_prime_factors_when_1(self):
        self.assertEqual([], self.sut.of(1))

    def test_prime_factors_when_2(self):
        self.assertEqual([2], self.sut.of(2))

    def test_prime_factors_when_3(self):
        self.assertEqual([3], self.sut.of(3))

    def test_prime_factors_when_4(self):
        self.assertEqual([2, 2], self.sut.of(4))

    def test_prime_factors_when_6(self):
        self.assertEqual([2, 3], self.sut.of(6))

    def test_prime_factors_when_8(self):
        self.assertEqual([2, 2, 2], self.sut.of(8))

    def test_prime_factors_when_9(self):
        self.assertEqual([3, 3], self.sut.of(9))

    def test_prime_factors_when_12(self):
        self.assertEqual([2, 2, 3], self.sut.of(12))

    def test_prime_factors_when_14(self):
        self.assertEqual([2, 7], self.sut.of(14))

    def test_prime_factors_when_15(self):
        self.assertEqual([3, 5], self.sut.of(15))
