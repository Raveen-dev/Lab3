import unittest
import price_info  # This imports your original code file

class TestPriceInfo(unittest.TestCase):

    def test_total_cost_shopping(self):
        # We know 5*1.20 + 5*1.40 + 1*6.50 + 2*2.70 + 10*0.90 + 1*2.95 + 2*4.95 = 49.75
        expected_total = 49.75
        actual_total = price_info.total_cost_shopping()
        
        # This checks if the actual function result matches our expected math
        self.assertAlmostEqual(actual_total, expected_total)

    def test_cost_of_fruit(self):
        # Test 10 apples: 10 * 1.20 = 12.0
        expected_fruit_cost = 12.0
        actual_fruit_cost = price_info.cost_of_fruits('apple', 10)
        
        self.assertAlmostEqual(actual_fruit_cost, expected_fruit_cost)

if __name__ == '__main__':
    unittest.main()