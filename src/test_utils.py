import unittest

from textnode import TextNode, TextType
from utils import split_nodes_delimiter


class TestSplitNodesDelimeter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_bold_and_italic(self):
        node = TextNode(
            "This is text with **bold text** and _italic text_", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic text", TextType.ITALIC),
            ],
        )
