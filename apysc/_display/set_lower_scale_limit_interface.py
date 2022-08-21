"""
This module is for the lower scale limit's setter interface class.
"""

from typing_extensions import final

from apysc._type.number import Number

MIN_SCALE: float = 0.00000001


class SetLowerScaleLimitInterface:
    @final
    def _set_lower_scale_limit(self, *, value: Number) -> None:
        """
        Set the lower scale limit to a specified value.

        Parameters
        ----------
        value : Number
            A value to apply the lower scale limit.
        """
        import apysc as ap

        with ap.If(value < MIN_SCALE, locals_=locals()):
            value.value = ap.Number(MIN_SCALE)
