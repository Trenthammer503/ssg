import unittest
from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_with_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(3, len(new_nodes))
        self.assertEqual("This is text with a ", new_nodes[0].text)
        self.assertEqual(TextType.TEXT, new_nodes[0].text_type)
        self.assertEqual("code block", new_nodes[1].text)
        self.assertEqual(TextType.CODE, new_nodes[1].text_type)
        self.assertEqual(" word", new_nodes[2].text)
        self.assertEqual(TextType.TEXT, new_nodes[2].text_type)
    
    def test_split_with_bold_delimiter(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(3, len(new_nodes))
        self.assertEqual("This is ", new_nodes[0].text)
        self.assertEqual(TextType.TEXT, new_nodes[0].text_type)
        self.assertEqual("bold", new_nodes[1].text)
        self.assertEqual(TextType.BOLD, new_nodes[1].text_type)
        self.assertEqual(" text", new_nodes[2].text)
        self.assertEqual(TextType.TEXT, new_nodes[2].text_type)

    def test_split_with_italic_delimiter(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        
        self.assertEqual(3, len(new_nodes))
        self.assertEqual("This is ", new_nodes[0].text)
        self.assertEqual(TextType.TEXT, new_nodes[0].text_type)
        self.assertEqual("italic", new_nodes[1].text)
        self.assertEqual(TextType.ITALIC, new_nodes[1].text_type)
        self.assertEqual(" text", new_nodes[2].text)
        self.assertEqual(TextType.TEXT, new_nodes[2].text_type)

    def test_multiple_delimiters_in_text(self):
        node = TextNode("This has `code` and **bold** text", TextType.TEXT)
        # First split by code
        intermediate_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        # Then split the result by bold
        final_nodes = split_nodes_delimiter(intermediate_nodes, "**", TextType.BOLD)
        
        self.assertEqual(5, len(final_nodes))
        self.assertEqual("This has ", final_nodes[0].text)
        self.assertEqual(TextType.TEXT, final_nodes[0].text_type)
        self.assertEqual("code", final_nodes[1].text)
        self.assertEqual(TextType.CODE, final_nodes[1].text_type)
        self.assertEqual(" and ", final_nodes[2].text)
        self.assertEqual(TextType.TEXT, final_nodes[2].text_type)
        self.assertEqual("bold", final_nodes[3].text)
        self.assertEqual(TextType.BOLD, final_nodes[3].text_type)
        self.assertEqual(" text", final_nodes[4].text)
        self.assertEqual(TextType.TEXT, final_nodes[4].text_type)
    
    def test_no_delimiter_in_text(self):
        node = TextNode("This has no delimiters", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(1, len(new_nodes))
        self.assertEqual("This has no delimiters", new_nodes[0].text)
        self.assertEqual(TextType.TEXT, new_nodes[0].text_type)

    