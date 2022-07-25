import re

pattern_title = r"(?<=\<title\>).+(?=\<\/title\>)"
pattern_content = r"(?<=>)([^<>]*)(?=<)"
html_text = input()
title = "".join(re.findall(pattern_title, html_text))
content = []
content_element = [elem.group() for elem in re.finditer(pattern_content, html_text)]
for element in content_element:
    element = element.replace("\\n", "")
    if element != title and element != '':
        content.append(element.strip())
print(f"Title: {title}")
print(f'Content: {" ".join(content)}')