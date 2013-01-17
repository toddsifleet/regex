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

see LICENSE