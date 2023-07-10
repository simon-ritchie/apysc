"""The class implementation for the `False_` constant.
"""

from typing_extensions import Final, final

from apysc._type.boolean import Boolean
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.bool_const_mixin import BoolConstMixIn


class _False(
    BoolConstMixIn,
    Boolean,
):

    _value: Final[bool] = False

    @final
    @add_debug_info_setting(module_name=__name__)
    def __init__(self) -> None:
        """
        The class implementation for the `False_` constant.
        """
        super(_False, self).__init__(
            value=False,
            variable_name_suffix="false",
        )


False_: Final[_False] = _False()
