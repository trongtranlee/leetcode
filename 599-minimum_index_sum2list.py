from astroid import List


class Solution(object):
    def findRestaurant(self, list1:List[str], list2:List[str])-> List[str]:
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        mapList1 = {}
        mapList2 = {}
        for index1, value1 in enumerate(list1):
            mapList1[value1] = index1
        for index2, value2 in enumerate(list2):
            mapList2[value2] = index2

        common_strings = []
        min_index_sum = float('inf')

        for word, index1 in mapList1.items():
            if word in mapList2:
                # Tính tổng chỉ số
                index_sum = index1 + mapList2[word]
                # Nếu tổng chỉ số nhỏ hơn hoặc bằng tổng nhỏ nhất hiện tại
                if index_sum <= min_index_sum:
                    # Nếu tổng chỉ số nhỏ hơn tổng nhỏ nhất hiện tại, cập nhật kết quả
                    if index_sum < min_index_sum:
                        common_strings = []
                        min_index_sum = index_sum
                    # Thêm chuỗi vào kết quả
                    common_strings.append(word)

        return common_strings

