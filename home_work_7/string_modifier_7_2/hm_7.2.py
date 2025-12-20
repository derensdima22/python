def correct_sentence(text: str) -> None:
    new_text = text[0].upper() + text[1:]
    # print(new_text if text[-1] == '.' else f"{new_text}.") # example 1

    if not text.endswith('.'): new_text += '.' # example 2
    print(new_text)


correct_sentence("greetings, friends")
correct_sentence("hello")
correct_sentence("Greetings. Friends")
correct_sentence("Greetings, friends.")
correct_sentence("greetings, friends.")