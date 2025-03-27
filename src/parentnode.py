from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        
        if self.tag is None:
            raise ValueError('ParentNode tag must have a value.')
        
        if self.children is None:
            raise ValueError('ParentNode children cannot be empty.')
        
        props_str = ""
        if self.props:
            for prop, value in self.props.items():
                props_str += f' {prop}="{value}"'

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f'<{self.tag}{props_str}>{children_html}</{self.tag}>'