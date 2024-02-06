"""Material icons' trending flat icon class implementation.
"""

from apysc._material_design.icon.path_and_var_name_setting_base import (
    PathAndVarNameSettingBase,
)


class MaterialTrendingFlatIcon(PathAndVarNameSettingBase):
    """
    Material icons' trending flat icon class implementation.

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
        return "M22 12l-4-4v3H3v2h15v3z"

    def _get_icon_variable_name(self) -> str:
        """
        Get this icon variable name's constant value.

        Returns
        -------
        icon_variable_name : str
            This icon variable name's constant value.
        """
        from apysc._expression import var_names

        return var_names.MATERIAL_TRENDING_FLAT_ICON
