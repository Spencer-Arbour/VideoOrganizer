# This is needed so the tests can be run from run_tests.sh with the proper imports
import sys
from os.path import abspath, dirname, join

sys.path.append(abspath(join(dirname(dirname(__file__)), "src")))
