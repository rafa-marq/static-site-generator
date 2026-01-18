import unittest
from htmlnode import HTMLNode, LeafNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_repr(self):
        node = LeafNode(tag="h1", value="Title", props={"class": "primary"})
        self.assertEqual(
            repr(node),
            "HTMLNode(h1, Title, {'class': 'primary'})"
        )
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()