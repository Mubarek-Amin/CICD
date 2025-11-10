import unittest
from hello import hello_world

class testHello(unittest.TestCase):
    def test(self):
        self.assertEqual(hello_world(), "hello world")


if __name__ == "__main__":
    unittest.main()