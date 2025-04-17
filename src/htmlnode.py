class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """Convert the HTMLNode to an HTML String"""
        if self.tag is None:
            return self.value or ""
        
        attrs_str = ""
        if self.props:
            for attr, value in self.props.items():
                attrs_str += f' {attr}="{value}"'

        if self.children:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
            return f"<{self.tag}{attrs_str}>{children_html}</{self.tag}>"
        elif self.value:
            return f"<{self.tag}{attrs_str}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{attrs_str}></{self.tag}>"
    
    def props_to_html(self):

        if self.props is None:
            return ""

        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result

    def __repr__(self):
        return F"HTMLNode(tag={repr(self.tag)}, value={repr(self.value)}, children={repr(self.children)}, props={repr(self.props)})"