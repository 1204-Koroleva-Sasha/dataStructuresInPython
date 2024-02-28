import unittest
from my_queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.my_queue = Queue()

    def tearDown(self):
        pass

    def test_is_empty(self):
        self.assertTrue(self.my_queue.is_empty())
        self.my_queue.queue = [1]
        self.assertFalse(self.my_queue.is_empty())

    def test_enqueue(self):
        self.my_queue.enqueue(2)
        self.assertEqual(self.my_queue.queue, [2])

        self.my_queue.enqueue(3)
        self.assertEqual(self.my_queue.queue, [2, 3])

    def test_dequeue(self):
        self.my_queue.queue = [1]
        self.my_queue.dequeue()
        self.assertEqual(self.my_queue.queue, [])

        self.my_queue.queue = [1, 2, 3]
        self.my_queue.dequeue()
        self.assertEqual(self.my_queue.queue, [2, 3])

        with self.assertRaises(Exception):
            self.my_queue.queue = []
            self.my_queue.dequeue()

    def test_peek_front(self):
        self.my_queue.queue = [1, 2, 3]
        self.assertEqual(self.my_queue.peek_front(), 1)

        self.my_queue.queue = [2, 3]
        self.assertEqual(self.my_queue.peek_front(), 2)

        with self.assertRaises(Exception):
            self.my_queue.queue = []
            self.my_queue.peek_front()


if __name__ == '__main__':
    unittest.main()