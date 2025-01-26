import re

def extract_markdown_images(text):
    pattern = r'!

\[([^\]

]+)\]

\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r'

\[([^\]

]+)\]

\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

# Tests
def test_extract_markdown_images():
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    assert extract_markdown_images(text) == [
        ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
        ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
    ]
    
    text = "No images here!"
    assert extract_markdown_images(text) == []
    
    text = "Broken ![alt text](url) and ![alt text(https://example.com) syntax"
    assert extract_markdown_images(text) == [("alt text", "url")]

def test_extract_markdown_links():
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    assert extract_markdown_links(text) == [
        ("to boot dev", "https://www.boot.dev"),
        ("to youtube", "https://www.youtube.com/@bootdotdev")
    ]
    
    text = "No links here!"
    assert extract_markdown_links(text) == []
    
    text = "Broken [link text](url and [link text(https://example.com) syntax"
    assert extract_markdown_links(text) == [("link text", "url")]

    print("All tests passed!")

# Run tests
test_extract_markdown_images()
test_extract_markdown_links()
