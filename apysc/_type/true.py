"""The class implementation for the `True` constant.
"""

from typing_extensions import Final, final

from apysc._type.boolean import Boolean
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.bool_const_mixin import BoolConstMixIn


class _True(
    BoolConstMixIn,
    Boolean,
):

    _value: Final[bool] = True

    @final
    @add_debug_info_setting(module_name=__name__)
    def __init__(self) -> None:
        """
        The class implementation for the `True` constant.
        """
        super(_True, self).__init__(
            value=True,
            variable_name_suffix="true",
        )


True_: Final[_True] = _True()
