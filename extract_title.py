import re

def extract_title(markdown):
    match = re.match(r'^# (.+)', markdown.strip())
    if match:
        return match.group(1).strip()
    else:
        raise Exception("No h1 header found")
