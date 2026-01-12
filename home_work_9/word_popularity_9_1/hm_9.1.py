from collections import Counter

def popular_words(text: str, words: list[str]) -> dict[str, int]:
    text_list = text.lower().split()
    counter = {}
    for word in text_list:
        counter[word] = counter.get(word, 0) + 1

    return {word: counter.get(word, 0) for word in words}


def popular_words_with_count(text: str, words: list[str]) -> dict[str, int]:
    text_list = text.lower().split()
    counter = Counter(text_list)

    return {word: counter.get(word, 0) for word in words}


print(popular_words('''
When I was One I had just begun When I was Two I was nearly new 
''', ['i', 'was', 'three', 'near']))

print(popular_words_with_count('''
When I was One I had just begun When I was Two I was nearly new 
''', ['i', 'was', 'three', 'near']))