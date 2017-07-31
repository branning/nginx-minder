#!/usr/bin/env python3
#
#

import os
import pytest

os.chdir('/usr/local/bin')
from nginx_minder import *

def test_nothing():
    return True
