import unittest
import logic


class MyTestCase(unittest.TestCase):
    def test_initialize(self):
        self.assertEqual(
            logic.initialize().all(),
            logic.np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]).all())


if __name__ == '__main__':
    unittest.main()
