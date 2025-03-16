import unittest

from htmlnode import HtmlNode, LeafNode


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

    def test_children(self):
        p = HtmlNode(tag="p", value="this is a paragraph")
        span = HtmlNode(tag="span", value="this is a span")

        parent = HtmlNode(tag="div", children=[p, span])
        self.assertEqual(
            f"{parent}",
            "<div><p>this is a paragraph</p><span>this is a span</span></div>",
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


if __name__ == "__main__":
    unittest.main()
