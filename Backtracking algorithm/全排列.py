def permute(nums):
    def backtrack(current, nums, visited):
        if len(current) == len(nums):
            result.append(current[:])
        else:
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    current.append(nums[i])
                    backtrack(current, nums, visited)
                    visited[i] = False
                    current.pop()

    result = []
    visited = [False] * len(nums)
    backtrack([], nums, visited)
    return result

print(permute([1,2,3]))