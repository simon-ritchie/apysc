"""The class implementation for the `False_` constant.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.bool_const_mixin import BoolConstMixIn
from apysc._type.boolean import Boolean


class _False(
    BoolConstMixIn,
    Boolean,
):
    _value: bool = False

    @final
    @add_debug_info_setting(module_name=__name__)
    def __init__(self) -> None:
        """
        The class implementation for the `False_` constant.

        References
        ----------
        - True_ and False_ constants
            - https://simon-ritchie.github.io/apysc/en/true_and_false.html
        """
        super(_False, self).__init__(
            value=False,
            variable_name_suffix="false",
        )
