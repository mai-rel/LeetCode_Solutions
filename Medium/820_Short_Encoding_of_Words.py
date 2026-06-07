from  typing import  List


def minimumLengthEncoding(words: List[str]) -> int:
    words.sort(key=len, reverse=True)
    used_words = {}
    i = 0

    for word in words:
        is_found = False
        for used_word in used_words:
            if used_word.endswith(word):
                is_found = True
                break

        if not is_found:
            used_words[word] = i
            i += (len(word) + 1)

    return i