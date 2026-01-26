import re

def delete_html_tags(html_file, result_file='new_file.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    clear_html = re.sub(r'<[^>]+>', '', html)
    text_splitlines = clear_html.splitlines()
    text = [line.strip() for line in text_splitlines if line.strip()]

    with open(result_file, 'w', encoding='utf-8') as out:
        out.write('\n'.join(text))

    return '\n'.join(text)


print(delete_html_tags('example.html'))
