def block_to_block_type(block):
    lines = block.split('\n')

    # Check for heading
    if lines[0].startswith('# ') or lines[0].startswith('## ') or lines[0].startswith('### ') or \
       lines[0].startswith('#### ') or lines[0].startswith('##### ') or lines[0].startswith('###### '):
        return "heading"

    # Check for code block
    if block.startswith('```') and block.endswith('```'):
        return "code block"

    # Check for quote block
    if all(line.startswith('> ') for line in lines):
        return "quote block"

    # Check for unordered list block
    if all(line.startswith('* ') or line.startswith('- ') for line in lines):
        return "unordered list block"

    # Check for ordered list block
    if all(line.startswith(f'{i}. ') for i, line in enumerate(lines, 1)):
        return "ordered list block"

    # Default to paragraph
    return "paragraph"

# Tests
def test_block_to_block_type():
    assert block_to_block_type("# This is a heading") == "heading"
    assert block_to_block_type("## This is a subheading") == "heading"
    assert block_to_block_type("```python\nprint('Hello, world!')\n```") == "code block"
    assert block_to_block_type("> This is a quote\n> It spans multiple lines") == "quote block"
    assert block_to_block_type("* This is an unordered list\n* Another item") == "unordered list block"
    assert block_to_block_type("1. First item\n2. Second item") == "ordered list block"
    assert block_to_block_type("This is a regular paragraph.") == "paragraph"

    print("All tests passed!")

# Run tests
test_block_to_block_type()
