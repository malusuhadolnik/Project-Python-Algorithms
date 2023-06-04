def find_duplicate(nums: list[int]):
    is_array = isinstance(nums, list)
    n = len(nums)

    if not nums or is_array is False or n == 1:
        return False

    ordered = sorted(nums)
    for i in range(0, n-1):
        if ordered[i] == ordered[i + 1] and ordered[i] > 0:
            return ordered[i]
    return False
