import unittest

from htmlnode import HtmlNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType


class TestHtmlNode(unittest.TestCase):
    def test_p_with_value(self):
        node = HtmlNode(tag="p", value="this is a paragraph")
        self.assertEqual(f"{node}", "<p>this is a paragraph</p>")

    def test_link(self):
        node = HtmlNode(
            tag="a",
            value="boot.dev",
            props={"href": "https://boot.dev", "target": "_blank"},
        )
        self.assertEqual(
            f"{node}", '<a href="https://boot.dev" target="_blank">boot.dev</a>'
        )


class TestHtmlLeaf(unittest.TestCase):
    def test_no_tag(self):
        leaf = LeafNode("this is a text")
        self.assertEqual("this is a text", leaf.to_html())

    def test_paragraph(self):
        leaf = LeafNode(value="this is a paragraph", tag="p", props={"class": "mb-4"})
        self.assertEqual('<p class="mb-4">this is a paragraph</p>', leaf.to_html())

    def test_no_value_exception(self):
        leaf = LeafNode(value=None)
        self.assertRaises(ValueError, leaf.to_html)


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode(tag="span", value="child")
        parent_node = ParentNode(tag="div", children=[child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode(tag="b", value="grandchild")
        child_node = ParentNode(tag="span", children=[grandchild_node])
        parent_node = ParentNode(tag="div", children=[child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertDictEqual(html_node.props, {"href": "https://boot.dev"})

    def test_image(self):
        node = TextNode(
            "This is an image", TextType.IMAGE, "https://boot.dev/example.png"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertDictEqual(
            html_node.props,
            {"src": "https://boot.dev/example.png", "alt": "This is an image"},
        )


if __name__ == "__main__":
    unittest.main()
