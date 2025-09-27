class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
            # print(hashmap)
        return []

        
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == target - nums[i]:
        #             return [i, j]
        # return []