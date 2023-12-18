"""The mix-in class implementation for the CSS line-height property.
"""

from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class TextLineHeightCssMixIn(
    AttrLinkingMixIn,
):
    _line_height: Number

    def _initialize_line_height(self) -> None:
        """
        Initialize the `_line_height` attribute.
        """
        if hasattr(self, "_line_height"):
            return
        self._line_height = Number(1.5)

    @property
    def line_height(self) -> Number:
        """
        Get a line-height value.

        Returns
        -------
        line_height : Number
            A line-height value.
        """
        self._initialize_line_height()
        return self._line_height

    @line_height.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    def line_height(self, value: Number) -> None:
        """
        Update a line-height value.

        Parameters
        ----------
        value : Number
            A line-height value.
        """
        from apysc._display.css_interface import CssInterface
        from apysc._validation import display_validation

        self._initialize_line_height()
        interface: CssInterface = display_validation.validate_css_interface(
            instance=self
        )
        self._line_height = value
        interface.set_css(
            name="line-height",
            value=self._line_height.to_string(),
        )

        self._append_applying_new_attr_val_exp(
            new_attr=self._line_height, attr_name="line_height"
        )
        self._append_attr_to_linking_stack(
            attr=self._line_height, attr_name="line_height"
        )
