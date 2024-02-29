class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        number = number.replace(" ", "").replace("-", "")

        formatted_number = []
        while len(number) > 4:
            formatted_number.append(number[:3])
            number = number[3:]

        # Handle the remaining digits
        if len(number) == 2:
            formatted_number.append(number)
        elif len(number) == 3:
            formatted_number.append(number)
        else:
            formatted_number.append(number[:2])
            formatted_number.append(number[2:])

        return "-".join(formatted_number)