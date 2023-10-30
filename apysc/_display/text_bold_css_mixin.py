"""The mix-in class implementation for the CSS bold (font-weight) property.
"""

from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.boolean import Boolean


class TextBoldCssMixIn(
    AttrLinkingMixIn,
):
    _bold: Boolean

    def _initialize_bold(self) -> None:
        """
        Initialize the `_bold` attribute.
        """
        if hasattr(self, "_bold"):
            return
        self._bold = Boolean(False)

    @property
    def bold(self) -> Boolean:
        """
        Get a bold (font-weight) value.

        Returns
        -------
        bold : Boolean
            A bold (font-weight) value.
        """
        self._initialize_bold()
        return self._bold._copy()

    @bold.setter
    def bold(self, value: Boolean) -> None:
        """
        Set a bold (font-weight) value.

        Parameters
        ----------
        value : Boolean
            A bold (font-weight) value.
        """
        from apysc._branch._else import Else
        from apysc._branch._if import If
        from apysc._display.css_interface import CssInterface
        from apysc._validation import display_validation

        interface: CssInterface = display_validation.validate_css_interface(
            instance=self
        )
        self._bold = value

        with If(self._bold):
            interface.set_css(
                name="font-weight",
                value="bold",
            )
        with Else():
            interface.set_css(
                name="font-weight",
                value="normal",
            )

        self._append_applying_new_attr_val_exp(new_attr=self._bold, attr_name="bold")
        self._append_attr_to_linking_stack(attr=self._bold, attr_name="bold")
