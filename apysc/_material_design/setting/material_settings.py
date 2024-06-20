"""The static class implementation for the material design settings.
"""

from typing import Optional
from apysc._material_design.color.material_color_scheme import MaterialColorScheme


class MaterialSettings:

    _color_scheme: Optional[MaterialColorScheme] = None

    @classmethod
    def get_color_scheme(cls) -> Optional[MaterialColorScheme]:
        """
        Get a color scheme setting.

        Returns
        -------
        color_scheme : MaterialColorScheme or None
            A color scheme setting. If the color scheme is not set,
            this property becomes None.
        """
        return cls._color_scheme

    @classmethod
    def set_color_scheme(cls, *, color_scheme: Optional[MaterialColorScheme]) -> None:
        """
        Set a color scheme setting.

        Parameters
        ----------
        color_scheme : MaterialColorScheme or None
            Color scheme to set. If None is specified, the color scheme
            will be removed.
        """
        cls._color_scheme = color_scheme
