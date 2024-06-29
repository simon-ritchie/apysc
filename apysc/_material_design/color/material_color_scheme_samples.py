"""The class implementation for material design's color scheme samples.
"""

from apysc._material_design.color.material_color_scheme import MaterialColorScheme


class MaterialColorSchemeSamples:
    @classmethod
    def create_light_color_schema_sample_brown_1(cls) -> MaterialColorScheme:
        """
        Create a light color scheme sample setting.

        Returns
        -------
        color_scheme : MaterialColorScheme
            A created color scheme sample setting.

        Notes
        -----
        This setting is created using the material-theme-builder, Apache-2.0 license.

        References
        ----------
        - material-theme-builder
            - https://material-foundation.github.io/material-theme-builder/
        - material-theme-builder GitHub
            - https://github.com/material-foundation/material-theme-builder
        - material-theme-builder license
            - https://github.com/material-foundation/material-theme-builder?tab=Apache-2.0-1-ov-file#readme  # noqa
        """
        from apysc._color.color import Color

        return MaterialColorScheme(
            primary=Color("#8F4C38"),
            on_primary=Color("#FFFFFF"),
            secondary=Color("#77574E"),
            on_secondary=Color("#FFFFFF"),
            error=Color("#BA1A1A"),
            on_error=Color("#FFFFFF"),
            surface=Color("#FFF8F6"),
            on_surface=Color("#231917"),
            primary_container=Color("#FFDBD1"),
            on_primary_container=Color("#3A0B01"),
            secondary_container=Color("#FFDBD1"),
            on_secondary_container=Color("#2C150F"),
            tertiary=Color("#6C5D2F"),
            on_tertiary=Color("#FFFFFF"),
            tertiary_container=Color("#F5E1A7"),
            on_tertiary_container=Color("#231B00"),
            error_container=Color("#FFDAD6"),
            on_error_container=Color("#410002"),
            outline=Color("#85736E"),
            outline_variant=Color("#D8C2BC"),
        )
