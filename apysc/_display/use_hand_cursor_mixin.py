"""The mix-in class implementation for the `use_hand_cursor` setting.
"""

from apysc._type.boolean import Boolean


class UseHandCursorMixIn:
    _use_hand_cursor: Boolean

    def _initialize_use_hand_cursor(self) -> None:
        """
        Initialize the `_use_hand_cursor` attribute if it hasn't been
        initialized yet.
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if hasattr(self, "_use_hand_cursor"):
            return

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="use_hand_cursor"
        )
        self._use_hand_cursor = Boolean(False, variable_name_suffix=suffix)

    @property
    def use_hand_cursor(self) -> Boolean:
        """
        Get a boolean value whether to use the hand cursor
        when the mouse pointer is over this instance.

        Returns
        -------
        use_hand_cursor : Boolean
            Whether to use the hand cursor or not.
        """
        self._initialize_use_hand_cursor()
        return self._use_hand_cursor.copy()

    @use_hand_cursor.setter
    def use_hand_cursor(self, value: Boolean) -> None:
        """
        Set a boolean value whether to use the hand cursor
        when the mouse pointer is over this instance.

        Parameters
        ----------
        value : Boolean
            Boolean value to set.
        """
        from apysc._branch._else import Else
        from apysc._branch._if import If
        from apysc._display.css_interface import CssInterface
        from apysc._validation.display_validation import validate_css_interface

        self._initialize_use_hand_cursor()
        self._use_hand_cursor.value = value
        self_instance: CssInterface = validate_css_interface(instance=self)
        with If(self._use_hand_cursor):
            self_instance.set_css(name="cursor", value="pointer")
        with Else():
            self_instance.set_css(name="cursor", value="auto")
