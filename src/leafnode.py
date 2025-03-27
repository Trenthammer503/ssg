from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)

        if value is None:
            raise ValueError("LeafNode must have a value")
        
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        
        if self.tag is None:
            return self.value
        
        props_str = ""
        if self.props:
            for prop, value in self.props.items():
                props_str += f' {prop}="{value}"'

        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"