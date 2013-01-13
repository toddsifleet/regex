import re


class Tester(object):
    default = None
    regex = None
    results = None
    def __init__(self, regex = None, flags = 0):
        if regex is not None:
            self.regex = re.compile(regex, flags)

    def __call__(self, string, regex = None, flags = 0):
        if regex is not None:
            self.regex = re.compile(regex, flags)
        if self.regex is None:
            raise Exception("You must define a regex before or during your call")

        self.results = re.search(self.regex, string)
        return self

    def __getitem__(self, keys):
        keys = keys if isinstance(keys, tuple) else (keys, )
        return self._get_group_item(keys)

    def __getattr__(self, name):
        return self._get_group_item((name,))

    def _get_group_item(self, keys):
        #if we don't have any info we don't have to bother looking
        if not self.results:
            return self.default

        try:
            return self.results.group(*keys)
        except:
            return self.default

    def __nonzero__(self):
        return self.results is not None

if __name__ == '__main__':
    #create an instance with a regex string
    regex = Tester('^(?P<this>this) .* (?P<test>test)$')

    if regex('this is a test'):
        print "regex('this is a test'):\n\t Passes as expected"
        print "Access like a dictionary (regex['test']): \n\t%s" % regex['test']                
        print "Get more than one value (regex['test', 'this']): \n\t%s" % ', '.join(regex['test', 'this'])
        print "Access as an attribute (regex.test): \n\t%s" % regex.test
        print "Access as an index (regex[1]): \n\t%s" % regex[0]
        print "doesn't die, returns None (regex.does_not_exist):\n\t %s" % str(regex.does_not_exist)

    print "\nYou can even do it all in one go:"
    print "RegEx('^(?P<this>this) .* (?P<test>test)$')('this is a test').this: \n\t%s" % Tester('^(?P<this>this) .* (?P<test>test)$')('this is a test').this
    print "regex('this is a test').this: \n\t%s" % regex('this is a test').this

    if not regex('this is test that will fail!'):
        print "\nregex('this is test that will fail!'):\n\tFailed as expected"
        print "Old results are cleared out (regex['test']): \n\t%s" % regex['test']