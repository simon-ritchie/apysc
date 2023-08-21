"""
This module is for the lower scale limit's setter interface class.
"""

from typing_extensions import final

from apysc._type.number import Number

MIN_SCALE: float = 0.00000001


class SetLowerScaleLimitMixIn:
    @final
    def _set_lower_scale_limit(self, *, value: Number) -> None:
        """
        Set the lower scale limit to a specified value.

        Parameters
        ----------
        value : Number
            A value to apply the lower scale limit.
        """
        from apysc._branch._if import If

        with If(value < MIN_SCALE, locals_=locals()):
            value.value = Number(MIN_SCALE)
