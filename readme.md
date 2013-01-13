Python RegEx
=============

A simple wrapper around python's [re module](http://docs.python.org/2/library/re.html), that makes it a little easier to work with.  I really like the way perl handles regex so this wraps up something similar.

Usage
-------
    from regex import Tester
    regex = Tester('^(?P<this>this) .* (?P<test>test)$')

    if regex('this is a test'):
        print "Passes as expected"
        print "Found: %s" % regex.test


Why?
-------

So that you don't have to do:

    x = re.search('^(?P<this>this) .* (?P<test>test)$')
    if x is not None:
        print x.group('this')

So that you can:

-access results like a list, dictionary, or attribute

-get a default value back, on a missed match

-stop testing first, just grab the reuslt


Overall if you like working with regex in perl, this makes it easier in python.

License:
-------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
