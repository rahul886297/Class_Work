import re

pattern = re.compile(r"\d+")

text = "123 apples, 456 bananas"
matches = pattern.findall(text)
print("Matches:", matches)