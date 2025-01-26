class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children else []
        self.props = props if props else {}

    def props_to_html(self):
        if not self.props:
            return ""
        props_str = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return f" {props_str}"

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method.")

# Define LeafNode as a subclass of HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("Value must be provided for LeafNode")
        super().__init__(tag=tag, value=value, children=[], props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        if self.tag == "img":  # Special case for self-closing tags like <img>
            return f'<{self.tag}{self.props_to_html()} />'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

# Define ParentNode as a subclass of HTMLNode
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("Tag must be provided for ParentNode")
        if not children:
            raise ValueError("Children must be provided for ParentNode")
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        children_html = ''.join(child.to_html() for child in self.children)
        return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'

# Example usage
node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

print(node.to_html())
