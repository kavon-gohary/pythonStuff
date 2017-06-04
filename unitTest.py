import cube as c
import unittest

class myTest(unittest.TestCase):

    def testCube(self):
        result = c.cube(3)
        expected = 27
        self.assertEqual(result,expected)
        self.assertEqual(c.cube(3), 27)        #these two assertEqual statements are equivalent. just different ways of writing the same test

    def testTRI(self):
        result = c.triArea(4, 4)
        expected = 8
        self.assertEqual(result, expected)
        self.assertEqual(c.triArea(4,4), 8)

#run the tests
if __name__ == '__main__':
    unittest.main()             #run the test
