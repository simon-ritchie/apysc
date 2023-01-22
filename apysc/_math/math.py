"""Class implementation for the math-related interfaces.
"""

from apysc._math.max_mixin import MaxMixIn
from apysc._math.min_mixin import MinMixIn
from apysc._math.trunc_mixin import TruncMixIn


class Math(TruncMixIn, MinMixIn, MaxMixIn):
    """Class implementation for the math-related interfaces."""
