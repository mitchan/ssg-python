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
        attributes = []
        for key in self.props:
            attributes.append(f'{key}="{self.props[key]}"')
        return " ".join(attributes)

    def __repr__(self):
        props = self.props_to_htlm()
        content = ""
        if self.value is not None:
            content = self.value
        return (
            f"<{self.tag}{props if props == "" else " " + props}>{content}</{self.tag}>"
        )


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
        if self.children is not None:
            content = "".join(list(map(lambda x: x.to_html(), self.children)))

        props = self.props_to_htlm()

        return (
            f"<{self.tag}{props if props == "" else " " + props}>{content}</{self.tag}>"
        )
