"""Material icons' face icon class implementation.
"""

from apysc._material_design.icon.path_and_var_name_setting_base import (
    PathAndVarNameSettingBase,
)


class MaterialFaceIcon(PathAndVarNameSettingBase):
    """
    Material icons' search icon class implementation.

    References
    ----------
    - Material icons
        - https://fonts.google.com/icons?selected=Material+Icons:search:
    - APACHE LICENSE, VERSION 2.0
        - https://www.apache.org/licenses/LICENSE-2.0.html
    """

    def _get_svg_path_value(self) -> str:
        """
        Get this icon's SVG path value.

        Returns
        -------
        svg_path_value : str
            This icon's SVG path value.
        """
        return "M9 11.75c-.69 0-1.25.56-1.25 1.25s.56 1.25 1.25 1.25 1.25-.56 1.25-1.25-.56-1.25-1.25-1.25zm6 0c-.69 0-1.25.56-1.25 1.25s.56 1.25 1.25 1.25 1.25-.56 1.25-1.25-.56-1.25-1.25-1.25zM12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8 0-.29.02-.58.05-.86 2.36-1.05 4.23-2.98 5.21-5.37C11.07 8.33 14.05 10 17.42 10c.78 0 1.53-.09 2.25-.26.21.71.33 1.47.33 2.26 0 4.41-3.59 8-8 8z"  # noqa

    def _get_icon_variable_name(self) -> str:
        """
        Get this icon variable name's constant value.

        Returns
        -------
        icon_variable_name : str
            This icon variable name's constant value.
        """
        from apysc._expression import var_names

        return var_names.MATERIAL_FACE_ICON
