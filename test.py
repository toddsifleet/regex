from regex import Tester
import unittest

class TesterTestCase(unittest.TestCase):
    pos_string = 'this is a test'
    neg_string = 'bob barker'
    def setUp(self):
        #create an instance with a regex string
        self.regex = Tester('^(?P<this>this) .* (?P<test>test)$')
        self.regex(self.pos_string)

    def testReturnsTheCorrectBooeleanValue(self):
        assert self.regex(self.pos_string)
        assert not self.regex(self.neg_string)

    def testAccessLikeADict(self):
        self.assertEqual(self.regex['test'], 'test')

    def testAccessMoreThanOneValue(self):
        result = self.regex['test', 'this']
        self.assertEqual(result, ('test', 'this'))

    def testAccessAsAttribute(self):
        self.assertEqual(self.regex.test, 'test')

    def testAccessByIndex(self):
        self.assertEqual(self.regex[1], 'this')

    def testAccessAsEmptyAttribute(self):
        self.assertEqual(self.regex.goose, None)

    def testClearPreviousResults(self):
        self.regex(self.neg_string)
        self.assertEqual(self.regex['test'], None)

if __name__ == '__main__':
    unittest.main()
