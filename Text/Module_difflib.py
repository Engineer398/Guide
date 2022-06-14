import difflib

textl = """"Lorem ipsum dolor sit amet, consectetuer adipiscing
elit. Integer eu lacus accumsan arcu fermentum euismod. Donec
pulvinar porttitor tellus. Aliquam venenatis. Donec facilisis
pharetra tortor. In nec mauris eget magna consequat
convalis. Nam sed sem vitae odio pellentesque interdum. Sed
consequat viverra nisl. Suspendisse arcu metus, blandit quis,
rhoncus ас, pharetra eget, velit. Mauris urna. Morbi nonummy
molestie orci. Praesent nisi elit, fringilla ас, suscipit non,
tristique vel, mauris. Curabitur vel lorem id nisl porta
adipiscing. Suspendisse eu lectus. In nunc. Duis vulputate
tristique enim. Donec quis lectus а justo imperdiet tempus."""

text2 = """Lorem ipsum dolor sit amet, consectetuer adipiscing
elit. Integer eu lacus accumsan arcu fermentum euismod. Donec
pulvinar, porttitor tellus. Aliquam venenatis. Donec facilisis
pharetra tortor. In nec mauris eget magna consequat
convalis. Nam cras vitae mi vitae odio pellentesque interdum. Sed
consequat viverra nisl. Suspendisse arcu metus, blandit quis,
rhoncus ас, pharetra eget, velit. Mauris urna. Morbi nonummy
molestie orci. Praesent nisi elit, fringilla ас, suscipit non,
tristique vel, mauris. Curabitur vel lorem id nisl porta
adipiscing. Duis vulputate tristique enim. Donec quis lectus а
justo imperdiet tempus. Suspendisse eu lectus. In nunc."""

text1_lines = textl.splitlines()
text2_lines = text2.splitlines()

def compare():
    d = difflib.Differ()
    diff = d.compare(text1_lines, text2_lines)
    print("\n".join(diff))

# compare()

def unified_diff():
    diff = difflib.unified_diff(text1_lines, text2_lines, lineterm="")
    print("\n".join(diff))

# unified_diff()

def sequence_match():
    a = [1, 2, 3, 4, 5, 6]
    b = [2, 1, 3, 5, 4, 6]

    diff = difflib.SequenceMatcher(None, a, b)
    for tag, i1, i2, j1, j2  in diff.get_opcodes():
        print(f"{tag} {i1} {i2} {j1} {j2}")

# sequence_match()
