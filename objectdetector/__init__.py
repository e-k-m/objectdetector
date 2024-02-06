"""
Objekt detection in georeferenced arial images.

Example
-------
To use objectdetector from code, do:

import objectdetector
objectdetector.say('I love batman')

Or you can also the CLI and do:
objectdetector I love batman
"""

from objectdetector import version
from objectdetector.objectdetector import say

__author__ = "Eric Matti"
__version__ = version.__version__
__all__ = [say]
