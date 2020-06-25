
def two_sum(nums, target):
    d ={}
    for i, v in enumerate(nums):
        if v in d:
            return [d[v], i]
        d[target-v] = i

