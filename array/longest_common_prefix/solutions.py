def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    strs_len = [len(i) for i in strs]
    min_len = min(strs_len)
    min_index = strs_len.index(min_len)
    prefix = strs[min_index]
    res = ''
    for i in range(min_len):
        for j in strs:
            if j[i] == prefix[i]:
                continue
            else:
                return res
        res += prefix[i]
    return res