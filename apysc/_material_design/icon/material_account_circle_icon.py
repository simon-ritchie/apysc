"""Material icons' account circle icon class implementation.
"""

from typing import Optional
from typing import Union

from apysc._color.color import Color
from apysc._display.child_mixin import ChildMixIn
from apysc._material_design.icon.material_icon_base import MaterialIconBase
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class MaterialAccountCircleIcon(MaterialIconBase):
    """
    Material icons' account circle icon class implementation.

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
        Material icons' account circle icon class implementation.

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
            type_name=var_names.MATERIAL_ACCOUNT_CIRCLE_ICON,
        )
        super(MaterialAccountCircleIcon, self).__init__(
            svg_path_value="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 4c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6zm0 14c-2.03 0-4.43-.82-6.14-2.88C7.55 15.8 9.68 15 12 15s4.45.8 6.14 2.12C16.43 19.18 14.03 20 12 20z",  # noqa
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
