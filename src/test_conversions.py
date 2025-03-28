import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode
from conversions import text_node_to_html_node  # Replace 'your_module_name' with the module containing your function

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        # Test for TEXT type (provided in the lesson)
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        # Test for BOLD type
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        
    def test_italic(self):
        # Test for ITALIC type
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        
    def test_code(self):
        # Test for CODE type
        node = TextNode("Code snippet", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code snippet")
        
    def test_link(self):
        # Test for LINK type
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props["href"], "https://example.com")
        
    def test_image(self):
        # Test for IMAGE type
        node = TextNode("Alt text for image", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "https://example.com/image.png")
        self.assertEqual(html_node.props["alt"], "Alt text for image")
        
    def test_invalid_type(self):
        # Test for invalid TextType
        # Create a mock TextNode with an invalid type for testing
        # This requires a bit of a hack since we're using an Enum
        class MockTextNode:
            def __init__(self):
                self.text = "Invalid"
                self.text_type = "invalid_type"
        
        node = MockTextNode()
        with self.assertRaises(Exception):
            html_node = text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()