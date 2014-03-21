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

