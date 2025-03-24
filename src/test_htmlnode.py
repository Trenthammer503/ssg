# src/test_htmlnode.py
import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        # Test that props_to_html returns empty string when props is None
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_single_prop(self):
        # Test with a single property
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
    
    def test_props_to_html_multiple_props(self):
        # Test with multiple properties
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        # Note: Since dictionaries don't guarantee order, you might need to check parts individually
        result = node.props_to_html()
        self.assertIn(' href="https://www.google.com"', result)
        self.assertIn(' target="_blank"', result)
        self.assertEqual(len(result), len(' href="https://www.google.com" target="_blank"'))

    def test_repr(self):
        node = HTMLNode("p", "Hello, world!", None, {"class": "greeting"})
        expected = 'HTMLNode(tag=\'p\', value=\'Hello, world!\', children=None, props={\'class\': \'greeting\'})'
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()