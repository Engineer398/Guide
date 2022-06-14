"""
Модуль textwrap может использоваться для форматирования текста в ситуациях,
когда требуется красиво оформленный вывод. Он предоставляет функциональность,
аналогичную средствам автоматического выравнивания и распределения
текста в пределах абзаца, предлагаемым многими текстовыми редакторами и
издательскими системами.
"""
sample_text = """The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
"""
import textwrap

# Функция fill() получает текст в качестве входных данных и возвращает
# текст, отформатированный с учетом ширины заданной области.
def fill():
    print(textwrap.fill(sample_text, width=30))

# fill()

# Функция dedent. Удаление существующих отступов textwrap.dedent
def dedent():
    print("Dedent:")
    print(textwrap.dedent(sample_text))

# dedent()

def indent():
    text = textwrap.dedent(sample_text)
    text = textwrap.fill(text, width=50)
    text = textwrap.indent(text, "> ") # make prefix
    print("Formated block")
    print(text)

# indent()

# indent predicate

def help_func(line):
    print(f"Indent: {line}", end="")
    return len(line) % 2 == 0


def indent_predicate():
    text = textwrap.dedent(sample_text)
    text = textwrap.fill(text, width=50)
    text = textwrap.indent(text, "> ", help_func)

    print("\n\nFormated text\n")
    print(text)

# indent_predicate()

def short_len():
    text = textwrap.dedent(sample_text)
    text = textwrap.shorten(text, width=40)
    print(text)

# short_len()




