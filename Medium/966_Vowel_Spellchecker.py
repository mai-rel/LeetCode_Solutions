from typing import List


def replace_vowels(word):
    new_word = ''
    vowels = set('aeiouAEIOU')

    for char in word:
        if char in vowels:
            new_word += '*'
        else:
            new_word += char

    return new_word


def spellchecker(wordlist: List[str], queries: List[str]) -> List[str]:
    words = set(wordlist)
    lowercase_words = {}
    no_vowels_words = {}

    for word in wordlist:
        lower_word = word.lower()
        if lower_word not in lowercase_words:
            lowercase_words[lower_word] = word

        no_vowels_word = replace_vowels(lower_word)

        if no_vowels_word not in no_vowels_words:
            no_vowels_words[no_vowels_word] = word

    answer = [''] * len(queries)

    for i, word in enumerate(queries):

        if word in words:
            answer[i] = word
            continue

        lower_word = word.lower()

        if lower_word in lowercase_words:
            answer[i] = lowercase_words[lower_word]
            continue

        no_vowels_word = replace_vowels(lower_word)

        if no_vowels_word in no_vowels_words:
            answer[i] = no_vowels_words[no_vowels_word]

    return answer