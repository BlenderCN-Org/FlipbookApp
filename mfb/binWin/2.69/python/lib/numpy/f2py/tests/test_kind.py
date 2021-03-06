import os
import math

from numpy.testing import *
from numpy import array

import util

def _path(*a):
    return os.path.join(*((os.path.dirname(__file__),) + a))

from numpy.f2py.crackfortran import _selected_int_kind_func as selected_int_kind
from numpy.f2py.crackfortran import _selected_real_kind_func as selected_real_kind

class TestKind(util.F2PyTest):
    sources = [_path('src', 'kind', 'foo.f90'),
               ]

    @dec.slow
    def test_all(self):
        selectedrealkind = self.module.selectedrealkind
        selectedintkind = self.module.selectedintkind

        for i in range(40):
            assert_(selectedintkind(i) in [selected_int_kind(i),-1],\
                    'selectedintkind(%s): expected %r but got %r' %  (i, selected_int_kind(i), selectedintkind(i)))

        for i in range(20):
            assert_(selectedrealkind(i) in [selected_real_kind(i),-1],\
                    'selectedrealkind(%s): expected %r but got %r' %  (i, selected_real_kind(i), selectedrealkind(i)))

if __name__ == "__main__":
    import nose
    nose.runmodule()
