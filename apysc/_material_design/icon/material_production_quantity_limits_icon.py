"""Material icons' production quantity limits icon class implementation.
"""

from apysc._material_design.icon.path_and_var_name_setting_base import (
    PathAndVarNameSettingBase,
)


class MaterialProductionQuantityLimitsIcon(PathAndVarNameSettingBase):
    """
    Material icons' production quantity limits icon class implementation.

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
        return "M13,10h-2V8h2V10z M13,6h-2V1h2V6z M7,18c-1.1,0-1.99,0.9-1.99,2S5.9,22,7,22s2-0.9,2-2S8.1,18,7,18z M17,18 c-1.1,0-1.99,0.9-1.99,2s0.89,2,1.99,2s2-0.9,2-2S18.1,18,17,18z M8.1,13h7.45c0.75,0,1.41-0.41,1.75-1.03L21,4.96L19.25,4l-3.7,7 H8.53L4.27,2H1v2h2l3.6,7.59l-1.35,2.44C4.52,15.37,5.48,17,7,17h12v-2H7L8.1,13z"  # noqa

    def _get_icon_variable_name(self) -> str:
        """
        Get this icon variable name's constant value.

        Returns
        -------
        icon_variable_name : str
            This icon variable name's constant value.
        """
        from apysc._expression import var_names

        return var_names.MATERIAL_PRODUCTION_QUANTITY_LIMITS_ICON
