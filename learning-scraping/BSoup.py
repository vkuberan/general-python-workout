import bs4

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beautiful Soup</title>
</head>
<body>
    <div class="soup">Welcome to Beautiful Soup - Heading 1</div>
    <div class="soup">Welcome to Beautiful Soup</div>
</body>
</html>"""

parsed_html = bs4.BeautifulSoup(html, "html.parser")

text_found = parsed_html.find("div").text

print(text_found)
