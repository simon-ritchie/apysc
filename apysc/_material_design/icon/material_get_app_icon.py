"""Material icons' get app icon class implementation.
"""

from apysc._material_design.icon.path_and_var_name_setting_base import (
    PathAndVarNameSettingBase,
)


class MaterialGetAppIcon(PathAndVarNameSettingBase):
    """
    Material icons' get app icon class implementation.

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
        return "M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"

    def _get_icon_variable_name(self) -> str:
        """
        Get this icon variable name's constant value.

        Returns
        -------
        icon_variable_name : str
            This icon variable name's constant value.
        """
        from apysc._expression import var_names

        return var_names.MATERIAL_GET_APP_ICON
