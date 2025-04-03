import unittest
from texttotextnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):

    def test_full_markdown_processing(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        actual_nodes = text_to_textnodes(text)
        self.assertListEqual(expected_nodes, actual_nodes)

    def test_no_markdown(self):
        text = "This is plain text."
        expected_nodes = [TextNode(text, TextType.TEXT)]
        actual_nodes = text_to_textnodes(text)
        self.assertListEqual(expected_nodes, actual_nodes)

    def test_only_bold(self):
        text = "This is **bold text**."
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(".", TextType.TEXT),
        ]
        actual_nodes = text_to_textnodes(text)
        self.assertListEqual(expected_nodes, actual_nodes)

    def test_only_italic(self):
        text = "This is _italic text_."
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(".", TextType.TEXT),
        ]
        actual_nodes = text_to_textnodes(text)
        self.assertListEqual(expected_nodes, actual_nodes)

    def test_only_code(self):
        text = "This is `code text`."
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code text", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        actual_nodes = text_to_textnodes(text)
        self.assertListEqual(expected_nodes, actual_nodes)

    def test_only_image(self):
        text = "This is an ![image](url)."
        expected_nodes = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "url"),
            TextNode(".", TextType.TEXT),
        ]
        actual_nodes = text_to_textnodes(text)
        self.assertListEqual(expected_nodes, actual_nodes)

    def test_only_link(self):
        text = "This is a [link](url)."
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "url"),
            TextNode(".", TextType.TEXT),
        ]
        actual_nodes = text_to_textnodes(text)
        self.assertListEqual(expected_nodes, actual_nodes)

    # def test_nested_markdown_not_supported(self):
    #     # The current implementation likely doesn't support nested markdown
    #     text = "This is **bold _italic_ text**."
    #     expected_nodes = [
    #         TextNode("This is ", TextType.TEXT),
    #         TextNode("bold ", TextType.BOLD),
    #         TextNode("_italic_", TextType.TEXT), # Likely treated as plain text
    #         TextNode(" text", TextType.BOLD),
    #         TextNode(".", TextType.TEXT),
    #     ]
    #     actual_nodes = text_to_textnodes(text)
    #     self.assertListEqual(expected_nodes, actual_nodes)

    # def test_markdown_at_start_and_end(self):
    #     text = "**bold** text _italic_ and `code`"
    #     expected_nodes = [
    #         TextNode("", TextType.BOLD),
    #         TextNode("bold", TextType.BOLD),
    #         TextNode("", TextType.BOLD),
    #         TextNode(" text ", TextType.TEXT),
    #         TextNode("", TextType.ITALIC),
    #         TextNode("italic", TextType.ITALIC),
    #         TextNode("", TextType.ITALIC),
    #         TextNode(" and ", TextType.TEXT),
    #         TextNode("", TextType.CODE),
    #         TextNode("code", TextType.CODE),
    #         TextNode("", TextType.CODE),
    #     ]
    #     actual_nodes = text_to_textnodes(text)
    #     self.assertListEqual(expected_nodes, actual_nodes)

if __name__ == '__main__':
    unittest.main()