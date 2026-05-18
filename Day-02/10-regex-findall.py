import re

text = "This is the Python Playlist"
pattern = r"Python"

search = re.search(pattern, text)

if search:
    print("Pattern Found:", search.group())
else:
    print("Pattern not found")