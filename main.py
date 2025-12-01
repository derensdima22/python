from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

h1_text = soup.find('h1').text
p_text = soup.find('p').text

print(h1_text)
print(p_text)

