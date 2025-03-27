import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    
    def test_to_html_basic(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")])
        self.assertEqual(node.to_html(), "<div><p>Hello, world!</p></div>")
    
    def test_to_html_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_to_html_with_props(self):
        node = ParentNode(
            "div", 
            [LeafNode("span", "Content")], 
            {"class": "container", "id": "main"}
        )
        self.assertEqual(node.to_html(), '<div class="container" id="main"><span>Content</span></div>')
    
    def test_to_html_with_nested_parents(self):
        grandchild = LeafNode("b", "Grandchild")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(
            parent.to_html(),
            "<div><span><b>Grandchild</b></span></div>"
        )
    
    def test_to_html_complex_structure(self):
        # Create a more complex nested structure
        structure = ParentNode(
            "div",
            [
                LeafNode("h1", "Website Title"),
                ParentNode(
                    "nav",
                    [
                        ParentNode("ul", [
                            ParentNode("li", [LeafNode("a", "Home")]),
                            ParentNode("li", [LeafNode("a", "About")]),
                            ParentNode("li", [LeafNode("a", "Contact")])
                        ])
                    ],
                    {"class": "main-nav"}
                ),
                ParentNode(
                    "section",
                    [
                        LeafNode("h2", "Welcome"),
                        LeafNode("p", "Content goes here")
                    ],
                    {"id": "main-content"}
                )
            ],
            {"class": "container"}
        )
        
        expected = '<div class="container"><h1>Website Title</h1><nav class="main-nav"><ul><li><a>Home</a></li><li><a>About</a></li><li><a>Contact</a></li></ul></nav><section id="main-content"><h2>Welcome</h2><p>Content goes here</p></section></div>'
        self.assertEqual(structure.to_html(), expected)