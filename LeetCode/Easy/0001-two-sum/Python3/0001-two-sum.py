class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = {}
        answer = []

        for i, n in enumerate(nums):
            find = target - n

            if find in num_list:
                answer.append(num_list[find])
                answer.append(i)
            
            else:
                num_list[n] = i
        
        return answer