from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

h1_text = soup.find('h1').text
p_text = soup.find('p').text

print(h1_text)
print(p_text)


import re

text_to_search ="""
    321-555-4321
    123.555.1234
    123*555*1234
    800*555*1234
    900-555-1234
    900-555-1234123
"""

result = re.compile(r"\d{3}[.*-]\d{3}[.*-]\d{4}")

matches = result.findall(text_to_search)
print(matches)

