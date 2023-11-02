"""The mix-in class implementation for the CSS italic (font-style) property.
"""

from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.boolean import Boolean
from apysc._validation import arg_validation_decos


class TextItalicCssMixIn(
    AttrLinkingMixIn,
):
    _italic: Boolean

    def _initialize_italic(self) -> None:
        """
        Initialize the `_italic` attribute.
        """
        if hasattr(self, "_italic"):
            return
        self._italic = Boolean(False)

    @property
    def italic(self) -> Boolean:
        """
        Get an italic (font-style) value.

        Returns
        -------
        italic : Boolean
            A italic (font-style) value.
        """
        self._initialize_italic()
        return self._italic._copy()

    @italic.setter
    @arg_validation_decos.is_apysc_boolean(arg_position_index=1)
    def italic(self, value: Boolean) -> None:
        """
        Set an italic (font-style) value.

        Parameters
        ----------
        value : Boolean
            An italic (font-style) value.
        """
        from apysc._branch._else import Else
        from apysc._branch._if import If
        from apysc._display.css_interface import CssInterface
        from apysc._validation import display_validation

        self._initialize_italic()
        interface: CssInterface = display_validation.validate_css_interface(
            instance=self
        )
        self._italic = value

        with If(self._italic):
            interface.set_css(
                name="font-style",
                value="italic",
            )
        with Else():
            interface.set_css(
                name="font-style",
                value="normal",
            )

        self._append_applying_new_attr_val_exp(
            new_attr=self._italic, attr_name="italic"
        )
        self._append_attr_to_linking_stack(attr=self._italic, attr_name="italic")
