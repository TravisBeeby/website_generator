class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def props_to_html(self):
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())

    def to_html(self):
        raise NotImplementedError("to_html method should be implemented by subclasses")

    def __repr__(self):
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"
