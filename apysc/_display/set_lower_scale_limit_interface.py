"""
This module is for the lower scale limit's setter interface class.
"""

from apysc._type.number import Number


class SetLowerScaleLimitInterface:

    def _set_lower_scale_limit(self, *, value: Number) -> None:
        """
        Set the lower scale limit to a specified value.

        Parameters
        ----------
        value : Number
            A value to apply the lower scale limit.
        """
        import apysc as ap
        with ap.If(value < 0.01):
            value.value = ap.Number(0.01)
