"""Material icons' shopping cart icon class implementation.
"""

from typing import Optional
from typing import Union

from apysc._color.color import Color
from apysc._display.child_mixin import ChildMixIn
from apysc._material_design.icon.material_icon_base import MaterialIconBase
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class MaterialShoppingCartIcon(MaterialIconBase):
    """
    Material icons' shopping cart icon class implementation.

    References
    ----------
    - Material icons
        - https://fonts.google.com/icons?selected=Material+Icons:search:
    - APACHE LICENSE, VERSION 2.0
        - https://www.apache.org/licenses/LICENSE-2.0.html
    """

    # fill_color
    @arg_validation_decos.is_color(arg_position_index=1, optional=False)
    # fill_alpha
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    # x
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    # y
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    # width
    @arg_validation_decos.num_is_gte_zero(arg_position_index=5, optional=False)
    # height
    @arg_validation_decos.num_is_gte_zero(arg_position_index=6, optional=False)
    # parent
    @arg_validation_decos.is_display_object_container(
        arg_position_index=7, optional=True
    )
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=8, optional=False)
    def __init__(
        self,
        *,
        fill_color: Color,
        fill_alpha: Union[float, Number] = 1.0,
        x: Union[float, Number] = 0,
        y: Union[float, Number] = 0,
        width: Union[int, Int] = 24,
        height: Union[int, Int] = 24,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Material icons' shopping cart icon class implementation.

        Parameters
        ----------
        fill_color : Color
            An icon fill-color.
        fill_alpha : Union[float, Number], optional
            An icon fill-alpha (opacity).
        x : Union[float, Number], optional
            An icon x-coordinate.
        y : Union[float, Number], optional
            An icon y-coordinate.
        width : Union[int, Int], optional
            An icon width.
        height : Union[int, Int], optional
            An icon height.
        parent : ChildMixIn or None, default None
            A parent instance to add this instance.
            If the specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - Material icons
            - https://fonts.google.com/icons?selected=Material+Icons:search:
        - APACHE LICENSE, VERSION 2.0
            - https://www.apache.org/licenses/LICENSE-2.0.html
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.MATERIAL_SHOPPING_CART_ICON,
        )
        super(MaterialShoppingCartIcon, self).__init__(
            svg_path_value="M7 18c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2-.9-2-2-2zM1 2v2h2l3.6 7.59-1.35 2.45c-.16.28-.25.61-.25.96 0 1.1.9 2 2 2h12v-2H7.42c-.14 0-.25-.11-.25-.25l.03-.12.9-1.63h7.45c.75 0 1.41-.41 1.75-1.03l3.58-6.49c.08-.14.12-.31.12-.48 0-.55-.45-1-1-1H5.21l-.94-2H1zm16 16c-1.1 0-1.99.9-1.99 2s.89 2 1.99 2 2-.9 2-2-.9-2-2-2z",  # noqa
            fill_color=fill_color,
            fill_alpha=fill_alpha,
            x=x,
            y=y,
            width=width,
            height=height,
            parent=parent,
            variable_name=variable_name,
            variable_name_suffix=variable_name_suffix,
        )
