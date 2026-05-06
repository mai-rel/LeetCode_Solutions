def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    max_len = 0
    l = 0

    for r, char in enumerate(s):

        while char in seen:
            prev_char = s[l]
            seen.remove(prev_char)
            l += 1

        seen.add(char)
        max_len = max(max_len, r - l + 1)

    return max_len