# Expected folder structure
#
# ./project
#   src/
#   tests/
#
# Put this file inside ./project/tests
#
# Then, for every test file inside ./project/tests:
# from src.package import function
#
# Original source: https://docs.python-guide.org/writing/structure/#test-suite
# Adapted by https://github.com/jotafeldmann
# https://gist.github.com/jotafeldmann/e8ee40be849afb3260936d78f543db0e

import os
import sys
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')))


file_path = './data/pokemon.csv'
