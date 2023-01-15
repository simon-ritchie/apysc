"""Class implementations for now-related mix-in.
"""

from datetime import datetime
from typing import TYPE_CHECKING

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._time.datetime_ import DateTime


class NowMixIn:
    @classmethod
    @final
    @add_debug_info_setting(module_name=__name__)
    def now(cls, *, variable_name_suffix: str = "") -> "DateTime":
        """
        Get a `DateTime` instance of the current time.

        Parameters
        ----------
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        dt : DateTime
            A created `DateTime` instance.

        References
        ----------
        - DateTime class now interface
            - https://simon-ritchie.github.io/apysc/en/datetime_now.html

        Examples
        --------
        >>> from datetime import datetime
        >>> import apysc as ap
        >>> py_now: datetime = datetime.now()
        >>> ap_now: ap.DateTime = ap.DateTime.now()
        >>> ap_now.year == py_now.year
        Boolean(True)
        >>> ap_now.month == py_now.month
        Boolean(True)
        >>> ap_now.day == py_now.day
        Boolean(True)
        """
        from apysc._time.datetime_ import DateTime

        now_: datetime = datetime.now()
        dt: DateTime = DateTime(
            year=1970,
            month=1,
            day=1,
            variable_name_suffix=variable_name_suffix,
        )
        dt._year._value = now_.year
        dt._month._value = now_.month
        dt._day._value = now_.day
        dt._hour._value = now_.hour
        dt._minute._value = now_.minute
        dt._second._value = now_.second
        _append_now_expression(dt=dt)
        return dt


@final
@add_debug_info_setting(module_name=__name__)
@arg_validation_decos.is_apysc_datetime(arg_position_index=0)
def _append_now_expression(*, dt: "DateTime") -> None:
    """
    Append a `now` interface expression string.

    Parameters
    ----------
    dt : DateTime
        A target `DateTime` instance.
    """
    import apysc as ap

    expression: str = f"{dt.variable_name} = new Date();"
    ap.append_js_expression(expression=expression)
