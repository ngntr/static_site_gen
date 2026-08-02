import unittest
from htmlnode import HTMLNode

class Tests(unittest.TestCase):
    def test_1(self):
        node = HTMLNode()
        node_2 = HTMLNode(None,None,None,None)
        self.assertEqual(node,node_2)

    def test_2(self):
        node = HTMLNode("a","xxx",None,{"p":"test"})
        node_2 = HTMLNode()
        self.assertNotEqual(node_2, node)
        