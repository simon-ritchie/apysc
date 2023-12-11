"""The class implementation for the `True_` constant.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.bool_const_mixin import BoolConstMixIn
from apysc._type.boolean import Boolean


class _True(
    BoolConstMixIn,
    Boolean,
):
    _value: bool = True

    @final
    @add_debug_info_setting(module_name=__name__)
    def __init__(self) -> None:
        """
        The class implementation for the `True_` constant.

        References
        ----------
        - True_ and False_ constants
            - https://simon-ritchie.github.io/apysc/en/true_and_false.html
        """
        super(_True, self).__init__(
            value=True,
            variable_name_suffix="true",
        )
