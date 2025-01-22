import unittest
from apriori import apriori

class TestApriori(unittest.TestCase):
    def test_apriori(self):
        dataset = [[1, 2, 3], [1, 3, 4], [2, 3, 5]]
        result = apriori(dataset, min_support=2)
        self.assertIn([1, 3], result)

if __name__ == "__main__":
    unittest.main()
