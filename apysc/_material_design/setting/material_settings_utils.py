"""The utility module for getting material design settings.
"""


from typing import Optional

from apysc._color.color import Color
from apysc._material_design.color.material_color_scheme_samples import (
    MaterialColorSchemeSamples
)
from apysc._material_design.color.material_color_scheme import (
    MaterialColorScheme
)


class MaterialSettingsUtils:

    _fixed_color_scheme: MaterialColorScheme

    @classmethod
    def _initialize_fixed_color_scheme_if_not_initialized(cls) -> None:
        """
        Initialize the `_fixed_color_scheme` attribute
        if it has not been initialized yet.
        """
        if hasattr(cls, '_fixed_color_scheme'):
            return
        cls._fixed_color_scheme = (
            MaterialColorSchemeSamples.create_dark_color_scheme_sample_brown_1()
        )

    @classmethod
    def get_primary_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get a primary color setting from setting.

        Parameters
        ----------
        color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target primary color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        from apysc._material_design.setting.material_settings import MaterialSettings
        from apysc._branch._if import If
        from apysc._type.boolean import Boolean
        from apysc._material_design.color.material_color_scheme import (
            MaterialColorScheme
        )

        if argument_color is not None:
            return argument_color

        with If(MaterialSettings.color_scheme_setting_is_enabled()):
            with If(MaterialSettings.current_color_scheme_is_light_color_scheme()):
                color_scheme: Optional[MaterialColorScheme] = (
                    MaterialSettings.get_light_color_scheme()
                )
                if color_scheme is not None:
                    return color_scheme.primary

            with If(MaterialSettings.current_color_scheme_is_dark_color_scheme()):
                color_scheme = MaterialSettings.get_dark_color_scheme()
                if color_scheme is not None:
                    return color_scheme.primary

        cls._initialize_fixed_color_scheme_if_not_initialized()
        pass
