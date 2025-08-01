import markdown
    
# Read markdown file
with open("sample.md", "r", encoding="utf-8") as md_file:
    md_text = md_file.read()

# Convert to HTML
html = markdown.markdown(md_text)

# Wrap it in a basic HTML template with CSS
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Markdown Output</title>
<style>
body {{
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: auto;
    padding: 2rem;
    line-height: 1.6;
}}
code {{
    background-color: #f4f4f4;
    padding: 2px 4px;
    border-radius: 4px;
}}
pre {{
    background-color: #f4f4f4;
    padding: 1rem;
    border-radius: 4px;
    overflow-x: auto;
}}
</style>
</head>
<body>
{html}
</body>
</html>
"""

# Save to output.html
with open("output.html", "w", encoding="utf-8") as output_file:
    output_file.write(html_content)

print("✅ Converted sample.md → output.html")
