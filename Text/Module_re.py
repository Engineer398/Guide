"""
Regular Expression
Only main functions
"""

import re

def re_search():
    pattern = "this"
    text = "Does this text match the pattern?"
    match = re.search(pattern, text)
    print(match)
    s = match.start()
    e = match.end()
    print("Found \"{0}\" in \"{1}\" from \"{2}\" to \"{3}\" \t \"{4}\"".format(
        match.re.pattern, match.string, s, e, text[s:e]))

# re_search()
# Функция compile () преобразует строку регулярного выражения в объект RegexObject.
def re_compile():
    regexs = [
        re.compile(p)
        for p in ["this", "that"]
    ]

    text = "Does this text match the pattern"
    print("Text: {!r}".format(text))

    for regex in regexs:
        print("Seeking {} ->".format(regex.pattern), end=" ")
        if regex.search(text):
            print("match")
        else:
            print("no match")

# re_compile()

def re_findall():
    text = "abbaabbababbbaaabbaba"
    pattern = "ab"

    for match in re.findall(pattern, text):
        print("Found \"{find}\"".format(find=match))

# re_findall()

# функция finditer возвращает итератор, создающий экземпляры Match
def re_finditer():
    text = "abbaabbababbbaaabbaba"
    pattern = "ab"
    print(text)
    for match in re.finditer(pattern, text):
        print("Find {2} from {0} to {1}".format(match.start(), match.end(), match.re.pattern))

re_finditer()