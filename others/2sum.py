def twoSum(nums, target): 
    visited = set()
    tuples = []

    for num in nums:
        if target-num in visited:
            tuples.append([target-num, num])
        else:
            visited.add(num)

    return tuples


if __name__ == "__main__":
    nums = [2, 5, 1, 8, 4]
    target = 6

    print(twoSum(nums, target))
