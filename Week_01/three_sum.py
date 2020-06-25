
from typing import List

def three_sum(nums:List[int])->List[List[int]]:
    if len(nums) < 3:
        return []
    nas = []
    nums.sort()
    for first in range(len(nums)-2):
        if nums[first] > 0:
            break
        if first > 0 and nums[first] == nums[first-1]:
            continue
        target = -nums[first]
        three = len(nums) - 1
        for second in range(first+1, len(nums)-1):
            if second > 0 and nums[second] == nums[second-1]:
                continue
            while second < three and nums[second]+nums[three]>target:
                three -= 1
            if second == three:
                break
            if nums[second] + nums[three] == target:
                nas.append([nums[first], nums[second], nums[three]])
    return nas



