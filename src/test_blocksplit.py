import unittest
from splitblocks import split_blocks

class TestSplitBlocks(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(split_blocks(""), [])

    def test_single_paragraph(self):
        text = "This is a simple paragraph."
        expected = ["This is a simple paragraph."]
        self.assertEqual(split_blocks(text), expected)

    def test_multiple_paragraphs(self):
        text = "First paragraph.\n\nSecond paragraph."
        expected = ["First paragraph.", "Second paragraph."]
        self.assertEqual(split_blocks(text), expected)

    def test_headers(self):
        text = "# Header 1\n\n## Header 2"
        expected = ["# Header 1", "## Header 2"]
        self.assertEqual(split_blocks(text), expected)

    def test_mixed_content(self):
        text = "# Title\n\nSome text.\n\n- List item 1\n- List item 2"
        expected = ["# Title", "Some text.", "- List item 1\n- List item 2"]
        self.assertEqual(split_blocks(text), expected)

if __name__ == '__main__':
    unittest.main()