"""print(__name__)
import practice

print(__name__)
if __name__ == "__main__":
    practice.my_function()
"""


def twoSum(nums, target):
    output_list = []
    for i in range(0, len(nums)):
        # print(input_list[i])
        for j in range(i + 1, len(nums)):
            # print(input_list[j])
            sum = nums[i] + nums[j]
            # print(sum)
            if sum == target:
                output_list.append(i)
                output_list.append(j)
                return output_list
    return output_list


input_list = [2, 7, 11, 15]
target = 22
op = twoSum(nums=input_list, target=target)
print(op)


