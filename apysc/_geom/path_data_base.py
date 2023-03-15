"""Base class implementation for the path data.
"""

from abc import ABC
from abc import abstractmethod
from typing import Union

from typing_extensions import final

from apysc._branch._else import Else
from apysc._branch._if import If
from apysc._geom.path_label import PathLabel
from apysc._geom.relative_mixin import RelativeMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_to_apysc_val_from_builtin_mixin import (
    AttrToApyscValFromBuiltinMixIn,
)
from apysc._type.boolean import Boolean
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class PathDataBase(RelativeMixIn, AttrToApyscValFromBuiltinMixIn, ABC):
    """
    Base class for the path data.
    """

    _path_label: PathLabel

    @arg_validation_decos.is_boolean(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self, *, path_label: PathLabel, relative: Union[bool, Boolean]
    ) -> None:
        """
        Base class for the path data.

        Parameters
        ----------
        path_label : PathLabel
            Target (SVG's) path label.
        relative : bool or Boolean
            A boolean value indicates whether the path
            coordinates are relative or not (absolute).
        """
        self._path_label = path_label
        self.relative = self._get_copied_boolean_from_builtin_val(
            bool_val=relative, attr_identifier="relative"
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_svg_char(self) -> String:
        """
        Get a SVG character (e.g., 'M' or 'm') from the
        current setting.

        Returns
        -------
        svg_char : String
            Target SVG character.
        """
        svg_char_: str = self._path_label.value
        if self._relative._value:
            svg_char: String = String(
                svg_char_.lower(), variable_name_suffix=self._variable_name_suffix
            )
        else:
            svg_char = String(
                svg_char_, variable_name_suffix=self._variable_name_suffix
            )
        with If(self._relative, locals_=locals()):
            svg_char.value = svg_char_.lower()
        with Else(locals_=locals()):
            svg_char.value = svg_char_
        return svg_char

    @abstractmethod
    def _get_svg_str(self) -> str:
        """
        Get a path's SVG string created with the current setting.
        """
