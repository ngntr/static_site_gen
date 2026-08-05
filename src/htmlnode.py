class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list["HTMLNode"] = None, props: dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = ""
        for key in self.props:
            result += f"{key}={self.props[key]} "
        return result[:-1]

    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        elif self.tag is None:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.props})"

        