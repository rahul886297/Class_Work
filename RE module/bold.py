#Write a functiont that takes a string with email and return it eith email enclosed in bold tag

import re
test="""
This is my email rmandla9988@gmail.com
"""
def bold_email(test):
    pattern_email = r"[\w.]+@[\S]*"
    match = re.search(pattern_email,test)
    replace = f"<b>{match.group()}</b>"
    replacedString = re.sub(pattern_email,replace, test)
    return replacedString


replacedString = bold_email(test)
print("after replacement")
print(f"\n\n{replacedString}\n\n")