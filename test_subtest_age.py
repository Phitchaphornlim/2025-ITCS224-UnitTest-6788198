import unittest
from age import categorize_by_age

class TestSubtestAge(unittest.TestCase):

    def test_child(self):
        for age in range(0, 10):  # 0–9
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Child")

    def test_adolescent(self):
        for age in range(10, 19):  # 10–18
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adolescent")

    def test_adult(self):
        for age in range(19, 66):  # 19–65
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adult")

if __name__ == "__main__":
    unittest.main(verbosity=2)