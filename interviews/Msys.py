# write a python code to find the pair of elements in a list that
# produces the min value when added.
# Use multilevel inheritance to get the list, process the sum, return the result
class InputList:
    def __init__(self, lst):
        self.lst = lst


class MinSumPairFinder(InputList):
    def __init__(self, lst):
        super().__init__(lst)
        self.min_pair = self.find_min_sum_pair()

    def find_min_sum_pair(self):
        if len(self.lst) < 2:
            return None  # Not enough elements to form a pair

        min_sum = float('inf')
        min_pair = (None, None)

        # Iterate through all possible pairs
        for i in range(len(self.lst)):
            for j in range(i + 1, len(self.lst)):
                current_sum = self.lst[i] + self.lst[j]
                if current_sum < min_sum:
                    min_sum = current_sum
                    min_pair = (self.lst[i], self.lst[j])

        return min_pair


class MinSumPairResult(MinSumPairFinder):
    def __init__(self, lst):
        super().__init__(lst)

    def get_min_sum_pair(self):
        return self.min_pair


# Example usage
lst = [4, 3, 1, 2, 5]
result = MinSumPairResult(lst)
print("The pair with the minimum sum is:", result.get_min_sum_pair())
