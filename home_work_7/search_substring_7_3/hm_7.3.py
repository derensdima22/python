def second_index(text: str, some_str: str) -> int | None:
    start_find = text.find(some_str)
    if start_find == -1:
        print("is None")
        return None

    end_find = text.find(some_str, start_find + len(some_str))
    print(end_find if end_find != -1 else "is None")
    return end_find if end_find != -1 else None


second_index("sims", "s") # == 3, 'Test1'
second_index("find the river", "e") # == 12, 'Test2'
second_index("hi", "h") # is None, 'Test3'
second_index("Hello, hello", "lo") #  == 10