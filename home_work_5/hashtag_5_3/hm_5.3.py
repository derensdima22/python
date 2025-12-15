import string

# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

hashtag_name = input("Enter a hashtag name: ")

for char in string.punctuation:
    hashtag_name = hashtag_name.replace(char, "")

hashtag = f"#{"".join(word.capitalize() for word in hashtag_name.split())}"

print(hashtag[:140])

