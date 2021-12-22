"""Base class implementation for the path data.
"""

from abc import ABC
from abc import abstractmethod
from typing import Union

from apysc._branch._else import Else
from apysc._branch._if import If
from apysc._geom.path_label import PathLabel
from apysc._geom.relative_interface import RelativeInterface
from apysc._type.boolean import Boolean
from apysc._type.string import String


class PathDataBase(RelativeInterface, ABC):
    """
    Base class for the path data.
    """

    _path_label: PathLabel

    def __init__(
            self, *, path_label: PathLabel,
            relative: Union[bool, Boolean]) -> None:
        """
        Base class for the path data.

        Parameters
        ----------
        path_label : PathLabel
            Target (svg's) path label.
        relative : bool or Boolean
            The boolean value indicating whether the path
            coordinates are relative or not (absolute).
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=PathDataBase):
            from apysc._converter.to_apysc_val_from_builtin import \
                get_copied_boolean_from_builtin_val
            self._path_label = path_label
            self.relative = get_copied_boolean_from_builtin_val(
                bool_val=relative)

    def _get_svg_char(self) -> String:
        """
        Get a SVG character (e.g., 'M' or 'm') from the
        current setting.

        Returns
        -------
        svg_char : String
            Target SVG character.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._get_svg_char, locals_=locals(),
                module_name=__name__, class_=PathDataBase):
            svg_char_: str = self._path_label.value
            if self._relative._value:
                svg_char: String = String(svg_char_.lower())
            else:
                svg_char = String(svg_char_)
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
