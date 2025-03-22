from textnode import TextType


class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_htlm(self):
        if self.props is None:
            return ""
        html_props = ""
        for key in self.props:
            html_props += f' {key}="{self.props[key]}"'
        return html_props

    def __repr__(self):
        content = ""
        if self.value is not None:
            content = self.value
        return f"<{self.tag}{self.props_to_htlm()}>{content}</{self.tag}>"


class LeafNode(HtmlNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be None")
        if self.tag is None:
            return self.value
        return f"{self}"


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag cannot be None")
        if self.children is None:
            raise ValueError("children cannot be None")

        content = ""
        for child in self.children:
            content += child.to_html()

        return f"<{self.tag}{self.props_to_htlm()}>{content}</{self.tag}>"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(
                tag="a", value=text_node.text, props={"href": text_node.url}
            )
        case TextType.IMAGE:
            return LeafNode(
                tag="img", value="", props={"src": text_node.url, "alt": text_node.text}
            )
        case _:
            raise ValueError(f"Invalid type: {text_node.text_type}")
