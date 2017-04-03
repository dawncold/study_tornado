# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division

instance = None


class Sig(object):

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        global instance
        if instance is None:
            instance = cls()
        return instance


class Sig2(object):

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if not hasattr(Sig2, '_instance'):
            Sig2._instance = cls()
        return Sig2._instance

if __name__ == '__main__':

    sig1 = Sig.instance()
    sig2 = Sig.instance()

    print(id(sig1))
    print(id(sig2))

    sig3 = Sig2.instance()
    sig4 = Sig2.instance()

    print(id(sig3))
    print(id(sig4))
