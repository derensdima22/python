import re

def first_word(text: str) -> str:
    match = re.search(r"[a-zA-Z']+", text)

    return match.group(0) if match else ''

print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))


# O(n) Якщо ми будемо використовувати строку замість листа, то в for ми будемо добавляти
# кожного разу до строки нову букву і стрінга буде завжди змінюватись, а сама стінга внас
# immutable ( замість word_list = [] world = ""). А так в нас завжди один масив і word_list
# який завжди ссилається на нього.
def first_word_2(text: str) -> str:
    word_list = []
    is_first = True
    for char in text:
        if char.isalpha() or char == "'":
            word_list.append(char)
            is_first = False
        elif not is_first:
            break

    return ''.join(word_list)

print(first_word_2("Hello world"))
print(first_word_2("greetings, friends"))
print(first_word_2("don't touch it"))
print(first_word_2(".., and so on ..."))
print(first_word_2("hi"))
print(first_word_2("Hello.World"))