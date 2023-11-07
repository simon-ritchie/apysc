"""The mix-in class implementation for `SvgForeignObjectChild`-related
interfaces.
"""

from typing import Union

from apysc._display.svg_foreign_object_child import SvgForeignObjectChild
from apysc._type.string import String


class SvgForeignObjectChildMixIn:
    _svg_foreign_object_child: SvgForeignObjectChild

    def _initialize_svg_foreign_object_child(
        self,
        html_str: Union[str, String],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Initialize the `_svg_foreign_object_child` attribute.

        Parameters
        ----------
        html_str : Union[str, String]
            A HTML string.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._display.add_foreign_object_child_mixin import (
            AddForeignObjectChildMixIn,
        )

        if not isinstance(self, AddForeignObjectChildMixIn):
            raise TypeError(
                "This method can only be called by an "
                "`AddForeignObjectChildMixIn`'s instance."
            )
        self._svg_foreign_object_child = SvgForeignObjectChild(
            html_str=html_str,
            variable_name_suffix=variable_name_suffix,
        )
        self._add_foreign_object_child(child=self._svg_foreign_object_child)
