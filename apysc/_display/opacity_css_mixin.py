"""The mix-in class implementation for the CSS fill-alpha (`opacity`) property.
"""

from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.number import Number


class OpacityCssMixIn(AttrLinkingMixIn):
    _fill_alpha: Number

    def _initialize_fill_alpha(self) -> None:
        """
        Initialize the `_fill_alpha` attribute.
        """
        if hasattr(self, "_fill_alpha"):
            return
        self._fill_alpha = Number(1.0)

    @property
    def fill_alpha(self) -> Number:
        """
        Get a fill-alpha (opacity) value.

        Returns
        -------
        alpha : Number
            A fill-alpha (opacity) value.
        """
        self._initialize_fill_alpha()
        return self._fill_alpha._copy()

    @fill_alpha.setter
    def fill_alpha(self, value: Number) -> None:
        """
        Set a fill-alpha (opacity) value.

        Parameters
        ----------
        value : Number
            A fill-alpha (opacity) value.
        """
        from apysc._display.css_interface import CssInterface

        if not isinstance(self, CssInterface):
            raise TypeError(
                "This method can only be called on an instance of `CssInterface` class."
            )
        self._fill_alpha = value
        self.set_css(
            name="opacity",
            value=self._fill_alpha.to_string(),
        )

        self._append_applying_new_attr_val_exp(
            new_attr=self._fill_alpha, attr_name="fill_alpha"
        )
        self._append_attr_to_linking_stack(
            attr=self._fill_alpha, attr_name="fill_alpha"
        )
