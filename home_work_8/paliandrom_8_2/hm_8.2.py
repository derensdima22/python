import re

def is_palindrome(text: str) -> bool:
    filter_re = re.sub(r'^a-z0-9]', '', text.lower())
    filter_str = ''.join(filter(str.isalnum, text.lower())) # -> or ''.join(x.lower() for x in text if x.isalnum())
    result = filter_str == filter_str[::-1]

    return result

print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('0P'))
print(is_palindrome('a.'))
print(is_palindrome('aurora'))
