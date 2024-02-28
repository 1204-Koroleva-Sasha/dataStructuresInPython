import unittest
from list import List


class TestList(unittest.TestCase):

    def setUp(self):
        self.my_list = List()

    def tearDown(self):
        self.my_list.clear()

    def test_is_empty(self):
        self.assertTrue(self.my_list.is_empty())
        self.my_list.list = [1]
        self.assertFalse(self.my_list.is_empty())

    def test_get_length(self):
        self.assertEqual(self.my_list.get_length(), 0)

        self.my_list.list = [1]
        self.assertEqual(self.my_list.get_length(), 1)

    def test_insert(self):

        self.my_list.insert(1, 0)
        self.assertEqual(self.my_list.list[0], 0)

        self.my_list.insert(2, 0)
        self.assertEqual(self.my_list.list, [0, 0])

        with self.assertRaises(Exception):
            self.my_list.insert(0, 1)

        with self.assertRaises(Exception):
            self.my_list.insert(4, 0)

    def test_remove(self):
        self.my_list.list = [0]
        self.my_list.remove(1)
        self.assertEqual(self.my_list.list,  [])

        self.my_list.list = [1, 2, 3]
        self.my_list.remove(2)
        self.assertEqual(self.my_list.list, [1, 3])

        with self.assertRaises(Exception):
            self.my_list.remove(0)

        with self.assertRaises(Exception):
            self.my_list.remove(5)

    def test_get_entry(self):
        self.my_list.list = [3]
        self.assertEqual(self.my_list.get_entry(1), 3)

        with self.assertRaises(Exception):
            self.my_list.get_entry(2)

        with self.assertRaises(Exception):
            self.my_list.get_entry(0)

    def test_replace(self):
        self.my_list.list = [0]
        self.my_list.replace(1, 3)
        self.assertEqual(self.my_list.list, [3])

        self.my_list.list = [1, 2, 3]
        self.my_list.replace(2, 4)
        self.assertEqual(self.my_list.list, [1, 4, 3])

        with self.assertRaises(Exception):
            self.my_list.replace(0, 5)

        with self.assertRaises(Exception):
            self.my_list.replace(4, 2)

    def test_clear(self):
        self.my_list.list = [0]
        self.my_list.clear()
        self.assertEqual(self.my_list.list, [])


if __name__ == '__main__':
    unittest.main()
