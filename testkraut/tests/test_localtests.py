# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the testkraut package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""Dog food!

This is Testkraut's own unit test interface to serve the local SPECs within
the unit tests battery as actual test cases.
"""
import os
import logging
import os.path as op

if 'TESTKRAUT_LOGGER_VERBOSE' in os.environ:
    lgr = logging.getLogger('testkraut')
    console = logging.StreamHandler()
    lgr.addHandler(console)
    cfg = os.environ['TESTKRAUT_LOGGER_VERBOSE']
    if cfg == 'debug':
        lgr.setLevel(logging.DEBUG)

from testkraut.testcase import TestFromSPEC, discover_specs, template_case, TemplateTestCase

class LocalDogFoodTests(TestFromSPEC):
    __metaclass__ = TemplateTestCase
    @template_case(discover_specs([op.join(op.dirname(__file__),
                                           'localtests')]))
    def _run_spec_test(self, spec_filename):
        return TestFromSPEC._run_spec_test(self, spec_filename)
