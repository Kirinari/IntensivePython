"""
hello pylint
"""


def find_anagrams(text, pattern):
    """
    hello pylint
    """

    max_ord = 0

    for i in text:
        if ord(i) > max_ord:
            max_ord = ord(i)
    for i in pattern:
        if ord(i) > max_ord:
            max_ord = ord(i)
    max_ord += 1
    result = []

    textlen = len(text)
    patternlen = len(pattern)

    text_count = [0] * max_ord
    pattern_counter = text_count.copy()

    for i in range(patternlen):
        symb_pattern = ord(pattern[i])
        symb_text = ord(text[i])
        text_count[symb_pattern] += 1
        pattern_counter[symb_text] += 1

    for i in range(patternlen, textlen):
        ans = True
        for j in range(max_ord):
            if text_count[j] != pattern_counter[j]:
                ans = False
        if ans:
            result.append(i - patternlen)

        symb_text_left = ord(text[i])
        pattern_counter[symb_text_left] += 1

        symb_text_right = ord(text[i-patternlen])
        pattern_counter[symb_text_right] -= 1

    ans = True
    for i in range(max_ord):
        if text_count[i] != pattern_counter[i]:
            ans = False
    if ans:
        result.append(textlen - patternlen)

    return result


assert find_anagrams("abcba", "abc") == [0, 2]
assert find_anagrams("aaa", "a") == [0, 1, 2]
assert find_anagrams("abc cba xabcd", 'abc') == [0, 4, 9]
assert find_anagrams("ффф", 'ф') == [0, 1, 2]
assert find_anagrams("trccccytvbabc", "cc") == [2, 3, 4]
assert find_anagrams("aaababaa", "aaba") == [0, 1, 4]
assert find_anagrams("ракета", "карета") == [0]
assert find_anagrams("тут нет анаграмм", "эх") == []
