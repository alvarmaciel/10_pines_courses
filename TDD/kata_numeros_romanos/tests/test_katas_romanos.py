import unittest


class MyTestCase(unittest.TestCase):
    def test_A(self):
        self.assertEqual(self.convert_to_roman_string(1), "I")

    def test_B(self):
        self.assertEqual(self.convert_to_roman_string(2), "II")

    def test_C(self):
        self.assertEqual(self.convert_to_roman_string(3), "III")

    def test_D(self):
        self.assertEqual(self.convert_to_roman_string(4), "IV")

    def test_E(self):
        self.assertEqual(self.convert_to_roman_string(5), "V")

    def test_F(self):
        self.assertEqual(self.convert_to_roman_string(6), "VI")

    def test_G(self):
        self.assertEqual(self.convert_to_roman_string(7), "VII")

    def test_H(self):
        self.assertEqual(self.convert_to_roman_string(8), "VIII")

    def test_I(self):
        self.assertEqual(self.convert_to_roman_string(9), "IX")

    def test_J(self):
        self.assertEqual(self.convert_to_roman_string(10), "X")

    def test_K(self):
        self.assertEqual(self.convert_to_roman_string(11), "XI")
        self.assertEqual(self.convert_to_roman_string(12), "XII")
        self.assertEqual(self.convert_to_roman_string(13), "XIII")

    def test_L(self):
        self.assertEqual(self.convert_to_roman_string(14), "XIV")

    def test_M(self):
        self.assertEqual(self.convert_to_roman_string(15), "XV")
        self.assertEqual(self.convert_to_roman_string(16), "XVI")
        self.assertEqual(self.convert_to_roman_string(17), "XVII")
        self.assertEqual(self.convert_to_roman_string(18), "XVIII")

    def test_N(self):
        self.assertEqual(self.convert_to_roman_string(19), "XIX")

    def test_O(self):
        self.assertEqual(self.convert_to_roman_string(20), "XX")
        self.assertEqual(self.convert_to_roman_string(21), "XXI")
        self.assertEqual(self.convert_to_roman_string(22), "XXII")
        self.assertEqual(self.convert_to_roman_string(23), "XXIII")
        self.assertEqual(self.convert_to_roman_string(24), "XXIV")
        self.assertEqual(self.convert_to_roman_string(25), "XXV")
        self.assertEqual(self.convert_to_roman_string(28), "XXVIII")
        self.assertEqual(self.convert_to_roman_string(29), "XXIX")

    def test_P(self):
        self.assertEqual(self.convert_to_roman_string(30), "XXX")
        self.assertEqual(self.convert_to_roman_string(33), "XXXIII")
        self.assertEqual(self.convert_to_roman_string(34), "XXXIV")
        self.assertEqual(self.convert_to_roman_string(35), "XXXV")
        self.assertEqual(self.convert_to_roman_string(38), "XXXVIII")
        self.assertEqual(self.convert_to_roman_string(39), "XXXIX")

    def test_Q(self):
        self.assertEqual(self.convert_to_roman_string(40), "XL")
        self.assertEqual(self.convert_to_roman_string(53), "LIII")
        self.assertEqual(self.convert_to_roman_string(64), "LXIV")
        self.assertEqual(self.convert_to_roman_string(75), "LXXV")
        self.assertEqual(self.convert_to_roman_string(88), "LXXXVIII")
        self.assertEqual(self.convert_to_roman_string(99), "XCIX")

    def convert_to_roman_string(self, number_to_convert: int) -> str:
        result = ""
        result = self.convert_digit(number_to_convert)
        if 10 <= number_to_convert <= 19:
            result = "X" + self.convert_digit(number_to_convert % 10)
        elif 20 <= number_to_convert <= 29:
            result = "XX" + self.convert_digit(number_to_convert % 20)
        elif number_to_convert >= 30:
            result = "XXX" + self.convert_digit(number_to_convert % 30)
        return result

    def convert_digit(self, number_to_convert: int) -> str:
        result = ""
        if 1 <= number_to_convert <= 3:
            result = self.dame_palitos(number_to_convert)
        elif number_to_convert == 4:
            result = "IV"
        elif 5 <= number_to_convert <= 8:
            result = "V" + self.dame_palitos(number_to_convert - 5)
        elif number_to_convert == 9:
            result = "IX"
        return result

    def dame_palitos(self, number_to_convert: int) -> str:
        result = ""
        for i in range(number_to_convert):
            result += "I"
        return result


if __name__ == '__main__':
    unittest.main()
