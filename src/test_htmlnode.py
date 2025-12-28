import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="div",
            value="Hello, world!",
            children=None,
            props={"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"'
        )

    def test_values(self):
        node = HTMLNode(tag="p", value="Hello World")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode(tag="h1", value="Title", children=None, props={"class": "primary"})
        self.assertEqual(
            repr(node),
            "HTMLNode(h1, Title, children: None, {'class': 'primary'})"
        )


if __name__ == "__main__":
    unittest.main()