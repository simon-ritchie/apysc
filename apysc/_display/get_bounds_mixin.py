"""The mix-in class implementation for the `get_bounds` method.
"""

from typing_extensions import final

from apysc._geom.rectangle_geom import RectangleGeom
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.variable_name_mixin import VariableNameMixIn


class GetBoundsMixIn(VariableNameMixIn):
    @final
    @add_debug_info_setting(module_name=__name__)
    def get_bounds(self) -> RectangleGeom:
        """
        Get an instance's bounding-box geometry data.

        Returns
        -------
        bounding_box : RectangleGeom
            An instance's bounding-box geometry data.

        References
        ----------
        - get_bounds interface
            - https://simon-ritchie.github.io/apysc/en/get_bounds.md
        - RectangleGeom class
            - https://simon-ritchie.github.io/apysc/en/rectangle_geom.html

        Examples
        --------
        >>> import apysc as ap

        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"), stage_width=250, stage_height=350
        ... )
        >>> rectangle: ap.Rectangle = ap.Rectangle(
        ...     x=50,
        ...     y=100,
        ...     width=150,
        ...     height=200,
        ...     fill_color=ap.Color("#0af"),
        ... )
        >>> bounding_box: ap.RectangleGeom = rectangle.get_bounds()
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="left_x"
        )
        left_x: Number = Number(0, variable_name_suffix=suffix)

        suffix = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="center_x"
        )
        center_x: Number = Number(0, variable_name_suffix=suffix)

        suffix = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="right_x"
        )
        right_x: Number = Number(0, variable_name_suffix=suffix)

        suffix = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="top_y"
        )
        top_y: Number = Number(0, variable_name_suffix=suffix)

        suffix = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="center_y"
        )
        center_y: Number = Number(0, variable_name_suffix=suffix)

        suffix = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="bottom_y"
        )
        bottom_y: Number = Number(0, variable_name_suffix=suffix)

        suffix = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="width"
        )
        width: Int = Int(0, variable_name_suffix=suffix)

        suffix = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="height"
        )
        height: Int = Int(0, variable_name_suffix=suffix)
        self._append_get_bounds_expression(
            left_x=left_x,
            center_x=center_x,
            right_x=right_x,
            top_y=top_y,
            center_y=center_y,
            bottom_y=bottom_y,
            width=width,
            height=height,
        )
        bounding_box: RectangleGeom = RectangleGeom(
            left_x=left_x,
            center_x=center_x,
            right_x=right_x,
            top_y=top_y,
            center_y=center_y,
            bottom_y=bottom_y,
            width=width,
            height=height,
        )
        return bounding_box

    def _append_get_bounds_expression(
        self,
        *,
        left_x: Number,
        center_x: Number,
        right_x: Number,
        top_y: Number,
        center_y: Number,
        bottom_y: Number,
        width: Int,
        height: Int,
    ) -> None:
        """
        Append a `get_counds` method expression string.

        Parameters
        ----------
        left_x : Number
            The rectangle left x coordinate.
        center_x : Number
            The rectangle center x coordinate.
        right_x : Number
            The rectangle right x coordinate.
        top_y : Number
            The rectangle top y coordinate.
        center_y : Number
            The rectangle center y coordinate.
        bottom_y : Number
            The rectangle bottom y coordinate.
        width : Int
            The rectangle width.
        height : Int
            The Rectangle height.
        """
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage
        from apysc._expression import expression_data_util

        stage: Stage = get_stage()
        expression: str = (
            f"var box = {self.variable_name}.rbox({stage.variable_name});"
            f"\n{left_x.variable_name} = box.x;"
            f"\n{center_x.variable_name} = box.cx;"
            f"\n{right_x.variable_name} = box.x2;"
            f"\n{top_y.variable_name} = box.y;"
            f"\n{center_y.variable_name} = box.cy;"
            f"\n{bottom_y.variable_name} = box.y2;"
            f"\n{width.variable_name} = box.width;"
            f"\n{height.variable_name} = box.height;"
        )
        expression_data_util.append_js_expression(expression=expression)
