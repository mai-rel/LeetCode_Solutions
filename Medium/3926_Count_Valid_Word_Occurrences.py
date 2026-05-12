from collections import Counter


def add_word(counter, stack):
    if stack[-1] == '-':
        stack.pop()
    word = ''.join(stack)
    counter[word] += 1
    stack.clear()


def countWordOccurrences(chunks: list[str], queries: list[str]) -> list[int]:
    stack = []
    counter = Counter()

    s = ''.join(chunks)

    for i, char in enumerate(s):
        if char.isalpha() or (stack and stack[-1].isalpha() and char == '-'):
            stack.append(char)
        elif stack and char == ' ':
            add_word(counter, stack)
        elif stack and char == '-' and stack[-1] == '-':
            add_word(counter, stack)

    if stack:
        add_word(counter, stack)

    result = []

    for word in queries:
        result.append(counter[word])

    return result