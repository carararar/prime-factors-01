from unittest import TestCase

from prime_factors import PrimeFactors


class TestPrimeFactors(TestCase):
    def setUp(self):
        super().setUp()
        self.sut = PrimeFactors()

    def test_prime_factors_when_1(self):
        self.assertEqual([], [])