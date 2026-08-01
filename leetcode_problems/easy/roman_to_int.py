def romanToInt(s: str) -> int:
        roman_numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0

        for i, j in zip(s, s[1:]):
            if roman_numbers[i] < roman_numbers[j]:
                result -= roman_numbers[i]
            else:
                result += roman_numbers[i]
        return result + roman_numbers[s[-1]]
                   


romanToInt('LVIII')