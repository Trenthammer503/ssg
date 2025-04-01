import unittest
from splitlinks import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitLinks(unittest.TestCase):

    def test_split_nodes_image_no_image(self):
        node = TextNode("This is text without any images.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_split_nodes_image_single_image_at_beginning(self):
        node = TextNode("![alt text](url) This is text.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("alt text", TextType.IMAGE, "url"),
                TextNode(" This is text.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_image_single_image_at_end(self):
        node = TextNode("This is text. ![alt text](url)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text. ", TextType.TEXT),
                TextNode("alt text", TextType.IMAGE, "url"),
            ],
            new_nodes,
        )

    def test_split_nodes_image_single_image_in_middle(self):
        node = TextNode("This is text before ![alt text](url) and after.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text before ", TextType.TEXT),
                TextNode("alt text", TextType.IMAGE, "url"),
                TextNode(" and after.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_image_multiple_images(self):
        node = TextNode("Text ![img1](url1) more text ![img2](url2) end.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text ", TextType.TEXT),
                TextNode("img1", TextType.IMAGE, "url1"),
                TextNode(" more text ", TextType.TEXT),
                TextNode("img2", TextType.IMAGE, "url2"),
                TextNode(" end.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_image_consecutive_images(self):
        node = TextNode("Text ![img1](url1)![img2](url2) end.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text ", TextType.TEXT),
                TextNode("img1", TextType.IMAGE, "url1"),
                TextNode("img2", TextType.IMAGE, "url2"), # Note the empty text node
                TextNode(" end.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_image_with_other_markdown(self):
        node = TextNode("This is **bold** text with ![image](url).", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is **bold** text with ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "url"),
                TextNode(".", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_link_no_link(self):
        node = TextNode("This is text without any links.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_nodes_link_single_link_at_beginning(self):
        node = TextNode("[link text](url) This is text.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link text", TextType.LINK, "url"),
                TextNode(" This is text.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_link_single_link_at_end(self):
        node = TextNode("This is text. [link text](url)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text. ", TextType.TEXT),
                TextNode("link text", TextType.LINK, "url"),
            ],
            new_nodes,
        )

    def test_split_nodes_link_single_link_in_middle(self):
        node = TextNode("This is text before [link text](url) and after.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text before ", TextType.TEXT),
                TextNode("link text", TextType.LINK, "url"),
                TextNode(" and after.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_link_multiple_links(self):
        node = TextNode("Text [link1](url1) more text [link2](url2) end.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "url1"),
                TextNode(" more text ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "url2"),
                TextNode(" end.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_link_consecutive_links(self):
        node = TextNode("Text [link1](url1)[link2](url2) end.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "url1"),
                TextNode("link2", TextType.LINK, "url2"), # Note the empty text node
                TextNode(" end.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_link_with_other_markdown(self):
        node = TextNode("This is **bold** text with [link](url).", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is **bold** text with ", TextType.TEXT),
                TextNode("link", TextType.LINK, "url"),
                TextNode(".", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_image_and_link_combined(self):
        node = TextNode("Text with ![image](img_url) and [link](link_url).", TextType.TEXT)
        # Order matters here, the functions process the first found element
        # split_nodes_image will process the image first
        intermediate_nodes = split_nodes_image([node])
        final_nodes = split_nodes_link(intermediate_nodes)
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "img_url"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link", TextType.LINK, "link_url"),
                TextNode(".", TextType.TEXT),
            ],
            final_nodes,
        )

    def test_split_nodes_link_and_image_combined(self):
        node = TextNode("Text with [link](link_url) and ![image](img_url).", TextType.TEXT)
        # Order matters here, the functions process the first found element
        # split_nodes_link will process the link first
        intermediate_nodes = split_nodes_link([node])
        final_nodes = split_nodes_image(intermediate_nodes)
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("link", TextType.LINK, "link_url"),
                TextNode(" and ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "img_url"),
                TextNode(".", TextType.TEXT),
            ],
            final_nodes,
        )

if __name__ == '__main__':
    unittest.main()