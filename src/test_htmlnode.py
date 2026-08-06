import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class Tests(unittest.TestCase):
    def test_1(self):
        node = HTMLNode()
        node_2 = HTMLNode(None,None,None,None)
        self.assertEqual(node,node_2)

    def test_2(self):
        node = HTMLNode("a","xxx",None,{"p":"test"})
        node_2 = HTMLNode()
        self.assertNotEqual(node_2, node)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_2(self):
        node = LeafNode("p",None)
        self.assertRaises(ValueError,node.to_html)

    def test_leaf_3(self):
        node = LeafNode(None,"Test")
        self.assertEqual(node.to_html(), "Test")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
