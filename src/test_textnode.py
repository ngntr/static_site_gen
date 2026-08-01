import unittest
from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a node", TextType.BOLD, "google.de")
        node2 = TextNode("This is a node", TextType.BOLD, "google.de")
        self.assertEqual(node, node2)

    def test_n_eq(self):
        node = TextNode("This is a node", TextType.BOLD)
        node2 = TextNode("This is a node", TextType.BOLD, "google.de")
        self.assertNotEqual(node, node2)

    def test_eq_3(self):
        node = TextNode("This is a node", TextType.TEXT, None)
        node2 = TextNode("This is a node", TextType.TEXT)
        self.assertEqual(node2, node)

if __name__ == "__main__":
    unittest.main()
