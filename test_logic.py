import unittest
import logic
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_initialize(self):
        # test_initialize-01
        actual = logic.initialize()
        expected = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertEqual(np.testing.assert_array_equal(actual, expected), None)

    def test_add(self):
        # test_add-01
        actualMat = logic.add(np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
        actual = np.count_nonzero(actualMat == 2) + np.count_nonzero(actualMat == 4)
        expected = 1
        self.assertEqual(actual, expected)
        # test_add-02
        actualMat = logic.add(np.array([[2, 32, 0, 64], [8, 4, 4, 0], [1024, 0, 32, 2], [0, 4, 16, 4]]))
        actual = np.count_nonzero(actualMat == 2) + np.count_nonzero(actualMat == 4)
        expected = 7
        self.assertEqual(actual, expected)
        # test_add-03
        actualMat = logic.add(np.array([[2, 2, 2, 2], [4, 4, 0, 4], [2, 2, 2, 2], [4, 4, 4, 4]]))
        actual = np.count_nonzero(actualMat == 2) + np.count_nonzero(actualMat == 4)
        expected = 16
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
