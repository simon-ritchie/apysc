"""Material icons' thumb down icon class implementation.
"""

from apysc._material_design.icon.path_and_var_name_setting_base import (
    PathAndVarNameSettingBase,
)


class MaterialThumbDownIcon(PathAndVarNameSettingBase):
    """
    Material icons' thumb down icon class implementation.

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
        return "M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v2c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z"  # noqa

    def _get_icon_variable_name(self) -> str:
        """
        Get this icon variable name's constant value.

        Returns
        -------
        icon_variable_name : str
            This icon variable name's constant value.
        """
        from apysc._expression import var_names

        return var_names.MATERIAL_THUMB_DOWN_ICON
