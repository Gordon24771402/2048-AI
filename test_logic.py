import unittest
import logic
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_initialize(self):
        # test_initialize-01
        actual = logic.initialize()
        expected = np.array([[0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]])
        self.assertEqual(np.testing.assert_array_equal(actual, expected), None)

    def test_add(self):
        # test_add-01
        actualMat = logic.add(np.array([[0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0]]))
        actual = np.count_nonzero(actualMat == 2) + np.count_nonzero(actualMat == 4)
        expected = 1
        self.assertEqual(actual, expected)
        # test_add-02
        actualMat = logic.add(np.array([[2, 32, 0, 64],
                                        [8, 4, 4, 0],
                                        [1024, 0, 32, 2],
                                        [0, 4, 16, 4]]))
        actual = np.count_nonzero(actualMat == 2) + np.count_nonzero(actualMat == 4)
        expected = 7
        self.assertEqual(actual, expected)
        # test_add-03
        actualMat = logic.add(np.array([[2, 2, 2, 2],
                                        [4, 4, 0, 4],
                                        [2, 2, 2, 2],
                                        [4, 4, 4, 4]]))
        actual = np.count_nonzero(actualMat == 2) + np.count_nonzero(actualMat == 4)
        expected = 16
        self.assertEqual(actual, expected)

    def test_check_state(self):
        # test_check_state-01 (all zeros)
        actualMat = np.array([[0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0]])
        actual = logic.check_state(actualMat)
        expected = "CONTINUE"
        self.assertEqual(actual, expected)
        # test_check_state-02 (none zero + none merge)
        actualMat = np.array([[2, 4, 2, 4],
                              [4, 2, 4, 2],
                              [8, 32, 8, 16],
                              [16, 8, 2, 8]])
        actual = logic.check_state(actualMat)
        expected = "LOSE"
        self.assertEqual(actual, expected)
        # test_check_state-03 (2048 is at actualMat[2][1])
        actualMat = np.array([[2, 4, 2, 4],
                              [4, 2, 4, 2],
                              [8, 2048, 8, 16],
                              [16, 8, 2, 8]])
        actual = logic.check_state(actualMat)
        expected = "WON"
        self.assertEqual(actual, expected)
        # test_check_state-04 (actualMat[1][1] merges with actualMat[1][2])
        actualMat = np.array([[2, 8, 2, 4],
                              [32, 4, 4, 2],
                              [8, 32, 8, 16],
                              [16, 8, 2, 8]])
        actual = logic.check_state(actualMat)
        expected = "CONTINUE"
        self.assertEqual(actual, expected)
        # test_check_state-05 (actualMat[1][2] merges with actualMat[2][2])
        actualMat = np.array([[2, 4, 2, 4],
                              [4, 2, 8, 2],
                              [8, 32, 8, 16],
                              [16, 8, 2, 8]])
        actual = logic.check_state(actualMat)
        expected = "CONTINUE"
        self.assertEqual(actual, expected)
        # test_check_state-06 (zero is at actualMat[1][1])
        actualMat = np.array([[2, 4, 2, 4],
                              [4, 0, 4, 2],
                              [8, 32, 8, 16],
                              [16, 8, 2, 8]])
        actual = logic.check_state(actualMat)
        expected = "CONTINUE"
        self.assertEqual(actual, expected)
        # test_check_state-07 (actualMat[0][1] merges with actualMat[0][2])
        actualMat = np.array([[2, 4, 4, 4],
                              [4, 2, 4, 2],
                              [8, 32, 8, 16],
                              [16, 8, 2, 8]])
        actual = logic.check_state(actualMat)
        expected = "CONTINUE"
        self.assertEqual(actual, expected)
        # test_check_state-08 (actualMat[3][1] merges with actualMat[3][2])
        actualMat = np.array([[2, 4, 2, 4],
                              [4, 2, 4, 2],
                              [8, 32, 8, 16],
                              [16, 2, 2, 8]])
        actual = logic.check_state(actualMat)
        expected = "CONTINUE"
        self.assertEqual(actual, expected)
        # test_check_state-08 (actualMat[1][3] merges with actualMat[2][3])
        actualMat = np.array([[2, 4, 2, 4],
                              [4, 2, 4, 2],
                              [8, 32, 8, 2],
                              [16, 4, 2, 8]])
        actual = logic.check_state(actualMat)
        expected = "CONTINUE"
        self.assertEqual(actual, expected)
        # test_check_state-09 (actualMat[1][0] merges with actualMat[2][0])
        actualMat = np.array([[2, 4, 2, 4],
                              [8, 2, 4, 2],
                              [8, 32, 8, 16],
                              [16, 8, 2, 8]])
        actual = logic.check_state(actualMat)
        expected = "CONTINUE"
        self.assertEqual(actual, expected)

    def test_left(self):
        # test_left-01
        actualMat = np.array([[0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0]])
        actual = logic.left(actualMat)
        expected = np.array([[0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]])
        self.assertEqual(np.testing.assert_array_equal(actual, expected), None)
        # test_left-02
        actualMat = np.array([[2, 4, 8, 16],
                              [16, 8, 4, 2],
                              [4, 16, 2, 8],
                              [8, 2, 16, 4]])
        actual = logic.left(actualMat)
        expected = np.array([[2, 4, 8, 16],
                              [16, 8, 4, 2],
                              [4, 16, 2, 8],
                              [8, 2, 16, 4]])
        self.assertEqual(np.testing.assert_array_equal(actual, expected), None)
        # test_left-03
        actualMat = np.array([[0, 2, 0, 2],
                              [2, 0, 2, 0],
                              [0, 0, 0, 2],
                              [2, 0, 0, 0]])
        actual = logic.left(actualMat)
        expected = np.array([[4, 0, 0, 0],
                             [4, 0, 0, 0],
                             [2, 0, 0, 0],
                             [2, 0, 0, 0]])
        self.assertEqual(np.testing.assert_array_equal(actual, expected), None)
        # test_left-04
        actualMat = np.array([[2, 2, 2, 2],
                              [0, 0, 0, 2],
                              [2, 0, 0, 2],
                              [0, 0, 0, 0]])
        actual = logic.left(actualMat)
        expected = np.array([[4, 4, 0, 0],
                             [2, 0, 0, 0],
                             [4, 0, 0, 0],
                             [0, 0, 0, 0]])
        self.assertEqual(np.testing.assert_array_equal(actual, expected), None)
        # test_left-05
        actualMat = np.array([[2, 0, 2, 2],
                              [2, 2, 0, 2],
                              [0, 0, 2, 2],
                              [2, 2, 0, 0]])
        actual = logic.left(actualMat)
        expected = np.array([[4, 2, 0, 0],
                             [4, 2, 0, 0],
                             [4, 0, 0, 0],
                             [4, 0, 0, 0]])
        self.assertEqual(np.testing.assert_array_equal(actual, expected), None)
        # test_left-06
        actualMat = np.array([[4, 4, 2, 2],
                              [2, 2, 4, 2],
                              [0, 8, 0, 4],
                              [8, 4, 4, 0]])
        actual = logic.left(actualMat)
        expected = np.array([[8, 4, 0, 0],
                             [4, 4, 2, 0],
                             [8, 4, 0, 0],
                             [8, 8, 0, 0]])
        self.assertEqual(np.testing.assert_array_equal(actual, expected), None)



if __name__ == '__main__':
    unittest.main()
