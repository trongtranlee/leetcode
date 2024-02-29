class Solution(object):
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        prev_value = 0

        for char in s:
            value = roman_values[char]

            # "IV" đại diện cho số 4, trong đó 'I' (1) được trừ đi từ 'V' (5).
            # Điều này có thể được thể hiện bằng cách lấy giá trị của ký tự hiện tại (value)
            # và trừ đi hai lần giá trị của ký tự trước đó (prev_value),
            # vì chúng ta đã cộng giá trị của ký tự trước đó vào result trong vòng lặp trước đó */
            if value > prev_value:
                result += value - 2 * prev_value
            else:
                result += value
            prev_value = value

        return result

