def merge2(nums1, m, nums2, n):
    nums1[:] = [x for x in nums1 if x != 0]
    nums2[:] = [x for x in nums2 if x != 0]
    i, j = 0, 0
    res = []
    run = min(m, n)
    for k in range(0, run):
        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    if m > n:
        res.extend(nums1[i:])
    else:
        res.extend(nums2[j:])
    return res

def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            print(nums1)
        else:
            nums1[k] = nums2[j]
            j -= 1
            print(nums1)
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1