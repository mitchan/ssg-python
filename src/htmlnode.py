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
        if self.children is not None:
            content = "".join(list(map(lambda x: f"{x}", self.children)))
        return (
            f"<{self.tag}{props if props == "" else " " + props}>{content}</{self.tag}>"
        )
