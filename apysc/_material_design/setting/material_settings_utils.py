"""The utility module for getting material design settings.
"""

from typing import Optional

from apysc._color.color import Color
from apysc._material_design.color.material_color_scheme import MaterialColorScheme
from apysc._material_design.color.material_color_scheme_names import MaterialColorNames
from apysc._material_design.color.material_color_scheme_samples import (
    MaterialColorSchemeSamples,
)


class MaterialSettingsUtils:

    _fixed_color_scheme: MaterialColorScheme

    @classmethod
    def _initialize_fixed_color_scheme_if_not_initialized(cls) -> None:
        """
        Initialize the `_fixed_color_scheme` attribute
        if it has not been initialized yet.
        """
        if hasattr(cls, "_fixed_color_scheme"):
            return
        cls._fixed_color_scheme = (
            MaterialColorSchemeSamples.create_dark_color_scheme_sample_brown_1()
        )

    @classmethod
    def _set_color_scheme_value_and_append_expression(
        cls,
        *,
        color_scheme: Optional[MaterialColorScheme],
        color_name: MaterialColorNames,
        target_color: Color,
    ) -> None:
        """
        Set a color scheme value to the target color and append
        color-related expressions.

        Notes
        -----
        If the specified `color_scheme` is `None`, then this method
        will do nothing.

        Parameters
        ----------
        color_scheme : Optional[MaterialColorScheme]
            A target color scheme.
        color_name : MaterialColorNames
            A target color name (e.g., "primary").
        target_color : Color
            A target color.
        """
        from apysc._expression import expression_data_util

        if color_scheme is None:
            return

        schgeme_color: Color = getattr(color_scheme, color_name)
        expression_data_util.append_js_expression(
            expression=f"{target_color.variable_name} = "
            f"{schgeme_color.variable_name};"
        )
        target_color._value = schgeme_color._value

    @classmethod
    def _get_target_color_and_add_expressions_by_color_name(
        cls,
        *,
        color_name: MaterialColorNames,
        argument_color: Optional[Color],
    ) -> Color:
        """
        Get a target color and add expressions of the specified
        color name.

        Parameters
        ----------
        color_name : MaterialColorNames
            A target color name (e.g., "primary").
        argument_color : Optional[Color]
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
        from apysc._branch._elif import Elif
        from apysc._branch._else import Else
        from apysc._branch._if import If
        from apysc._material_design.color.material_color_scheme import (
            MaterialColorScheme,
        )
        from apysc._material_design.setting.material_settings import MaterialSettings
        from apysc._type.boolean import Boolean

        cls._initialize_fixed_color_scheme_if_not_initialized()

        if argument_color is not None:
            return argument_color

        target_color: Color = Color("#000000")
        current_color_scheme_is_light_color_scheme: Boolean = (
            MaterialSettings.current_color_scheme_is_light_color_scheme()
        )
        current_color_scheme_is_dark_color_scheme: Boolean = (
            MaterialSettings.current_color_scheme_is_dark_color_scheme()
        )
        with If(MaterialSettings.color_scheme_setting_is_enabled()):
            with If(current_color_scheme_is_light_color_scheme):
                color_scheme: Optional[MaterialColorScheme] = (
                    MaterialSettings.get_light_color_scheme()
                )
                cls._set_color_scheme_value_and_append_expression(
                    color_scheme=color_scheme,
                    color_name=color_name,
                    target_color=target_color,
                )

            with Elif(current_color_scheme_is_dark_color_scheme):
                color_scheme = MaterialSettings.get_dark_color_scheme()
                cls._set_color_scheme_value_and_append_expression(
                    color_scheme=color_scheme,
                    color_name=color_name,
                    target_color=target_color,
                )
        with Else():
            cls._set_color_scheme_value_and_append_expression(
                color_scheme=cls._fixed_color_scheme,
                color_name=color_name,
                target_color=target_color,
            )
        return target_color

    @classmethod
    def get_primary_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get a primary color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `primary` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="primary",
            argument_color=argument_color,
        )

    @classmethod
    def get_on_primary_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get an `on_primary` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `on_primary` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="on_primary",
            argument_color=argument_color,
        )

    @classmethod
    def get_secondary_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get a secondary color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `secondary` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="secondary",
            argument_color=argument_color,
        )

    @classmethod
    def get_on_secondary_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get an `on_secondary` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `on_secondary` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="on_secondary",
            argument_color=argument_color,
        )

    @classmethod
    def get_error_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get an error color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `error` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="error",
            argument_color=argument_color,
        )

    @classmethod
    def get_on_error_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get an `on_error` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `on_error` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="on_error",
            argument_color=argument_color,
        )

    @classmethod
    def get_surface(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get a surface color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `surface` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="surface",
            argument_color=argument_color,
        )

    @classmethod
    def on_surface_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get an `on_surface` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `on_surface` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="on_surface",
            argument_color=argument_color,
        )

    @classmethod
    def get_primary_container_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get a `primary_container` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `primary_container` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="primary_container",
            argument_color=argument_color,
        )

    @classmethod
    def get_on_primary_container_color(
        cls,
        *,
        argument_color: Optional[Color],
    ) -> Color:
        """
        Get an `on_primary_container` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `on_primary_container` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="on_primary_container",
            argument_color=argument_color,
        )

    @classmethod
    def get_secondary_container_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get a `secondary_container` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `secondary_container` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="secondary_container",
            argument_color=argument_color,
        )

    @classmethod
    def get_on_secondary_container_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get an `on_secondary_container` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `on_secondary_container` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="on_secondary_container",
            argument_color=argument_color,
        )

    @classmethod
    def get_tertiary_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get a `tertiary` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `tertiary` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="tertiary",
            argument_color=argument_color,
        )

    @classmethod
    def get_on_tertiary_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get an `on_tertiary` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `on_tertiary` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="on_tertiary",
            argument_color=argument_color,
        )

    @classmethod
    def get_tertiary_container_color(cls, *, argument_color: Optional[Color]) -> Color:
        """
        Get a `tertiary_container` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `tertiary_container` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="tertiary_container",
            argument_color=argument_color,
        )

    @classmethod
    def get_on_tertiary_container_color(
        cls,
        *,
        argument_color: Optional[Color],
    ) -> Color:
        """
        Get an `on_tertiary_container` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `on_tertiary_container` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="on_tertiary_container",
            argument_color=argument_color,
        )

    @classmethod
    def get_error_container_color(
        cls,
        *,
        argument_color: Optional[Color],
    ) -> Color:
        """
        Get an `error_container` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `error_container` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="error_container",
            argument_color=argument_color,
        )

    @classmethod
    def get_on_error_container_color(
        cls,
        *,
        argument_color: Optional[Color],
    ) -> Color:
        """
        Get an `on_error_container` color setting from setting.

        Parameters
        ----------
        argument_color : Optional[Color]
            A specified argument color.

        Returns
        -------
        target_color : Color
            A target `on_error_container` color.
            This value becomes according to the following priorities:
            1. If the `argument_color` is not the `None`
            2. If a color scheme is set in the `MaterialSettings`
            3. A fixed color value.
        """
        return cls._get_target_color_and_add_expressions_by_color_name(
            color_name="on_error_container",
            argument_color=argument_color,
        )
