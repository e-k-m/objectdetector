import unittest

import objectdetector


class TestSay(unittest.TestCase):
    def test_say(self):
        message = "I love batman"
        self.assertTrue(message in objectdetector.say(message))


if __name__ == "__main__":
    unittest.main()
