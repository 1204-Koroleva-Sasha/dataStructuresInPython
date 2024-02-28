import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.my_stack = Stack()

    def tearDown(self):
        pass

    def test_push(self):
        self.my_stack.push(1)
        self.assertEqual(self.my_stack.stack, [1])

        self.my_stack.push(2)
        self.assertEqual(self.my_stack.stack, [1, 2])

    def test_pop(self):
        self.my_stack.stack = [1]
        self.my_stack.pop()
        self.assertEqual(self.my_stack.stack, [])

        self.my_stack.stack = [1, 2]
        self.my_stack.pop()
        self.assertEqual(self.my_stack.stack, [1])

        with self.assertRaises(Exception):
            self.my_stack.stack = []
            self.my_stack.pop()

    def test_peek(self):
        self.my_stack.stack = [1]
        self.assertEqual(self.my_stack.peek(), 1)

        self.my_stack.stack = [1, 2]
        self.assertEqual(self.my_stack.peek(), 2)

        with self.assertRaises(Exception):
            self.my_stack.stack = []
            self.my_stack.peek()

    def test_is_empty(self):
        self.assertTrue(self.my_stack.is_empty())
        self.my_stack.stack = [1]
        self.assertFalse(self.my_stack.is_empty())


if __name__ == '__main__':
    unittest.main()
