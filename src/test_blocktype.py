import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_empty_block(self):
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(None), BlockType.PARAGRAPH)

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```code here```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```python\nprint('hello')\n```"), BlockType.CODE)

    def test_quote_block(self):
        self.assertEqual(block_to_block_type(">This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> Multi-line\n> quote"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("* List item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("- List item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("+ List item"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("2. Second item"), BlockType.ORDERED_LIST)

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Heading 4"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Heading 5"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("Regular text"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Text with #no space"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("1 Starting with number"), BlockType.PARAGRAPH)

if __name__ == '__main__':
    unittest.main()